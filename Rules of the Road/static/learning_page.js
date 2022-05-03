n_questions = 5
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

	if(currentIdx <= n_questions){
		$("#learnNext").show()
		$('.progress-bar').width(currentIdx*100/n_questions+"%")
		$('div.progress-bar').text(currentIdx+"/"+n_questions);
	}

	else{
		$("#learnNext").hide()
	}

	$("#toSummary").click(function(){
		console.log("to summary clicked")

		location.href = "#summary"
	})

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
			if(currentIdx == n_questions){
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

})