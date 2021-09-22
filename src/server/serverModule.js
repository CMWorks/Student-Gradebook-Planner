const crypto = require('crypto')

class serverModule {

	/**
	Gets autherization token from server and saves it
	returns true if successful
	returns false in user cradentials (email or password) is invalid
	*/
	// secure(email, password) {
	// 	this.authenticate(email, password).then((data) => {
	// 		if (data.status === 401) return false
	// 		this.token = data.access_token;
	// 		this.myHeaders = {
	// 			'Content-Type': 'application/json',
	// 			'Authorization': ('Bearer ' + this.token)
	// 		}
	// 		return true
	// 	})
	// }

	/**
	retisters user to users.json
	returns true if user was registered
	returns false in email is already used
	Note: this does not add the user to the main databse, it just adds them to user.json
	*/
	// registerUser(Email, Password) {
	// 	let userdata = {
	// 		email: Email,
	// 		password: Password
	// 	}

	// 	this.register(userdata).then((data) => {
	// 		if (data.status === 401) return false
	// 		else return true
	// 	});
	// }

	/**
	Retrieves user by userID
	returns user object
	*/
	// getUser(userID) {
	// 	this.get(userID).then((data) => {
	// 		this.obj = data[0];
	// 		return data[0]
	// 	})
	// }

	deleteUser = async (userID) => {
		await fetch('http://localhost:5000/users/' + userID, { method: 'DELETE', headers: this.myHeaders })
	}

	/**
	Adds user to database
	returns the user with his id attached
	*/
	addUser = async (data) => {
		const res = await fetch('http://localhost:5000/users', {
			method: 'POST',
			headers: this.myHeaders,
			body: JSON.stringify(data)
		})
		const ret = await res.json()
		return ret
	}

	/**
	updates user with new data
	NOTE: id is different from userID, this is the databse id
	you guys will only use this function to update
	returns the responce from server
	*/
	updateUser = async (id, new_data) => {
		const res = await fetch('http://localhost:5000/users/' + id, {
			method: 'PUT',
			headers: this.myHeaders,
			body: JSON.stringify(new_data)
		})
		const data = await res.json()
		return data
	}

	authenticate = async (eHash, idHash) => {
		const res = await fetch('http://localhost:5000/auth/login', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: '{"eHash":"' + eHash + '","iHash": "' + idHash + '"}',
		})
		const data = await res.json()
		return data
		//authenticate().then(function(object){t = object.access_token})
	}

	register = async (userdata) => {
		const res = await fetch('http://localhost:5000/auth/register', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(userdata),
		})
		const data = await res.json()
		return data
	}

	get = async (userID) => {
		const res = await fetch('http://localhost:5000/users?userID_like=' + userID, {
			headers: this.myHeaders
		})
		const data = await res.json()
		return data
	}

	generateHash(email, password) {
		return crypto.createHash('sha512').update(email + password).digest('hex')
	}

	constructor() {
		this.token = ""
		this.obj = {}
		this.myHeaders = { 'Content-Type': 'application/json' }
	}
}

export default serverModule
