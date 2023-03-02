from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ajax")
def ajax():
  return "This is the response from the remote server. The remote server is configured to allow cross origin requests"

@app.route('/store-form', methods=['POST'])
def store_form():
	print("Storing form data...")
	data = request.form
	
	# Store to database here
	print("form data:", data)

	return {
		'emailId'	 : data['userEmail'],
		'phoneNumber' : data['userContact'],
		'password' : data['userPassword'],
		'gender'	 : 'Male' if data['genderMale'] else 'Female',
	}

if __name__ == '__main__':
	app.run(port=5050)
