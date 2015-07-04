var map;
var markers = [];
var instituto_seleccionada = 0;
var institutos_temp;

$(function() {
	var mapOptions = {
		zoom: 15,
		center: new google.maps.LatLng(-2.1677561,-79.9169337)
	};
	map = new google.maps.Map(document.getElementById('map-canvas'), mapOptions);

	infowindow = new google.maps.InfoWindow({
		content:'<span id="hook">Hello World!</span>',
		maxWidth: 400
	});

	var poligono = [
	    new google.maps.LatLng(-2.1931734, -79.9409447),
	    new google.maps.LatLng(-2.1652986, -79.9284134),
	    new google.maps.LatLng(-2.2070678, -79.9199591),
	    new google.maps.LatLng(-2.2270942, -79.9294434),
	    new google.maps.LatLng(-2.1931734, -79.9409447)
	  ];

	  // Construct the polygon.
	  bermudaTriangle = new google.maps.Polygon({
	    paths: poligono,
	    strokeColor: '#FF0000',
	    strokeOpacity: 0.8,
	    strokeWeight: 2,
	    fillColor: '#FF0000',
	    fillOpacity: 0.35
	  });

	  bermudaTriangle.setMap(map);

	mostrarIE();
});

function setAllMap(map) {
  for (var i = 0; i < markers.length; i++) {
    markers[i].setMap(map);
  }
}

function clearMarkers() {
  setAllMap(null);
}

function mostrarIE() {
	institutos_temp = institutos;
	mostrarInstitutos();
}

function mostrarWithin() {
	institutos_temp = institutos_within;
	mostrarInstitutos();
}

function mostrarLeft() {
	institutos_temp = institutos_left;
	mostrarInstitutos();
}

function mostrarRight() {
	institutos_temp = institutos_right;
	mostrarInstitutos();
}

function mostrarInstitutos() {
	clearMarkers();

	for (var i in institutos) {
		var instituto = institutos_temp[i];
		var marker = new google.maps.Marker({
			draggable: false,
			raiseOnDrag: false,
			icon: imagetypes[ "I" ],
			shadow: shadow,
			shape: shape,
			map: map,
			title: instituto.nombre,
			position: new google.maps.LatLng( instituto.latitud, instituto.longitud)
		});

		var cadena = "<h3>"+ instituto.nombre+"</h3>" +
			"<table style='width:100%;'>"+
			"<tr><td><strong>C&oacute;digo:</strong></td>"+
			"<td>"+instituto.nombre+"</td></tr>"+
			"</table>";
		bindInfoWindow(marker, map, infowindow, cadena);  
		instituto.marker = marker;
		marker.setMap(map);
		markers.push(marker);
	}
}

function bindInfoWindow(marker, map, infowindow, html) { 
	google.maps.event.addListener(marker, 'click', function() {
		infowindow.setContent(html); 
		infowindow.open(map, marker); 
	});
} 


