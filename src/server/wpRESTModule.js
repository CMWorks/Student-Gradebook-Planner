const crypto = require('crypto')

class RESTModule {

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

	getAllFromTable = async (table, foreignKey) => {
		const res = await fetch(this.serverLocation + this.apiVersion + table + "?foreignKey="+foreignKey, {
			headers: this.myHeaders
		})
		const data = await res.json()
		return data
	}

	getUserData = async (table, id) => {
		console.log(this.myHeaders)
		const res = await fetch(this.serverLocation + this.apiVersion + table + "/" + id, {
			headers: this.myHeaders
		})
		const data = await res.json()
		return data
	}

	deleteUserData = async (table, id) => {
		await fetch(this.serverLocation + this.apiVersion + table + "/" + id, { method: 'DELETE', headers: this.myHeaders })
	}

	/**
	Adds user to database
	returns the user with his id attached
	*/
	addUserData = async (table, id, data) => {
		const res = await fetch(this.serverLocation + this.apiVersion + table + "/" + id, {
			method: 'POST',
			headers: this.myHeaders,
			body: JSON.stringify(data)
		})
		const ret = await res.json()
		return ret
	}

	/**
	updates table row with new data
	NOTE: id is different from userID, this is the databse id
	you guys will only use this function to update
	returns the responce from server
	*/
	updateUserData = async (table, id, new_data) => {
		const res = await fetch(this.serverLocation + this.apiVersion + table + "/" + id, {
			method: 'PUT',
			headers: this.myHeaders,
			body: JSON.stringify(new_data)
		})
		const data = await res.json()
		return data
	}

	authenticate = async (eHash, idHash) => {
		const res = await fetch(this.serverLocation + this.apiVersion + 'auth/login', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: '{"eHash":"' + eHash + '","iHash": "' + idHash + '"}',
		})
		const data = await res.json()
		return data
		//authenticate().then(function(object){t = object.access_token})
	}

	register = async (userdata) => {
		const res = await fetch(this.serverLocation + this.apiVersion + 'auth/register', {
			method: 'POST',
			headers: { 'Content-Type': 'application/json' },
			body: JSON.stringify(userdata),
		})
		const data = await res.json()
		return data
	}

	generateHash(email, password) {
		return crypto.createHash('sha256').update(email + password).digest('base64')
		// return parseInt( crypto.createHash('sha256').update(email + password).digest('hex').split('').reverse().join(''), 16);
	}

	constructor() {
		this.token = ""
		this.obj = {}
		this.myHeaders = { 'Content-Type': 'application/json' };
		this.serverLocation = "http://127.0.0.1:5000/";
		this.apiVersion = "v1/"
	}
}

export default RESTModule
