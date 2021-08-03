const like_btn_id = "#like-btn"
$(like_btn_id).click(function () {


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


    let post_id = $(like_btn_id).attr('data-id')
    let like_btn_text = $(like_btn_id).text()

    let url = '';
    let btn_text = '';
    let btn_class = '';
    if (like_btn_text === 'Like') {
        url = '/activity/like/'
        btn_text = 'Unlike'
        btn_class = 'btn btn-warning'
    } else {
        url = '/activity/unlike/'
        btn_text = 'Like'
        btn_class = 'btn btn-primary'
    }


    $.ajax({
        url: url,
        method: "POST",
        data: {
            'post_id': post_id,
        },
        success: function (data) {
            if (data['status'] === 'ok') {
                $(like_btn_id).text(btn_text)
                $(like_btn_id).attr({'class': btn_class})

                $("#like-count").text(data['like_count'])
            }
        }
    });
});