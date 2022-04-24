$(document).ready(function(){
	let url = window.location.href
	let currentIdx = url.slice(-1)
	console.log("current id = " + currentIdx)

	if(currentIdx >=2){
		$("#learnPrevious").show()
	}

	else{
		$('#learnNext').css('margin-left', 0)
		$("#learnPrevious").hide()
	}

	if(currentIdx <= 5){
		$("#learnNext").show()
	}

	else{
		$("#learnNext").hide()
	}


	$("#learnPrevious").click(function(){
		console.log("clicked previous")

		if($("#learnPrevious").show()){
			let prevIdx = parseInt(currentIdx) - 1
			let url = "/learn/" + prevIdx
            location.href = url
			console.log("updated: " + prevIdx)
		}

	})

	$("#learnNext").click(function(){
		console.log("clicked next")

		if($("#learnNext").show()){
			if(currentIdx == 5){
				let url = "/quiz"
				location.href = url
			}
			else{
				let nextIdx = parseInt(currentIdx) + 1
				let url = "/learn/" + nextIdx
				location.href = url
			}

			console.log("updated: " + nextIdx)

		}

	})

	$("#startQuizButton").click(function(){
		console.log("start quiz")

		let url = "/quiz/1"
        location.href = url

	})

})