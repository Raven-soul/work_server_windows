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
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '../append/',
            method: 'post',
            dataType: "html",
            data: { csrfmiddlewaretoken: csrf_token,
                    'user_id': productId,
                    'typeRequest': typeRequest,
                    'isRedirect': isRedirect
                    },
            success: function(data){
                alert('ready');
            }
        });
    })
}

function addToSelectedList(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    alert('productID' + productId)
    ajaxRequest(productId, 'addToSelectList');
}

function addToSelectedListRedirect(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    alert('productID' + productId)
    ajaxRequest(productId, 'addToSelectList');
}

function addToFavoriteList(button){
    id = button.getAttribute('product-data-area');
    productId = document.getElementById(id).getAttribute('product-id');
    alert('productID' + productId)
    ajaxRequest(productId, 'addToFavoriteList');
}