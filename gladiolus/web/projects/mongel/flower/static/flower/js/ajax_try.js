function data_click() {
    alert('work')
}

$("document").ready(function() {
    $.ajax({
        url: 'js_start/',
        method: 'post',
        dataType: 'html',
        data: {text: 'Текст'},
        success: function(data){
        alert(data);
        }
    });
})
