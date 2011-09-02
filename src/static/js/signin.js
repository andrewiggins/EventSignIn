var imghtml = '<img src="/img/loading.gif" />';

function prependUser(name, email)
{
    var logcontent = name + ' ('+email+') has signed in.';
    var spanhtml = '<span>'+logcontent+'</span>';
    
    var loghtml = '<div class="listentry first">'+spanhtml+'</div>';

    if (name != '' || email != '')
    {
        $('#log div.first').removeClass('first');
        
        $('#log').prepend(loghtml);
        $('#log div.first').hide().slideDown();
        
        signinUser($('#log div.first'), name, email);
    }
}

function signinUser(tag, name, email) 
{   
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