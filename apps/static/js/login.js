function fblogin() {
    FB.api('/me', function (response) {
        var name = response.name;
        var fb_id = response.id;
        var email = response.email;

        FB.api('/me/picture?width=100&height=100', function (response) {
            var img_url = response.data.url;
            $.ajax({

                url: "/login",
                data: {
                    name: name,
                    fb_id: fb_id,
                    email: email,
                    img_url : img_url,
                    timezone_offset : new Date().getTimezoneOffset()
                },
                dataType: 'JSON',
                success: function (data) {
                    location.href = '/group';
                }
            });
        });
    });
}




$(document).ready(function () {
    $('#facebook-btn').click(function () {
        FB.login(function (response) {

            if(response.status == 'connected'){
                fblogin();
            }

        },{scope: 'email'});
    });
});
