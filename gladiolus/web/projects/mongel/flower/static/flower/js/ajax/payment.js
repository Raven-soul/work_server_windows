//
// payment.js
// development of an online flower shop
//
// Created by Artem Kozyrev on 24.05.2023.
//

function ajaxPayRequest(method){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../pay/', {csrfmiddlewaretoken: csrf_token, 'method': method}, function(data){
        alert('Оплата прошла успешно, список товаров добавлен в раздел "Купленные товары" в личном кабинете пользователя')
        window.location.href = data.redirect
    });
}

function pay(button){
    ajaxPayRequest(button.getAttribute('method-pay'));
}