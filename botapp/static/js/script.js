// Pure javascript code that initializes the map
function initMap(lat=16.2333, lng=-61.5167) {
  var newPos = document.getElementById('query--form')
  var center = { lat: lat, lng: lng };
  const map = new google.maps.Map(document.getElementById("map"), {
    center: center,
    zoom: 13,
  });
  // The marker, positioned at Pointe-à-Pitre
  var marker = new google.maps.Marker({
    position: center,
    map: map,
  });

};

// Using jQuery to get value from the form and send it to my python code
$("#query--form").submit(function(event) {
  var $map = map
  // Stop form from submitting normally
  event.preventDefault();
 
  // Get some values from elements on the page:
  var $form = $(this),
    term = $form.find("input[name='question']").val(),
    url = $form.attr("action");
 
  // Send the data using post
  var posting = $.post(url, {question: term});
 
  // Put the results in a element
  posting.done(function(data) {
    var text = data.query;
    var address = data.label[0];
    var lat = data.label[1].lat;
    var lng = data.label[1].lng;
    initMap(lat,lng);
    $(".result").append($(".picture_papy"));
    $("#papy").fadeOut(600).fadeIn(600);
    $(".result").append("<h1>Voici l'adresse que tu cherchais : </h1>", address);  
    $(".result").append("<h1>Est-ce que tu savais que ...</h1>", text);
    $(".result").append($("<br><a class='link'>Pour plus d'informations</a><br>"));
    $(".link").attr({href:'https://fr.wikipedia.org/wiki/' + term, target: '_blank'});

  });
});