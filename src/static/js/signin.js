// TODO: when a log is sent through the channel, no picture will be shown

// TODO: write add user code

// TODO: setup channel
// TODO: setup download
// TODO: setup error pages
// TODO: setup auto-delete
// TODO: add recaptcha
// TODO: add setup email

function prependUser(name, email){
    if (name != '' && email != '') {
        var logcontent = name + ' ('+email+') has signed in.';
        var spanhtml = '<span>'+logcontent+'</span>';
        var loghtml = '<div class="signinlog_entry first">'+spanhtml+'</div>';
        
        $('#signinlog div.first').removeClass('first');
        $('#signinlog').prepend(loghtml);
        $('#signinlog div.first').hide().slideDown();
    }
}

function signInUser(data) {
    name = data.name;
    email = data.email;
    
    if (name != '' && email != '') {
        var userTag = getUserTag(name, email)
        if (userTag.length == 0) {
            prependUser(name, email);
            registerUser($('#signinlog div.first'), data);
        } else {
            userTag = userTag.first();
            if (userTag.hasClass('error')) {
                showUserMsg('error', name, email, function () {
                    retryUser(userTag, name, email);
                });
            } else if (userTag.hasClass('loading')) {
                showUserMsg('loading', name, email);
            } else {
                showUserMsg('success', name, email);
            }
        }
    }
}

function getUserTag(name, email) {
    var tags = $('.signinlog_entry');
    var regex = new RegExp('^'+name+' \\('+email+'\\) .*');

    return tags.filter(function() {
        return regex.test($(this).text())
    });
}

function getUserMsg(status, name, email) {
    var msg = name+' ('+email+') ';
    switch (status) {
        case "error":
            msg += 'had an error. Retrying...';
            break;
        case "loading":
            msg += 'is currently saving...';
            break;
        default:
            msg += 'has already successfully logged in.';
    }
    return msg;
}

function showUserMsg(status, name, email, callback) {
    var msg = getUserMsg(status, name, email);
    
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
                $('#msgs').slideUp(callback);
        }, 2000)
    });
}

function retryUser(tag, data) {
    tag.slideUp(function() {
        $(this).remove();
        signInUser(data);
    });
}

function registerUser(tag, data) {    
    $.ajax({
        url: '/signin',
        dataType: 'json',
        data: data,
        beforeSend: function(jqXHR, settings) {
            tag.addClass('loading');
            tag.append('<img src="/img/loading.gif" />');
        },
        success: function(data, textStatus, jqXHR) {
            if (data.status == 'success')
                signInSuccess(tag);
            else
                signInError(tag, data.name, data.email);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            signInError(tag, data.name, data.email);
        },
        complete: function(jqXHR, textStatus) {
            tag.removeClass('loading');
        }
    })
}

function signInSuccess(tag) {
    tag.find('img').attr('src', '/img/tick.png');
}

function signInError(tag, name, email) {
    tag.addClass('error');
    tag.find('img').attr('src', '/img/cross.png');
    errormsg = name + ' (' + email + ') ' + 'has failed. Please try again.'
    tag.find('span').text(errormsg);
}