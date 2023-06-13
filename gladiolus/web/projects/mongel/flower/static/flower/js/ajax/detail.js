//
// detail.js
// development of an online flower shop
//
// Created by Artem Kozyrev on 19.04.2023.
//

function collapsElement(elem){
    id = elem.getAttribute('aria-controls');
    
    if (elem.getAttribute('aria-expanded') == 'true'){
        document.getElementById(id).style.display = 'none';
        elem.setAttribute('aria-expanded', false);
    } else {
        document.getElementById(id).style.display = '';
        elem.setAttribute('aria-expanded', true);
    }
}

function ajaxRequest(productId, typeRequest, isRedirect = false){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../append/', {
        csrfmiddlewaretoken: csrf_token, 
        'user_id': productId,
        'typeRequest': typeRequest,
        'isRedirect': isRedirect}, 
        function(data){
            if (data.isRedirect){
                window.location.href = data.redirect
                }
    });
}

function addToSelectedList(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    ajaxRequest(productId, 'addToSelectList');
}

function addToSelectedListRedirect(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    ajaxRequest(productId, 'addToSelectList', true);
}

function addToFavoriteList(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    ajaxRequest(productId, 'addToFavoriteList');
}