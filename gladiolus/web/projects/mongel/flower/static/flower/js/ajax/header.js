//
// header.js
// development of an online flower shop
//
// Created by Artem Kozyrev on 22.05.2023.
//

function ajaxSetSityRequest(cityId, showArea, replaceableArea){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../setSity/', {csrfmiddlewaretoken: csrf_token, 'cityId': cityId}, function(data){
        replaceableArea.remove();
        showArea.innerHTML = data;
    });
}

function setSity(button){
    city_id = button.getAttribute('city-id');
    show_area = document.getElementById(button.getAttribute('output-area'));
    replaceable_area = document.getElementById(button.getAttribute('replaceable-area'));
    ajaxSetSityRequest(city_id, show_area, replaceable_area);
}