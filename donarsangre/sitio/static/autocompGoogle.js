// Working code, need to set up Billing for it to actually function
// HTML needed:
// <script src="https://maps.googleapis.com/maps/api/js?key=AIzaSyBSHD4vrWK98EPYTW8Ziu0alqTvXlpRrto&libraries=places&callback=initAutocomplete" async defer></script>
// <script type="text/javascript" src="{% static "autocompGoogle.js" %}"></script>
// <input type="text" id="autocomplete" placeholder="Enter a place"><br>

let autocomplete;

function initAutocomplete(){
	autocomplete = new google.maps.places.Autocomplete(
		document.getElementById('autocomplete'),
		{
			types: ['establishment'],
			componentRestrictions: {'country': ['AU']},
			fields: ['place_id']
		});
	autocomplete.addListener('place_changed', onPlaceChanged);
}

function onPlaceChanged() {
	var place = autocomplete.getPlace();

	if (!place.geometry) {
		document.getElementById('autocomplete').placeholder = 'Enter a place';
	} else {
		document.getElementById('details').innerHTML = place.name;
	}
}
