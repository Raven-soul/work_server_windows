function data_click() {
    alert('work')
}

$("document").ready(function() {
    csrf_token = $('input[name="csrfmiddlewaretoken"]').val();

    $.ajax({
        url: 'js_start/',
        method: 'post',
        dataType: "json",
        data: {text: 'Текст',
              csrfmiddlewaretoken: csrf_token},
        success: function(data){
            alert(data.foo);
        }
    });
})
