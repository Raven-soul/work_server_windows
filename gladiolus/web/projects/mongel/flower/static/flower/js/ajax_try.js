function data_click() {
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
    
        $.ajax({
            url: '../cookie/',
            method: 'post',
            dataType: "html",
            data: {text: 'Текст',
                  csrfmiddlewaretoken: csrf_token},
            success: function(data){
                alert(data);
            }
        });
    })
}


