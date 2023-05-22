function ajaxSetSityRequest(typeRequest, majorArea, replaceableArea){
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    $.post('../setSity/', {csrfmiddlewaretoken: csrf_token, 'typeRequest': typeRequest}, function(data){
        replaceableArea.remove();
        majorArea.innerHTML = data;
    });
}

function setSity(button){
    alert('ready');
}