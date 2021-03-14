document.getElementById("submit_button").onclick = function(event) {
    params = $('.ip_form').serialize();
    var theUrl = "/location?" + params;
    console.log(theUrl);
    var request = new XMLHttpRequest();
    request.open("PATCH", decodeURIComponent(theUrl), false);
    request.send(null);
    document.getElementById("res").innerHTML = request.responseText;
    console.log(request.response);
    event.preventDefault();
};