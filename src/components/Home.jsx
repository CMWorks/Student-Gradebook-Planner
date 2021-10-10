import React from "react";

class Home extends React.Component {

  render() {
    var myHeaders = {
			'Content-Type': 'application/json',
			Authorization: 'Bearer 12345'
		}

			fetch('http://127.0.0.1:5000/companies', {
				headers: myHeaders
			}).then(res => res.json().then(data => console.log(data)))

    return (
      <div className="home">
        <div className="container">
          <div className="row align-items-center my-5">
            <div className="col-lg-7">
              <img
                className="img-fluid rounded mb-4 mb-lg-0"
                src="http://placehold.it/900x400"
                alt=""
              />
            </div>
            <div className="col-lg-5">
              <h1 className="font-weight-light">Home</h1>
              <p>
                Lorem Ipsum is simply dummy text of the printing and typesetting
                industry. Lorem Ipsum has been the industry's standard dummy text
                ever since the 1500s, when an unknown printer took a galley of
                type and scrambled it to make a type specimen book.
              </p>
            </div>
          </div>
        </div>
      </div>
    );
  }
}

export default Home;