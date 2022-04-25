
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

	if(currentIdx <= 5){
		$("#testNext").show()
		buildTerrain(question.terrain, question.cars_from, question.cars_to)
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
			if(currentIdx == 5){
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

})

function buildTerrain(terrain, cars_from, cars_to) {
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
				for(let [key, value] of Object.entries(cars_to)) {
					let x = value[0]
					let y = value[1]
					if(x == parseInt(r) && y == parseInt(column)) {
						div.addClass('droppable')
						// div.addClass('ui-droppable')
						console.log(div)
						// Insert droppable here
					}
				}
			}
			for(let [key, value] of Object.entries(cars_from)) {
				let x = value[0]
				let y = value[1]
				if(x == parseInt(r) && y == parseInt(column)) {
					let car = $('<div class="block car">')
					car.attr('id', key)
					let arrow = $('<img class="arrow-image" src="/static/right-traffic-arrow-hi.png">')
					car.append(arrow)
					div.append(car)
				}
			}
			row.append(div)
		}
		$('.terrain').append(row)
	}
	$('.droppable').droppable({
		classes: {
			"ui-droppable-hover": "ui-state-hover",
			"ui-droppable-active": "ui-state-default"
		  },
		// accept: "#"+key
		drop: function( event, ui ) {
			// $( this )
			console.log($( this ))
		  }
	})
	$(".car").draggable({
		revert: "invalid",
		stack: ".draggable",
		snap: ".block"
	});
}