var map = null;
var marker = null;
var makerGoal = null;
var pos = null;
var distance = 0;
var notified = false;

function initMap() {
	map = new google.maps.Map(document.getElementById('map'), {
		center: {
			lat: 55.866170,
			lng: -4.251004
		},
		zoom: 11
	});

	// Try HTML5 geolocation.
	if (navigator.geolocation) {
		navigator.geolocation.watchPosition(function (position) {

			// Get current location

			pos = {
				lat: position.coords.latitude,
				lng: position.coords.longitude
			};

			// Update current location marker

			if (marker !== null) {
				marker.setPosition(pos);
			} else {
				marker = new google.maps.Marker({
					position: pos,
					map: map,
					title: 'Current Location',
					icon: 'http://maps.google.com/mapfiles/ms/icons/blue-dot.png'
				});
			}

			calculateDistance();
	
			notify();

			// Centre Map
			map.setCenter(pos);
		}, function () {
			handleLocationError(true, infoWindow, map.getCenter());
		});
	} else {
		// Browser doesn't support Geolocation
		handleLocationError(false, infoWindow, map.getCenter());
	}
}

function notify(){
	if (!notified && distance < 0.2){
		notified = true;
		window.alert("You are approaching your stop!");
	}
	return
}

// Error Handling

function handleLocationError(browserHasGeolocation, infoWindow, pos) {
	infoWindow.setPosition(pos);
	infoWindow.setContent(browserHasGeolocation ?
		'Error: The Geolocation service failed.' :
		'Error: Your browser doesn\'t support geolocation.');
}

// Update Goal Marker

function changeGoal(lat, lng) {
	if (makerGoal !== null) {
		var newPosition = {
			lat: parseFloat(lat),
			lng: parseFloat(lng)
		};
		makerGoal.setPosition(newPosition);
	} else {
		makerGoal = new google.maps.Marker({
			position: {
				lat: lat,
				lng: lng
			},
			map: map,
			title: 'Goal',
			icon: 'http://maps.google.com/mapfiles/ms/icons/red-dot.png'
		});
	}
	calculateDistance();
}

// Calculate Distance between current location and destination

function calculateDistance() {
	if (makerGoal !== null) {
		distance = getDistanceFromLatLonInKm(pos.lat, pos.lng, makerGoal.getPosition().lat(), makerGoal.getPosition().lng());
		document.getElementById('text').innerHTML = 'Distance to Destination: ' + parseFloat(Math.round(distance * 100) / 100).toFixed(2) + ' km';
	}
}

// Distance Calculation

function getDistanceFromLatLonInKm(lat1, lon1, lat2, lon2) {
	var R = 6371; // Radius of the earth in km
	var dLat = deg2rad(lat2 - lat1); // deg2rad below
	var dLon = deg2rad(lon2 - lon1);
	var a =
		Math.sin(dLat / 2) * Math.sin(dLat / 2) +
		Math.cos(deg2rad(lat1)) * Math.cos(deg2rad(lat2)) *
		Math.sin(dLon / 2) * Math.sin(dLon / 2);
	var c = 2 * Math.atan2(Math.sqrt(a), Math.sqrt(1 - a));
	var d = R * c; // Distance in km
	return d;
}

function deg2rad(deg) {
	return deg * (Math.PI / 180);
}

