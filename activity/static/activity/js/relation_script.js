const following_btn_id = "#following-btn"
$(following_btn_id).click(function () {


    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    const csrftoken = getCookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function (xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });


    let user_id = $(following_btn_id).attr('data-id')
    let follow_btn_text = $(following_btn_id).text()

    let url = '';
    let btn_text = '';
    let btn_class = '';
    if (follow_btn_text === 'Follow') {
        url = '/activity/follow/'
        btn_text = 'Unfollow'
        btn_class = 'btn btn-warning'
    } else {
        url = '/activity/unfollow/'
        btn_text = 'Follow'
        btn_class = 'btn btn-primary'
    }


    $.ajax({
        url: url,
        method: "POST",
        data: {
            'user_id': user_id,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $(following_btn_id).text(btn_text)
                $(following_btn_id).attr({'class': btn_class})
            }
        }
    });
});