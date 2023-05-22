function awake(common_data_id, product_row_name) {
    totalPriceCalculator(common_data_id, product_row_name).then(console.log);
    delivery_calculate(common_data_id);
}

function counterIncrease(button, qty_field_max, common_data_id, product_row_name) {
    factor = 1;
    qty_field = document.getElementById(button.getAttribute('aria-controls'));

    qty_field_previous_value = Number(qty_field.getAttribute('value'));
    qty_field_min = Number(qty_field.getAttribute('min'));

    if((qty_field_previous_value + Number(1*factor)) > qty_field_max) {} 
    else if((qty_field_previous_value + Number(1*factor)) < qty_field_min) {}
    else {
        qty_field.setAttribute('value', Number(qty_field_previous_value + Number(1*factor)));
    }

    // productCostCalculator(button.getAttribute('product-id'), qty_field.getAttribute('value'));
    totalPriceCalculator(common_data_id, product_row_name);
}

function counterDecrease(button, qty_field_max, common_data_id, product_row_name) {
    factor = -1
    qty_field = document.getElementById(button.getAttribute('aria-controls'));

    qty_field_previous_value = Number(qty_field.getAttribute('value'));
    qty_field_min = Number(qty_field.getAttribute('min'));

    if((qty_field_previous_value + Number(1*factor)) > qty_field_max) {} 
    else if((qty_field_previous_value + Number(1*factor)) < qty_field_min) {}
    else {
        qty_field.setAttribute('value', Number(qty_field_previous_value + Number(1*factor)));
    }

    // productCostCalculator(button.getAttribute('product-id'), qty_field.getAttribute('value'));
    totalPriceCalculator(common_data_id, product_row_name);
}

function productCostCalculator(product_row_id, quantity_field_tag_view){
    product_tag = document.getElementById(product_row_id);
    product_price = parseFloat((product_tag.getAttribute('price').replace(",", ".")));
    product_price_tag = document.getElementById(product_tag.getAttribute('priduct-id') + '-price');
    product_price_tag.innerHTML = String(Number(quantity_field_tag_view)*Number(product_price));
}

function totalPriceCalculator(common_data_id, product_row_name) {
    var row = document.querySelectorAll('.product-row');

    [].forEach.call(row, el => {
        alert(el.getAttribute('price'));
    });
}

function deleteRowButton(executing_button_tag, common_data_id, product_row_name) {
    product_row_id = executing_button_tag.getAttribute('product-id');
    document.getElementById(product_row_id).remove();

    totalPriceCalculator(common_data_id, product_row_name);
}

function delivery_calculate(common_data_id) {
    commonDataTag = document.getElementById(common_data_id);

    delivery_tag = document.getElementById(commonDataTag.getAttribute('delivery-price-area'));
    currency_tag = document.getElementById(delivery_tag.getAttribute('currency-area'));

    delivery_cost = Number(delivery_tag.getAttribute('delivery-cost'));

    if (delivery_cost == 0) {
        delivery_tag.innerHTML = 'бесплатно';
        currency_tag.style.display = 'none';
    }
    else {
        delivery_tag.innerHTML = delivery_cost;
    }
}