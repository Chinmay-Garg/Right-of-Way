$(document).ready(function(){

    let location = window.location.pathname;
    if (location == "/quiz/end") {
        $('.nav-link').css('display', 'none')
    }
    console.log(location)

})
