function iniciarMap(){
    var coord = {lat:19.0016629 ,lng: -98.199963};
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}