function validateForm() {
    var action = $('#action').val();
    if (action == 'create') {
        if ($('#newpassword').val() != $('#re_newpassword').val()) {
            showUserMsg('Passwords do not match.');
            return false;
        }
    } else if (action != 'login') {
        showUserMsg('Server Error. Please refresh the page.');
        return false;
    }
    
    return true;
}

function showUserMsg(msg) {
    $('#msgs').addClass('changing')
    $('#msgs').slideUp(function () {
        var msgcount = $('#msgs').children().length + 1;
        var msgid = 'msg' + msgcount;
        var newmsg = $('<div>').attr('id', msgid).addClass(status).text(msg);
        
        $('#msgs').children().hide();
        $('#msgs').prepend(newmsg).slideDown();
        $('#msgs').removeClass('changing');
        
        setTimeout(function() {
            var first_msgid = $('#msgs').children().first().attr('id');
            var new_msgid = newmsg.attr('id');
            var idmatch = (first_msgid == new_msgid);
            var ischanging = $('#msgs').hasClass('changing');
            
            if (!ischanging && idmatch)
                $('#msgs').slideUp();
        }, 2000)
    });
}