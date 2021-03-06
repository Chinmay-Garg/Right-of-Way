from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)


# VARIABLES
topics = {
	"1": {
		"title": "Overview: What is right of way?",
		"image": "https://amaabcaprod.azureedge.net/content/images/articles/right-of-way-intersection_example_4.jpg",
		"video": "learning1.mp4",
		"source": "https://www.youtube.com/embed/U3NAK7lKaws?start=13&end=57",
		"summary": "When driving, the rules of the road that establish who has the right to go first is called right of way. " +
		"As a driver, right of way should be given based on the right-of-way rules in the various scenarios we will cover."
	},
	"2": {
		"title": "Controlled Intersections: FIFO",
		"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
		"video": "learning2.mp4",
		"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=18&end=43",
		"summary": "A controlled intersection is a point where multiple roads cross over. It being controlled means it has signs, traffic lights, and/or road signs to guide drivers. " +
		"A tool to manage who goes first is FIFO, or first in, first out, meaning the driver that stops at the intersection first has the right of way." 
	},
	"3": {
		"title": "Controlled Intersections: Rightmost side",
		"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
		"video": "learning3.mp4",
		"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=43&end=92",
		"summary": "In the case where multiple cars get to the intersection at the same time, the driver on the rightmost side should go first. If there are four cars in the intersection, whoever slowly advances first should go. "
	},
	"4": {
		"title": "Uncontrolled Intersections: Pedestrians",
		"image": "https://1.bp.blogspot.com/-2HZxRE3jUcM/X3hNmgE0S9I/AAAAAAAAA_8/m_qWBreBUnswSgBe011H9bWdoLHvSum6QCLcBGAsYHQ/w1200-h630-p-k-no-nu/two-cars-uncontrolled-intersection.jpg",
		"video": "learning4.mp4",
		"source": "https://www.youtube.com/embed/zbc-SVuHTKo?start=60&end=81",
		"summary": "An uncontrolled intersection has no stop signs or traffic lights. This makes yielding to right of way extra important. " +
		"The right of way should always be given to pedestrians." 
	},
	"5": {
		"title": "Emergency Vehicles",
		"image": "https://www.fountainvalley.org/ImageRepository/Document?documentID=10622",
		"video": "learning5.mp4",
		"source": "https://www.youtube.com/embed/8MpfC3mIvhs?start=36&end=83",
		"summary": "In the case of an emergency vehicle passing, it is important to allow them the right of way and give them ample space soon as possible in a safe manner. " +
		"The rule of thumb is to move to the closest lane, moving to the right side if you are in the center lane."
	},
	"6": {
		"title": "Multi-lane Roundabouts",
		"image": "https://driving-test-success.com/roundabouts/roundabout-image.jpg",
		"video": "learning6.mp4",
		"source": "https://www.youtube.com/embed/CEhNboz5GPk?start=197&end=238",
		"summary": "Multi-lane roundabouts are designed to slow traffic and minimize accidents. However, they can be confusing, even for an experienced driver. " +
		"The key is to stop, know which lane you are taking, and yield until all lanes of traffic are free, and then proceed slowly." 
	}
}
questions = {
	"1": {
		"prompt": "Which car should go first at this intersection if they both arrived at the same time?",
		"terrain": 	   [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7 0
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6 1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5 2
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4 3
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3 4
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2 5
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1 6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0 7
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [5, 5, "Car", "N", "\u2191"], "B":[3, 6, "Car", "W", "\u2191"]},
		"cars_to": {"A": [2, 5, "Car", "N", "A"], "B":[3, 3, "Car", "W", "B"]},
		"horizontal_lane": {"30": 0, "31": 0, "32": 0, "33": 0, "36": 0, "37": 0, "38": 0, "39": 0},
		"vertical_lane": {"04": 0, "14": 0, "24": 0, "54": 0, "64": 0, "74": 0},
		"hint": {
			"title": "Controlled Intersections: Rightmost side",
			"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
			"video": "learning3.mp4",
			"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=43&end=92",
			"summary": "In the case where multiple cars get to the intersection at the same time, the driver on the rightmost side should go first. If there are four cars in the intersection, whoever slowly advances first should go. "
	},
		"answer": ["B"],
		"answer_summary": "Yellow car should go first as it's on the rightmost side."
	},
	"2": {
		"prompt": "Which car should go first at this intersection if the car in the blue box arrived first?",
		"terrain": 		[[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [5, 5, "Car", "N", "\u2191"], "B":[3, 6, "Car", "W", "\u2191"]},
		"cars_to": {"A": [2,5, "Car", "N", "A"], "B":[3, 3,  "Car", "N", "B"]},
		"horizontal_lane": {"30": 0, "31": 0, "32": 0, "33": 0, "36": 0, "37": 0, "38": 0, "39": 0},
		"vertical_lane": {"04": 0, "14": 0, "24": 0, "54": 0, "64": 0, "74": 0},
		"hint": {
			"title": "Controlled Intersections: FIFO",
			"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
			"video": "learning2.mp4",
			"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=18&end=43",
			"summary": "A controlled intersection is a point where multiple roads cross over. It being controlled means it has signs, traffic lights, and/or road signs to guide drivers. " +
			"A tool to manage who goes first is FIFO, or first in, first out, meaning the driver that stops at the intersection first has the right of way."
	},
		"answer": ["A"],
		"answer_summary": "Blue car should go first as it arrived first at the intersection."
	},
	"3": {
		"prompt": "Which car should go first at this intersection if they both arrived at the same time?",
		"terrain": [[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4, 3, "Car", "E", "\u2191"], "B":[3, 6, "Car", "W", "\u21b0"]},
		"cars_to": {"A": [4, 6, "Car", "E", "A"], "B":[5, 4,  "Car", "S", "B"]},
		"horizontal_lane": {"30": 0, "31": 0, "32": 0, "33": 0, "36": 0, "37": 0, "38": 0, "39": 0},
		"vertical_lane": {"04": 0, "14": 0, "24": 0, "54": 0, "64": 0, "74": 0},
		"hint": {
			"title": "Controlled Intersections: Rightmost side",
			"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
			"video": "learning3.mp4",
			"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=43&end=92",
			"summary": "In the case where multiple cars get to the intersection at the same time, the driver on the rightmost side should go first. If there are four cars in the intersection, whoever slowly advances first should go. "
	},
		"answer": ["A"],
		"answer_summary": "Blue car should go first as it is continuing straight and yellow car must yield since it's turning."
	},
	"4": {
		"prompt": "Which car has the right-of-way if the road on the top is ending?",
		"terrain": 	   [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7 0
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6 1
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #5 2
						[1, 1, 1, 1, 1, 1, 1, 0, 0, 0], #4 3
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3 4
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #2 5
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1 6
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],#0 7
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4, 4, "Car", "E", "\u2191"], "B":[3, 5, "Car", "E", "\u2197"]},
		"cars_to": {"A": [4, 6, "Car", "E", "A"], "B":[4, 7,  "Car", "E", "B"]},
		"horizontal_lane": {"30": 0, "31": 0, "32": 0, "33": 0, "34": 0, "35": 0, "36": 0, "37": 0, "38": 0, "39": 0},
		"hint": {
			"title": "Controlled Intersections: FIFO",
			"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
			"video": "learning2.mp4",
			"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=18&end=43",
			"summary": "A controlled intersection is a point where multiple roads cross over. It being controlled means it has signs, traffic lights, and/or road signs to guide drivers. " +
			"A tool to manage who goes first is FIFO, or first in, first out, meaning the driver that stops at the intersection first has the right of way."
	},
		"answer": ["B"],
		"answer_summary": "Yellow car should go first as it is ahead of the blue car when the lane starts to merge."
	},
	"5": {
		"prompt": "Which way should a car yield if an emergency vehicle (with active sirens) is behind it?",
		"terrain":     [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #7 0
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #6 1
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #5 2
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4 3
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3 4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #2 5
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0], #1 6
						[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]],#0 7
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [4, 4, "Car", "E", "\u2191"], "B":[4, 2, "Ambulance", "E", "\u2191"]},
		"cars_to": {"A": [5, 6, "Car", "E", "A"], "A1":[3, 6,  "Car", "E", "A"]},
		"horizontal_lane": {
			"20": 0, "21": 0, "22": 0, "23": 0, "24": 0, "25": 0, "26": 0, "27": 0, "28": 0, "29": 0,
			"30": 0, "31": 0, "32": 0, "33": 0, "34": 0, "35": 0, "36": 0, "36": 0, "37": 0, "38": 0, "39": 0,
			"40": 0, "41": 0, "42": 0, "43": 0, "44": 0, "45": 0, "46": 0, "47": 0, "48": 0, "49": 0
		},
		"hint": {
			"title": "Emergency Vehicles",
			"image": "https://www.fountainvalley.org/ImageRepository/Document?documentID=10622",
			"video": "learning5.mp4",
			"source": "https://www.youtube.com/embed/8MpfC3mIvhs?start=36&end=83",
			"summary": "In the case of an emergency vehicle passing, it is important to allow them the right of way and give them ample space soon as possible in a safe manner. " +
			"The rule of thumb is to move to the closest lane, moving to the right side if you are in the center lane."
		},
		"answer": ["A"],
		"answer_summary": "Blue car should move towards the right lane as that is the closest lane."
	},
	"6": {
		"prompt": "Which car should go first at this intersection if they all arrived at the same time?",
		"terrain": 		[[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #7
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #6
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #5
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #4
						[1, 1, 1, 1, 1, 1, 1, 1, 1, 1], #3
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #2
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0], #1
						[0, 0, 0, 0, 1, 1, 0, 0, 0, 0]],#0
						#0, 1, 2, 3, 4, 5, 6, 7, 8, 9
		"cars_from": {"A": [2, 4, "Car", "S", "\u2191"], "B":[3, 6, "Car", "W", "\u2191"], "C":[4, 3, "Car", "E", "\u21b0"]},
		"cars_to": {"A": [5,4, "Car", "S", "A"], "B":[3, 3, "Car", "N", "B"], "C":[2, 5,  "Car", "E", "C"]},
		"horizontal_lane": {"30": 0, "31": 0, "32": 0, "33": 0, "36": 0, "37": 0, "38": 0, "39": 0},
		"vertical_lane": {"04": 0, "14": 0, "24": 0, "54": 0, "64": 0, "74": 0},
		"hint": {
			"title": "Controlled Intersections: Rightmost side",
			"image": "https://static.epermittest.com/media/filer_public_thumbnails/filer_public/a7/c7/a7c7623e-b7ba-46b8-a2bd-146572859e97/right-of-way-at-intersections.jpg__1920x0_q100_subsampling-2_upscale.jpg",
			"video": "learning3.mp4",
			"source": "https://www.youtube.com/embed/VWXgqPzADGQ?start=43&end=92",
			"summary": "In the case where multiple cars get to the intersection at the same time, the driver on the rightmost side should go first. If there are four cars in the intersection, whoever slowly advances first should go. "
	},
		"answer": ["C", "A", "B"],
		"answer_summary": "Red car should go first as it's on the rightmost side with no car on its right."
		
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
def quizendpage(idx=None):
	for question in questions:
		if question == idx:
			return render_template('quiz_page.html', questions=questions[question])	
	return render_template('quiz_end.html', questions={})

@app.route('/quiz/<idx>')
def quizpage(idx=None):
	for question in questions:
		if question == idx:
			return render_template('quiz_page.html', questions=questions[question])		
	return render_template('quiz_page.html', questions={})

@app.route('/answers')
def answers():
	return answers
# AJAX FUNCTIONS


if __name__ == '__main__':
   app.run(debug = True)

