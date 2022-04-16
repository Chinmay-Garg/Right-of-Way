from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# VARIABLES
topics = {
	"1": {
		"title": "",
		"image": "",
		"video": "",
		"summary": ""
	},
}
questions = {
	"1": {
		"prompt": "",
		"road": "",
		"cars": ["", ""]
	},
}

# ROUTES
@app.route('/')
def hello_world():
   return render_template('welcome.html')

@app.route('/view/<id>')
def learningpage(id=None):

	return render_template('learning_page.html', topics=topics)

@app.route('/quiz/<id>')
def quizpage(id=None):

	return render_template('quiz_page.html', questions=questions)

# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)

