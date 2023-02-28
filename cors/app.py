from flask import Flask, request, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/ajax")
def ajax():
  return "This is the response from the remote server. The remote server is configured to allow cross origin requests"

if __name__ == '__main__':
	app.run(port=5050)
