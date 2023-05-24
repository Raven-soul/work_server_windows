function ajaxGetSityRequest(showArea){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../getSity/', {csrfmiddlewaretoken: csrf_token}, function(data){
        showArea.innerHTML = data.cityCurent;
    });
}

function ajaxDeleteRequest(productId, list, row){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../delete/', {csrfmiddlewaretoken: csrf_token, 'productId': productId, 'list': list}, function(data){
        row.remove();
    });
}

function ajaxConfirmRequest(productList){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../basketConfirm/', {
        csrfmiddlewaretoken: csrf_token, 
        'selected_products': JSON.stringify(productList)
    }, function(data){
        window.location.href = data.redirect;
    });
}

function awake(common_data_id) {
    totalPrice(common_data_id);
    delivery_compute(common_data_id);
    checkCity(document.getElementById(document.getElementById(common_data_id).getAttribute('city-button-id')));
}

function counterIncrease(button, qty_max){
    factor = 1;
    local_compute(button, qty_max, factor);
}

function counterDecrease(button, qty_max){
    factor = -1;
    local_compute(button, qty_max, factor);
}

function local_compute(button, qty_max, factor){
    row = document.getElementById(button.getAttribute('product-id'));
    qty = document.getElementById(row.getAttribute('qty-name') + button.getAttribute('product-id'));
    result_price = document.getElementById(row.getAttribute('product-price-name') + button.getAttribute('product-id'));

    qty__previous = Number(qty.getAttribute('value'));
    qty_min = Number(qty.getAttribute('min'));

    if((qty__previous + Number(1*factor)) > qty_max) {} 
    else if((qty__previous + Number(1*factor)) < qty_min) {}
    else {
        qty.setAttribute('value', Number(qty__previous + Number(1*factor)));
    }

    localPrice(qty, row, result_price);
    totalPrice(row.getAttribute('common-data-id'));
}

function localPrice(qty, row, result_price){
    count = Number(qty.getAttribute('value'));
    price = Number(row.getAttribute('price').replace(/,/, '.'));
    result_price.innerHTML = Number(count*price);
}

function totalPrice(common){
    rows = document.querySelectorAll('.product-row');
    result = 0;
    [].forEach.call(rows, el => {
        qty = document.getElementById(el.getAttribute('qty-name') + el.getAttribute('id'));
        price = Number(el.getAttribute('price').replace(/,/, '.'));        
        count = Number(qty.getAttribute('value'));
        result = result + (price*count);
    });
    document.getElementById(document.getElementById(common).getAttribute('previous-price-area')).innerHTML = result;
    delivery_compute(common);
    delivery_price = Number(document.getElementById(document.getElementById(common).getAttribute('delivery-price-area')).getAttribute('delivery-cost'));
    document.getElementById(document.getElementById(common).getAttribute('total-price-id')).innerHTML = delivery_price + result;
}

function delivery_compute(common_data_id) {
    common = document.getElementById(common_data_id);

    delivery = document.getElementById(common.getAttribute('delivery-price-area'));
    currency = document.getElementById(delivery.getAttribute('currency-area'));

    delivery_price = Number(delivery.getAttribute('delivery-cost'));

    if (delivery_price == 0) {
        delivery.innerHTML = 'бесплатно';
        currency.style.display = 'none';
    }
    else {
        delivery.innerHTML = delivery_price;
    }
}

function checkCity(button){
    ajaxGetSityRequest(document.getElementById(button.getAttribute('city-area-id')));
}

function deleteRow(button){
    list = 'select';
    productId = button.getAttribute('product-id');
    row = document.getElementById(productId);
    
    ajaxDeleteRequest(productId, list, row);
}

function orderConfirm(){
    rows = document.querySelectorAll('.product-row');
    result = [];
    [].forEach.call(rows, el => {
        qty = document.getElementById(el.getAttribute('qty-name') + el.getAttribute('id'));      
        count = Number(qty.getAttribute('value'));
        result.push({
            'product_id': el.getAttribute('id'),
            'count': count
        });
    });
    ajaxConfirmRequest(result);
}