
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