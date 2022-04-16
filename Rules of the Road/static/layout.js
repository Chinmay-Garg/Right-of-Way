$(document).ready(function(){
	let link = "/search_results/"

	$("#searchButton").click(function(){
		if(!jQuery.trim($("#searchInput").val())) {
			$("#searchInput").focus()
		} else {
			toSearch = $("#searchInput").val()
	    	window.location.href = link + toSearch
		}
    })

    $("input").keyup(function (key) {
  		if(key.keyCode == 13) {
  			if(!jQuery.trim($("#searchInput").val())) {
				$("#searchInput").focus()
			} else {
				let toSearch = $("#searchInput").val()
				link = link + toSearch
				$("#searchInput").val('')
		    	
		    	window.location.href = link
			}
  		}
  	})

})
