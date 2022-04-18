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
	"3": {
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
		"cars_from": {"A": [3, 4, "Car", "W"], "B":[6, 3, "Car", "E"]},
		"cars_to": {"A": [4,4, "Car", "W"], "B":[3, 3,  "Car", "N"]},
		"answer": ["A"]
	},
	"4": {
		"prompt": "Which car should go first?",
		"terrain": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 0, 0, 0], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4, 3, "Car", "W"], "B":[5, 4, "Car", "W"]},
		"cars_to": {"A": [7, 3, "Car", "W"], "B":[7, 3,  "Car", "W"]},
		"answer": ["B"]
	},
	"5": {
		"prompt": "Which way should car A yield?",
		"terrain": [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4, 3, "Car", "W"], "B":[3, 3, "Ambulance", "W"]},
		"cars_to": {"A": [5,3, "Car", "W"], "B":[4, 3,  "Ambulance", "W"]},
		"answer": ["Right"]
	},
	"6": {
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
		"cars_from": {"A": [4,2, "Car", "N"], "B":[3, 4, "Car", "W"], "C":[6, 3, "Car", "E"]},
		"cars_to": {"A": [4,5, "Car", "N"], "B":[5, 2, "Car", "S"], "C":[3, 3,  "Car", "E"]},
		"answer": ["C", "A", "B"]
	}
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

