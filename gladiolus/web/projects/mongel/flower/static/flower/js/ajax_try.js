function data_click(user_id) {
    $("document").ready(function() {
        csrf_token = $('input[name="csrfmiddlewaretoken"]').val();
        alert(user_id)
        $.ajax({
            url: '../cookie/',
            method: 'post',
            dataType: "html",
            data: {user_id: user_id,
                  csrfmiddlewaretoken: csrf_token},
            success: function(data){
                alert(data);
            }
        });
    })
}


