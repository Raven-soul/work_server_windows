function awake(common_id, item_name) {
    totalPriceCalculator(common_id, item_name);
    delivery_calculate(common_id);
}

function counterIncrease(tagButton, maxValue, factor, common_id, item_name) {
    id = tagButton.getAttribute('aria-controls');
    tagIncrease = document.getElementById(id);

    tagIncreasePreviousValue = Number(tagIncrease.getAttribute('value'));
    minValue = Number(tagIncrease.getAttribute('min'));

    if((tagIncreasePreviousValue + Number(1*factor)) > maxValue) {} 
    else if((tagIncreasePreviousValue + Number(1*factor)) < minValue) {}
    else {
        tagIncrease.setAttribute('value', Number(tagIncreasePreviousValue + Number(1*factor)));
    }

    productCostCalculator(tagButton.getAttribute('product-id'), tagIncrease.getAttribute('value'));
    totalPriceCalculator(common_id, item_name);
}

function productCostCalculator(RowId, number){
    tagProduct = document.getElementById(RowId);
    price = Number(tagProduct.getAttribute('price'));
    priceTag = document.getElementById(tagProduct.getAttribute('priduct-id') + '-price');
    priceTag.innerHTML = String(Number(number)*Number(price));
}

function deleteRowButton(tagButton, common_id, item_name) {
    id = tagButton.getAttribute('product-id');
    document.getElementById(id).remove();

    totalPriceCalculator(common_id, item_name);
}

function totalPriceCalculator(common_id, item_name) {
    commonDataTag = document.getElementById(common_id);

    total_previous_tag = document.getElementById(commonDataTag.getAttribute('previous-price-area'));
    total_delivery_tag = document.getElementById(commonDataTag.getAttribute('delivery-price-area'));
    total_price_tag = document.getElementById(commonDataTag.getAttribute('total-price-area'));

    max_product_rows_number = Number(commonDataTag.getAttribute('product-max-rows'));
    total_delivery_price_data = Number(total_delivery_tag.getAttribute('delivery-cost'));

    total_price_data = 0;

    for (let i = 1; i <= max_product_rows_number; i++) { 
        try {
            priduct_row = document.getElementById(String(item_name + String(i)));
        
            product_db_id = priduct_row.getAttribute('priduct-id');
            product_price = Number(priduct_row.getAttribute('price'));

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

function delivery_calculate(common_id) {
    commonDataTag = document.getElementById(common_id);

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