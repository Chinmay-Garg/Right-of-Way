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
		"prompt": "Which car should go first?",
		"terrain": [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4,2, "Car", "N"], "B":[6, 3, "Car", "E"]},
		"cars_to": {"A": [4,5, "Car", "N"], "B":[3, 3,  "Car", "E"]},
		"answer": ["B"]
	},
	"2": {
		"prompt": "Which car should go first?",
		"terrain": [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4,2, "Car", "N"], "B":[6, 3, "Car", "E"]},
		"cars_to": {"A": [4,5, "Car", "N"], "B":[4, 5,  "Car", "N"]},
		"answer": ["B"]
	},
}


# ROUTES
@app.route('/')
def hello_world():
   return render_template('welcome.html')

@app.route('/view/<idx>')
def learningpage(idx=None):

	return render_template('learning_page.html', topics=topics)

@app.route('/quiz/<idx>')
def quizpage(idx=None):
	for question in questions:
		print(question, questions[question])
		if question == idx:
			return render_template('quiz_page.html', questions=questions[question])		
	return render_template('quiz_page.html', questions={})

# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)

