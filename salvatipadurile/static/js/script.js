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

var camioane = JSON.parse(data);
// alert(camioane['truck1']['latitudine']);

var truck1 = L.marker([camioane['truck1']['latitudine'], camioane['truck1']['longitudine']])
.addTo(map)
  .bindPopup(
    "<b>" + camioane['truck1']['nr_matriculare'] +"</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup();

var truck2 = L.marker([camioane['truck2']['latitudine'], camioane['truck2']['longitudine']])
.addTo(map)
  .bindPopup(
    "<b>" + camioane['truck2']['nr_matriculare'] +"</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup();

var truck3 = L.marker([camioane['truck3']['latitudine'], camioane['truck3']['longitudine']])
.addTo(map)
  .bindPopup(
    "<b>" + camioane['truck3']['nr_matriculare'] +"</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup();  

var truck4 = L.marker([camioane['truck4']['latitudine'], camioane['truck4']['longitudine']])
.addTo(map)
  .bindPopup(
    "<b>" + camioane['truck4']['nr_matriculare'] +"</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup();

var truck5 = L.marker([camioane['truck5']['latitudine'], camioane['truck5']['longitudine']])
.addTo(map)
  .bindPopup(
    "<b>" + camioane['truck5']['nr_matriculare'] +"</b><br/>camion cu rasinoase <br/> greutate declarata: 5t <br/> nu se poate masura"
  )
  .openPopup(); 

function onMapClick(e) {
  popup
    .setLatLng(e.latlng)
    .setContent("Ai apasat pe " + e.latlng.toString())
    .openOn(map);
}

map.on("click", onMapClick);