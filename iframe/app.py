from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
	return render_template('index.html')

@app.route('/store-form', methods=['POST'])
def store_form():
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

