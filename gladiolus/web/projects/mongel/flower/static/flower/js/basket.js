function awake(common_data_id, product_row_name) {
    totalPriceCalculator(common_data_id, product_row_name).then(console.log);
    delivery_calculate(common_data_id);
}

function counterIncrease(executing_button_tag, quantity_field_maxValue, factor, common_data_id, product_row_name) {
    quantity_field_id = executing_button_tag.getAttribute('aria-controls');
    quantity_field_tag = document.getElementById(quantity_field_id);

    quantity_field_tag_previous_value = Number(quantity_field_tag.getAttribute('value'));
    quantity_field_minValue = Number(quantity_field_tag.getAttribute('min'));

    if((quantity_field_tag_previous_value + Number(1*factor)) > quantity_field_maxValue) {} 
    else if((quantity_field_tag_previous_value + Number(1*factor)) < quantity_field_minValue) {}
    else {
        quantity_field_tag.setAttribute('value', Number(quantity_field_tag_previous_value + Number(1*factor)));
    }

    productCostCalculator(executing_button_tag.getAttribute('product-id'), quantity_field_tag.getAttribute('value'));
    totalPriceCalculator(common_data_id, product_row_name);
}

function productCostCalculator(product_row_id, quantity_field_tag_view){
    product_tag = document.getElementById(product_row_id);
    product_price = parseFloat((product_tag.getAttribute('price').replace(",", ".")));
    product_price_tag = document.getElementById(product_tag.getAttribute('priduct-id') + '-price');
    product_price_tag.innerHTML = String(Number(quantity_field_tag_view)*Number(product_price));
}

function deleteRowButton(executing_button_tag, common_data_id, product_row_name) {
    product_row_id = executing_button_tag.getAttribute('product-id');
    document.getElementById(product_row_id).remove();

    totalPriceCalculator(common_data_id, product_row_name);
}

function totalPriceCalculator(common_data_id, product_row_name) {
    commonDataTag = document.getElementById(common_data_id);
    total_previous_tag = document.getElementById(commonDataTag.getAttribute('previous-price-area'));
    
    total_delivery_tag = document.getElementById(commonDataTag.getAttribute('delivery-price-area'));
    total_price_tag = document.getElementById(commonDataTag.getAttribute('total-price-area'));

    max_product_rows_number = Number(commonDataTag.getAttribute('product-max-rows'));
    total_delivery_price_data = Number(total_delivery_tag.getAttribute('delivery-cost'));

    total_price_data = 0;

    for (let i = 1; i <= max_product_rows_number; i++) { 
        try {
            priduct_row = document.getElementById(String(product_row_name + String(i)));
            product_db_id = priduct_row.getAttribute('priduct-id');
            product_price = parseFloat((priduct_row.getAttribute('price').replace(",", ".")));
            product_number = Number(document.getElementById(product_db_id + '-qty-container').getAttribute('value'));
            total_price_data = total_price_data + (product_number * product_price);
        } catch (err) {}        
    }

    total_previous_tag.setAttribute('value', total_price_data);
    total_previous_tag.innerHTML = total_price_data;

    total_price_data = total_price_data + total_delivery_price_data;

    total_price_tag.setAttribute('value', total_price_data);
    total_price_tag.innerHTML = total_price_data;
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

function coocieStart() {
    document.cookie = "user=John; path=/; expires=Tue, 19 Jan 2038 03:14:07 GMT";
    alert(document.cookie);
}