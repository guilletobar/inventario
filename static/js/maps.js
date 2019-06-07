/*
 * Simple Google Maps Route API example for finding the shortest route between a number
 * of interesting places and a current position. Please keep disclaimer with code if
 * you use it so people can find updates.
 * Coded by Jason Mayes 2014. http://www.jasonmayes.com
 * Latest version available at: https://codepen.io/jasonmayes/pen/DupCH
 */

var map;
function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: {lat: -33.619577, lng: -70.71203980000001},
        zoom: 16

    });
     var marker = new google.maps.Marker({
          position: {lat: -33.619577, lng: -70.71203980000001},
          map: map,
	  title: 'genoma'
        });
      }
