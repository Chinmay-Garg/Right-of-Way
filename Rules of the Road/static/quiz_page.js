let n_questions = 6
let n_correct = 0
$(document).ready(function(){
	let url = window.location.href
	let currentIdx = url.slice(-1)
	console.log("current id = " + currentIdx)

	if(currentIdx >=2){
		$("#testPrevious").show()
	}

	else{
		$("#testPrevious").hide()
	}

	if(currentIdx <= n_questions){
		$("#testNext").show()

		$('.progress-bar').width(currentIdx*100/n_questions+"%")
		$('div.progress-bar').text(currentIdx+"/"+n_questions);
		buildTerrain(question.terrain, question.cars_from, question.cars_to, question.horizontal_lane, question.vertical_lane)
	}

	else{
		$("#testNext").hide()
	}


	$("#testPrevious").click(function(){
		console.log("clicked previous")

		if($("#testPrevious").show()){
			let prevIdx = parseInt(currentIdx) - 1
			let url = "/quiz/" + prevIdx
            location.href = url
			console.log("updated: " + prevIdx)
		}

	})
	

	$("#testNext").click(function(){
		console.log("clicked next")

		if($("#testNext").show()){
			if(currentIdx == n_questions){
				let url = "/quiz/end"
				location.href = url
			}
			else{
				let nextIdx = parseInt(currentIdx) + 1
				let url = "/quiz/" + nextIdx
				location.href = url
			}

			console.log("updated: " + nextIdx)

		}

	})

	if (currentIdx == "d") {
		n_correct = parseInt(sessionStorage.getItem("n_correct"))
		$('#score-div').text("You got " + n_correct + " out of " + n_questions + " correct!")
		sessionStorage.setItem("n_correct",0);

	}

})

function buildTerrain(terrain, cars_from, cars_to, horizontalLane, verticalLane) {
	// console.log(cars_from)
	
	for(var r in terrain) {
		let row = $('<div class="block-row">')
		let i = terrain[r]
		for(var column in i) {
			let j = i[column]
			let div;
			if(j == "0") {
				div = $('<div class="block grass">')
			} else if (j == "1") {
				div = $(`<div data-x="${r}" data-y="${column}" class="block road">`)
				if(horizontalLane != undefined || horizontalLane != null) {
					if((r.toString()+column.toString()) in horizontalLane) {
						div.css('background-image', 'linear-gradient(to right, white 33%, rgba(255,255,255,0) 0%)')
						div.css('background-position', 'bottom')
						div.css('background-size', '2rem 5px')
						div.css('background-repeat', 'repeat-x')
					}
				}

				if(verticalLane != undefined || verticalLane != null) {
					if((r.toString()+column.toString()) in verticalLane) {
						div.css('background-image', 'linear-gradient(white 33%, rgba(255,255,255,0) 0%)')
						div.css('background-position', 'right')
						div.css('background-size', '5px 2rem')
						div.css('background-repeat', 'repeat-y')
					}
				}

				for(let [key, value] of Object.entries(cars_to)) {
					let x = value[0]
					let y = value[1]
					if(x == parseInt(r) && y == parseInt(column)) {
						div.addClass('droppable')
						div.attr('id', key);
						// div.addClass('ui-droppable')
						console.log(div)
						// Insert droppable here
					}
				}
			}
			for(let [key, value] of Object.entries(cars_from)) {
				let x = value[0]
				let y = value[1]
				let vehicle = value[2]
				let dir = value[3]

				if(x == parseInt(r) && y == parseInt(column)) {
					let car = $('<div class="block car">')
					let car_img = $('<img class="w-100" src="/static/car.png">')
					car.attr('id', key)
					if(dir == "N") {
						car.css(
							'transform',
							'rotate(90deg)'
						)
					} else if (dir == "S") {
						car.css(
							'transform',
							'rotate(-90deg)'
						)
					} else if (dir == "E") {
						car.css(
							'transform',
							'rotate(180deg)'
						)
					}
					// let arrow = $('<img class="arrow-image" src="/static/right-traffic-arrow-hi.png">')

					// car.append(arrow)
					car.append(car_img)
					div.append(car)
				}
			}
			row.append(div)
		}
		$('.terrain').append(row)
	}
	$(".car").draggable({
		revert: "invalid",
		stack: ".draggable",
		snap: ".block",
		cursor: "move",
		classes: {
			"ui-draggable": "mouse-hover"
		}
	});
	$('.droppable').droppable({
		classes: {
			"ui-droppable-hover": "ui-state-hover",
			"ui-droppable-active": "ui-state-default",
		  },
		// accept: "#"+key
		drop: function( event, ui ) {
			// Correct answer
			if (question.answer[0] == ui.draggable.attr("id") && ui.draggable.attr("id") == $(this).attr("id")) {
				n_correct = parseInt(sessionStorage.getItem("n_correct"))
				n_correct = n_correct + 1
				sessionStorage.setItem("n_correct",n_correct);
				console.log("correct: " + n_correct)

				$('div.quiz-feedback').text("Correct");
				$('div.quiz-feedback').addClass('success');
			} else {
				// Incorrect answer
				$('div.quiz-feedback').text("Incorrect");
				$('div.quiz-feedback').addClass('warning');
			}
			$(".car").draggable({ 
				disabled: true,
				classes: {
					"ui-draggable": ""
				} });

			document.getElementById('testNext').disabled = false;
		  }
	})
	
}