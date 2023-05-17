function ajaxRequest(typeRequest, majorArea, replaceableArea){
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '../accountLists/',
            method: 'post',
            dataType: "html",
            data: { csrfmiddlewaretoken: csrf_token,
                    'typeRequest': typeRequest
                    },
            success: function(data){
                replaceableArea.remove();
                majorArea.innerHTML = data;
            }
        });
    })
}

function awake(majorTagId, replaceableAreaTagId ){
    majorDataAreaTag = document.getElementById(majorTagId);
    replaceableAreaTag = document.getElementById(replaceableAreaTagId);    
    ajaxRequest('choosen_short', majorDataAreaTag, replaceableAreaTag);
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
    ajaxRequest('choosen_short', majorDataAreaTag, replaceableAreaTag);
}

function showPurchasedList(button){
    chooseButton(button, 1)
    majorDataAreaTag = document.getElementById(button.getAttribute('data-area-id'));
    replaceableAreaTag = document.getElementById(button.getAttribute('show-content-area-id'));   
    ajaxRequest('purchased_short', majorDataAreaTag, replaceableAreaTag);
}

function showFavoriteList(button){
    chooseButton(button, 2)
    majorDataAreaTag = document.getElementById(button.getAttribute('data-area-id'));
    replaceableAreaTag = document.getElementById(button.getAttribute('show-content-area-id'));   
    ajaxRequest('liked_short', majorDataAreaTag, replaceableAreaTag);
}

function selectRowDelete(button){
    id = button.getAttribute('product-id');
    alert(id)
}