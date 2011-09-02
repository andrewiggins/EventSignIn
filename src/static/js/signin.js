var imghtml = '<img src="/img/loading.gif" />';

function prependUser(name, email){
    var logcontent = name + ' ('+email+') has signed in.';
    var spanhtml = '<span>'+logcontent+'</span>';
    
    var loghtml = '<div class="signinlog_entry first">'+spanhtml+'</div>';

    if (name != '' || email != '') {
        if (!userexists(name, email)) {
            $('#signinlog div.first').removeClass('first');
            
            $('#signinlog').prepend(loghtml);
            $('#signinlog div.first').hide().slideDown();
            
            signinUser($('#signinlog div.first'), name, email);
        }
    }
}

function userexists(name, email) {
    var tags = $('.signinlog_entry');
    var namefilter = "div:contains('"+name+" ')"
    var emailfilter = "div:contains('("+email+")')";
    
    if (name != '')
        tags = tags.filter(namefilter);
    
    if (email != '')
        tags = tags.filter(emailfilter);
    
    return tags.length != 0;
    
}

function signinUser(tag, name, email) {   
    $.ajax({
        url: '/signin',
        dataType: 'json',
        data: {'name': name, 'email': email},
        beforeSend: function(jqXHR, settings) {
            tag.addClass('loading');
            tag.append(imghtml);
        },
        success: function(data, textStatus, jqXHR) {
            if (data.status == 'success')
                signInSuccess(tag);
            else
                signInError(tag, name, email);
        },
        error: function(jqXHR, textStatus, errorThrown) {
            signInError(tag, name, email);
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