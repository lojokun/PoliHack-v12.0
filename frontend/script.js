var map = L.map("map").setView([46.103498, 25.210392], 7.4);

var tiles = L.tileLayer(
  "https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw",
  {
    maxZoom: 18,
    attribution:
      'Map data &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, ' +
      'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
    id: "mapbox/streets-v11",
    tileSize: 512,
    zoomOffset: -1,
  }
).addTo(map);

var marker = L.marker([46.103498, 25.210392])
  .addTo(map)
  .bindPopup(
    "<b>SV 25 SSR</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> greutate masurata: 9t"
  )
  .openPopup();
  
var marker2 = L.marker([46.2, 25.210392])
  .addTo(map)
  .bindPopup(
    "<b>AB 01 HOT</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup();

var popup = L.popup()
  .setLatLng([46.783437, 23.608901])
  .setContent("aici suntem noi")
  .openOn(map);

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("Ai apasat pe " + e.latlng.toString())
    .openOn(map);
}

map.on("click", onMapClick);
