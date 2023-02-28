from flask import Flask, request, render_template

app = Flask(__name__)

# This is the partner server, it is not configured with CORS.
# Running it this way as loading partner.html as a file in browser seems to confuse the origin/stuff

@app.route('/partner', methods=['GET'])
def index():
	return render_template('partner.html')


if __name__ == '__main__':
	app.run(port=5000)
