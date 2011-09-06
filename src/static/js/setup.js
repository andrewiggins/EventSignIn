$(function() {
    $('#login').hide();
    $('#date').datetimepicker({
        ampm: true,
        dateformat: "{{ dformat }}",
        timeformat: "{{ tformat }}",
        seperator: "{{ sep }}"
    });
    $('#eventForm').submit(function () {
        return validateForm();
    });
    
    $('nav li').click(function() {
        var visible = $('.action:visible');
        var toshow = $($(this).attr('show'));
                        
        if (!visible.is(toshow))
        {
            visible.slideToggle();
            visible.find('input').removeAttr('required');
            
            toshow.slideToggle();
            toshow.find('input').attr('required', 'required');
            
            $('#action').val(toshow.find('fieldset').attr('name'));
        }        
    });
})

function validateForm() { 
    var org = $('#org').val();
    var event = $('#event').val();
    var datetime = $('#date').val();
    var password = $('#password').val();
    var newpassword = $('#newpassword').val();
    var re_newpassword = $('#re_newpassword').val();
    
    if (org == '' || event == '' || datetime == '') {
        showUserMsg('Please fill out all inputs.');
        return false;
    }
    
    var action = $('#action').val();
    if (action == 'create') {
        if (newpassword == '') {
            showUserMsg('Please fill out all inputs.');
            return false;
        } else if (newpassword != re_newpassword) {
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