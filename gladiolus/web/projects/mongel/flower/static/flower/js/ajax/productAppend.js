//
// productAppend.js
// development of an online flower shop
//
// Created by Artem Kozyrev on 12.05.2023.
//

function data_click(button) {
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '../append/',
            method: 'post',
            dataType: "html",
            data: {'user_id': button.getAttribute('product-id'),
                    csrfmiddlewaretoken: csrf_token},
            success: function(data){
                alert(data);
            }
        });
    })
}