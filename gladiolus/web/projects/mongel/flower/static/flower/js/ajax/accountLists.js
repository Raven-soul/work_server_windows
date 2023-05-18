function ajaxReplaceRequest(typeRequest, majorArea, replaceableArea){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../accountLists/', {csrfmiddlewaretoken: csrf_token, 'typeRequest': typeRequest}, function(data){
        replaceableArea.remove();
        majorArea.innerHTML = data;
    });
}

function ajaxDeleteRequest(productId, list, row){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../delete/', {csrfmiddlewaretoken: csrf_token, 'productId': productId, 'list': list}, function(data){
        document.getElementById(row.getAttribute('hr-id')).remove();
        row.remove();
    });
}

function ajaxReviewRequest(productId){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../startReview/', {csrfmiddlewaretoken: csrf_token, 'productId': productId}, function(data){
        // window.location.href = data.redirect
        alert(data.redirect + ' ' + window.location.href)
    });
}

function awake(majorTagId, replaceableAreaTagId ){
    majorDataAreaTag = document.getElementById(majorTagId);
    replaceableAreaTag = document.getElementById(replaceableAreaTagId);    
    ajaxReplaceRequest('choosen_short', majorDataAreaTag, replaceableAreaTag);
}

function chooseButton(button, selectPos){
    commonDataTag = document.getElementById(button.getAttribute('common-data-id'));

    buttonIdPrefix = commonDataTag.getAttribute('button-id-prefix');
    numberButtons = commonDataTag.getAttribute('number-buttons');

    for(i = 0; i < numberButtons; i++){
        button = document.getElementById(buttonIdPrefix + i);
        if(i==selectPos){
            button.classList.add('button-select');
        }
        else{
            button.classList.remove('button-select');
        }
        
    }
}

function showSelectedList(button){
    chooseButton(button, 0)
    majorDataAreaTag = document.getElementById(button.getAttribute('data-area-id'));
    replaceableAreaTag = document.getElementById(button.getAttribute('show-content-area-id'));    
    ajaxReplaceRequest('choosen_short', majorDataAreaTag, replaceableAreaTag);
}

function showPurchasedList(button){
    chooseButton(button, 1)
    majorDataAreaTag = document.getElementById(button.getAttribute('data-area-id'));
    replaceableAreaTag = document.getElementById(button.getAttribute('show-content-area-id'));   
    ajaxReplaceRequest('purchased_short', majorDataAreaTag, replaceableAreaTag);
}

function showFavoriteList(button){
    chooseButton(button, 2)
    majorDataAreaTag = document.getElementById(button.getAttribute('data-area-id'));
    replaceableAreaTag = document.getElementById(button.getAttribute('show-content-area-id'));   
    ajaxReplaceRequest('liked_short', majorDataAreaTag, replaceableAreaTag);
}

function productDelete(button){
    productTag = document.getElementById(button.getAttribute('product-id'));
    if(productTag.getAttribute('list-type') == 'purchase'){
        if (confirm("Вы уверены? \nДеньги вернутся вам втечении двух рабочих дней")) {
            ajaxDeleteRequest(productTag.getAttribute('product-id'), productTag.getAttribute('list-type'), productTag);
        }
        else{}
    }
    else {
        ajaxDeleteRequest(productTag.getAttribute('product-id'), productTag.getAttribute('list-type'), productTag);
    }
}

function addReview(button){
    ajaxReviewRequest(button.getAttribute('product-id'));
}