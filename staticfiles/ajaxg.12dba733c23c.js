const form = document.getElementById('red');
form.addEventListener("submit",submitHandler);
function submitHandler(e) {
    var serializedData = $(this).serialize();
    e.preventDefault();
    $.ajax({
        type: 'POST' , 
        data: serializedData  ,
        dataType: 'json',
        success: function (data) {
            if (data.msg === 'Success') {
                alert('We got your message! we will get in touch with you ASAP');
                $("#red").trigger('reset');
      }
    }
 })
}
