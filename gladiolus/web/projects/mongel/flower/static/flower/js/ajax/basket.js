function awake(common_data_id, data) {
    alert(common_data_id);
    // totalPrice(common_data_id);
    // delivery(common_data_id);
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
    totalPrice(document.getElementById(row.getAttribute('common-data-id')));
}

function localPrice(qty, row, result_price){
    count = Number(qty.getAttribute('value'));
    price = Number(row.getAttribute('price').replace(/,/, '.'));
    result_price.innerHTML = Number(count*price);
}

function totalPrice(common){
    row = document.querySelectorAll('.product-row');
    result = 0;
    [].forEach.call(row, el => {
        qty = document.getElementById(el.getAttribute('qty-name') + el.getAttribute('id'));
        price = Number(el.getAttribute('price').replace(/,/, '.'));        
        count = Number(qty.getAttribute('value'));
        result = result + (price*count);
    });

    document.getElementById(common.getAttribute('total-price-id')).innerHTML = result;
}