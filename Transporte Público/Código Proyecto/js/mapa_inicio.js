//Funcion que permite inicializa un mapa y poder visualizarlo
function iniciarMap(){
    //señala las coordenadas donde iniciara el mapa
    var coord = {lat:19.0016629 ,lng: -98.199963};
    //creacion de un elemento de mapa con las coordenadas y el zoom que deseemos tener
    //al momento de visualizarlo
    var map = new google.maps.Map(document.getElementById('map'),{
        zoom: 15,
        center: coord
    });
    //Agrega un marcador en las coordenadas dadas y en el mapa usado
    var marker = new google.maps.Marker({
        position: coord,
        map: map
    });
}