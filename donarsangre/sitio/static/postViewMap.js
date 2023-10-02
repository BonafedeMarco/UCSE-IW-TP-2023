//Set up some of our variables.
var map; //Will contain map object.

//Defaults for backup
//var latitude = -31.252606961483437;
//var longitude = -61.49176597595215;

//Function called to initialize / create the map.
//This is called when the page has loaded.
function initMap(latitude = -31.252606961483437, longitude = -61.49176597595215) {

    latitude = parseFloat(latitude.toString().replace(",","."));
    longitude = parseFloat(longitude.toString().replace(",","."));
    console.log(latitude);
    console.log(longitude);
    //The center location of our map.
    var centerOfMap = new google.maps.LatLng(latitude, longitude);

    //Map options.
    var options = {
      center: centerOfMap, //Set center.
      zoom: 16 //The zoom value-61.4882899.
    };

    //Create the map object.
    map = new google.maps.Map(document.getElementById('map'), options);

    //Create marker
    marker = new google.maps.Marker({
	    position: { lat: latitude, lng: longitude },
	    map: map,
	    draggable: false
    });
}

//Load the map when the page has finished loading.
google.maps.event.addDomListener(window, 'load', initMap);
