from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# VARIABLES
topics = {
	"1": {
		"title": "What is right of way?",
		"image": "https://static.epermittest.com/media/filer_public/39/96/3996a095-6318-4316-9a17-5caf6152c550/right-of-way-rules.jpg",
		"video": "https://www.youtube.com/embed/U3NAK7lKaws?start=13&end=57",
		"summary": "When driving, the rules of the road that establish who has the right to go first is called <b>right of way</b>." +
		"As a driver, right of way should be <b>given</b> based on the right-of-way rules in the various scenarios we will cover."
	},
	"2": {
		"title": "Controlled Intersections",
		"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
		"video": "https://www.youtube.com/embed/VWXgqPzADGQ?start=18&end=152",
		"summary": "A controlled intersection a point where multiple roads cross over, and it being controlled means it has signs, traffic lights, and/or road signs to guide drivers." +
		"A tool to manage who goes first is <b>FIFO</b>, or <b>first in, first out</b>, meaning the driver that stops at the intersection first has the right of way." 
	},
	"3": {
		"title": "Uncontrolled Intersections",
		"image": "https://1.bp.blogspot.com/-2HZxRE3jUcM/X3hNmgE0S9I/AAAAAAAAA_8/m_qWBreBUnswSgBe011H9bWdoLHvSum6QCLcBGAsYHQ/w1200-h630-p-k-no-nu/two-cars-uncontrolled-intersection.jpg",
		"video": "https://www.youtube.com/embed/zbc-SVuHTKo?start=14&end=81",
		"summary": "An uncontrolled intersection has no stop signs or traffic lights. This makes yielding extra important." +
		"Right of way should always be given to pedestrians, emergency vehicles, <b>and the driver to your right.</b>" 
	},
	"4": {
		"title": "Emergency Vehicles",
		"image": "https://www.fountainvalley.org/ImageRepository/Document?documentID=10622",
		"video": "https://www.youtube.com/embed/8MpfC3mIvhs?start=4&end=83",
		"summary": "In the case of an emergency vehicle passing, it is important to allow them the right of way <b>as soon as possible in a safe manner.</b>" +
		"The rule of thumb is to <b>move to the closet lane, and moving to the right side if you are in the center lane.</b>"
	},
	"5": {
		"title": "Multi-lane Roundabouts",
		"image": "https://driving-test-success.com/roundabouts/roundabout-image.jpg",
		"video": "https://www.youtube.com/embed/CEhNboz5GPk?start=114&end=238",
		"summary": "Multi-lane roundabouts are designed to slow traffic and minimize accidents. However, they can be confusing, even for an experienced driver." +
		"The key is to stop, know which lane you are taking, wait for a gap <b>in all lanes of traffic</b>, and the proceed <b>slowly</b>." 
	}
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

answers = {1:["B"], 2:["B"], 3:["A"], 4:["B"], 5:["Right"], 6:["C", "A", "B"]}

# ROUTES
@app.route('/')
def hello_world():
   return render_template('welcome.html')

@app.route('/learn/<idx>')
def learningpage(idx=None):
	global topic
	topic = topics[idx]

	return render_template('learning_page.html', topic=topic)

@app.route('/quiz')
def transitionpage():
	return render_template('quiz_home.html')

@app.route('/quiz/end')
def transitionpage():
	return render_template('quiz_end.html')

@app.route('/quiz/<idx>')
def quizpage(idx=None):
	for question in questions:
		print(question, questions[question])
		if question == idx:
			return render_template('quiz_page.html', questions=questions[question])		
	return render_template('quiz_page.html', questions={})

@app.route('/answers')
def answers():
	return answers
# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)

