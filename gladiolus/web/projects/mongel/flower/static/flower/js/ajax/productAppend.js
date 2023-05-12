function data_click(button) {
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        $.ajax({
            url: '../append/' + button.getAttribute('product-id'),
            method: 'post',
            dataType: "html",
            data: {user_id: 0,
                  csrfmiddlewaretoken: csrf_token},
            success: function(data){
                alert(data);
            }
        });
    })
}