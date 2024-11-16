// Initialize the map
var map = L.map('map').setView([40, -110], 4);

// Add OpenStreetMap tile layer
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

var wmsLayer;

// Function to load GeoServer layer
function loadGeoServerLayer() {
    if (!wmsLayer) {
        wmsLayer = L.tileLayer.wms('http://localhost:8080/geoserver/wms', {
            layers: 'us_states:us_states',
            format: 'image/png',
            transparent: true
        }).addTo(map);
    }
}

// Function to remove GeoServer layer
function removeGeoServerLayer() {
    if (wmsLayer) {
        // console.log('Removing layer');
        map.removeLayer(wmsLayer);
        wmsLayer = null;
    }
}

var markers = []; // Array to hold all markers

// Function to load city points from backend
function loadCityPoints() {
    fetch('http://localhost:8000/cities')
        .then(response => response.json())
        .then(data => {
            // console.log('City points:', data);
            data.forEach(city => {
                var marker = L.marker([city.Latitude, city.Longitude])
                    // .bindPopup(`<b>${city.name}</b><br>Population: ${city.population}`)
                    .addTo(map);
                markers.push(marker); // Add marker to the array
                marker.on('click', function () {
                    document.getElementById('info-content').innerHTML = `
                                    <h2>${city.City}</h2>
                                    <p>State: ${city.State}</p>
                                    <p>Latitude: ${city.Latitude}</p>
                                    <p>Longitude: ${city.Longitude}</p>
                                    <p>Population estimate 2022: ${city.Population_estimate_2022}</p>
                                    <p>Population 2020: ${city.Population_2020}</p>
                                    <p>Change population: ${city.Change_population}</p>
                                    <p>Land area: ${city.Land_area}</p>
                                    <p>Population density 2020: ${city.Population_density_2020}</p>
                                `;
                });
            });
        })
        .catch(error => console.error('Error loading city points:', error));
}

// Function to clear all markers
function clearMarkers() {
    markers.forEach(marker => {
        map.removeLayer(marker);
    });
    markers = []; // Clear the markers array
}

// Load GeoServer layer and city points
// loadGeoServerLayer();
// loadCityPoints();