function fblogin() {
    var name;
    FB.api('/me', function (response) {
        name = response.name;
        if (name != undefined) {
            alert(name);
        }
    });
}


$(document).ready(function () {
    $('#facebook-btn').click(function () {
        FB.login(function (response) {
            fblogin();
        });
    });
});