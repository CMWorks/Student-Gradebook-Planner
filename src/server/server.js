const fs = require('fs')
const bodyParser = require('body-parser')
const jsonServer = require('json-server')
const jwt = require('jsonwebtoken')

const server = jsonServer.create()
const router = jsonServer.router('./db.json')
var userdb = JSON.parse(fs.readFileSync('./users.json', 'UTF-8'))

server.use(bodyParser.urlencoded({ extended: true }))
server.use(bodyParser.json())
server.use(jsonServer.defaults());

const SECRET_KEY = '123456789'

const AUTH_ON = true
const USER_ID_REQ = '/?userID_like='

const expiresIn = '1h'

function cleanQuery(query) {
  let a = query.split("_like=")[1]
  while (a.includes('[')) {
    a = a.replace("[", "")
  }
  while (a.includes(']')) {
    a = a.replace("]", "")
  }
  while (a.includes('^')) {
    a = a.replace("^", "")
  }
  while (a.includes('$')) {
    a = a.replace("$", "")
  }
  return "^" + a + "$"
}

// Create a token from a payload
function createToken(payload) {
  return jwt.sign(payload, SECRET_KEY, { expiresIn })
}

// Verify the token
function verifyToken(token) {
  return jwt.verify(token, SECRET_KEY, (err, decode) => decode !== undefined ? decode : err)
}

// Check if the user already exists in database
function isAuthenticated({ eHash, iHash }) {
  return userdb.users.findIndex(user => user.eHash === eHash || user.iHash === iHash) !== -1
}

// Check if the users full cradentials is correct
function isAuthenticatedFull({ eHash, iHash }) {
  return userdb.users.findIndex(user => user.eHash === eHash && user.iHash === iHash) !== -1
}

// Register New User
server.post('/auth/register', (req, res) => {
  console.log("register endpoint called; request body:");
  console.log(req.body);
  const { eHash, iHash } = req.body;

  if (isAuthenticated({ eHash, iHash }) === true) {
    const status = 401;
    const message = 'Email already exist';
    res.status(status).json({ status, message });
    return
  }

  fs.readFile("./users.json", (err, data) => {
    if (err) {
      const status = 401
      const message = err
      res.status(status).json({ status, message })
      return
    };

    // Get current users data
    var data = JSON.parse(data.toString());


    // Get the id of last user
    var last_item_id = data.users[data.users.length - 1].id;

    //Add new user
    data.users.push({ id: last_item_id + 1, eHash: eHash, iHash: iHash }); //add some data
    userdb = data
    var writeData = fs.writeFile("./users.json", JSON.stringify(data), (err, result) => {  // WRITE
      if (err) {
        const status = 401
        const message = err
        res.status(status).json({ status, message })
        return
      }
    });
  });

  // Create token for new user
  const access_token = createToken({ eHash, iHash })
  console.log("Access Token:" + access_token);
  res.status(200).json({ access_token })
})

// Login to one of the users from ./users.json
server.post('/auth/login', (req, res) => {
  console.log("login endpoint called; request body:");
  console.log(req.body);
  const { eHash, iHash } = req.body;
  if (isAuthenticatedFull({ eHash, iHash }) === false) {
    const status = 401
    const message = 'Incorrect email or password'
    res.status(status).json({ status, message })
    return
  }
  const access_token = createToken({ eHash, iHash })
  console.log("Access Token:" + access_token);
  res.status(200).json({ access_token })

  // crypto.randomBytes(32, (err, salt) => {
  //   if (err) throw err;
  //   argon2i.hash(email + password, salt).then(hash => {
  //     console.log("Access Token:" + access_token);
  //     res.status(200).json({ access_token, hash })
  //   })
  // })

})

server.use(/^(?!\/auth).*$/, (req, res, next) => {
  // url: /?postID_like=1
  // baseURL: /auth/login
  // method: GET

  if ("userID_like" in req.query && req.url.includes(USER_ID_REQ)) {
    req.query.userID_like = cleanQuery(req.url)
  }
  else {
    req.query.userID_like = "^$"
  }

  if (AUTH_ON) {
    if (req.headers.authorization === undefined || req.headers.authorization.split(' ')[0] !== 'Bearer' || (req.method == "GET" && (!req.url.includes(USER_ID_REQ) || req.url == USER_ID_REQ || req.baseUrl.split('/').length != 2))) {
      console.log("IN")
      const status = 401
      const message = 'Error in authorization format'
      res.status(status).json({ status, message })
      return
    }
    try {
      let verifyTokenResult;
      verifyTokenResult = verifyToken(req.headers.authorization.split(' ')[1]);

      if (verifyTokenResult instanceof Error) {
        const status = 401
        const message = 'Access token not provided'
        res.status(status).json({ status, message })
        return
      }
      next()
    } catch (err) {
      const status = 401
      const message = 'Error access_token is revoked'
      res.status(status).json({ status, message })
    }
  } else {
    next()
  }
})

server.use(router)

server.listen(5000, () => {
  console.log('Run Auth API Server')
})
