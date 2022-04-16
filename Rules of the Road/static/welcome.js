function featureRest(restaurant) {
	let link = "http://127.0.0.1:5000/view/" + restaurant.id

	let featureCode = "<div class='inline'><a href='"
	featureCode = featureCode + link + "'>"
	featureCode = featureCode + "<img src='"
	featureCode = featureCode + restaurant.image
	featureCode = featureCode + "' alt='"
	featureCode = featureCode + restaurant.name
	featureCode = featureCode + " storefront.' class='tinyPic'></a></div>"
	featureCode = featureCode + "<div class='inline'><a href='" + link
	featureCode = featureCode + "'>" + restaurant.name + "</a><br><a href='"
	featureCode = featureCode + link + "'> Rated " + restaurant.stars + " stars.</a></div>"

	return featureCode
}

$(document).ready(function(){
	let code = ""

	code = featureRest(restaurants.loscaf)
	$("#one").append(code)

	code = featureRest(restaurants.peqcol)
	$("#two").append(code)

	code = featureRest(restaurants.elmord)
	$("#three").append(code)
})
