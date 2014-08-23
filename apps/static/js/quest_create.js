$(document).ready(function () {
    $("#add-friends").click( function() {
        openAddFriendsPopup();
    });

    $("#whiteboard").click( function() {
        closeAddFriendsPopup();
    });

    $("#add-friends-lockin").click( function() {
        $(".picked").each( function() {
            $(this).remove();
        });
        $(".btn-circle").each( function() {
            if( this.getAttribute("data-checked") ) {
                dom = $(this).next().clone();
                $(dom).css({"display": "inline", "margin": "20px"});
                $(dom).addClass("picked");
                $("#add-friends").after( dom );
            }
        });
        closeAddFriendsPopup();
    });

    $(".btn-circle").each( function() {
        $(this).click( function() {
            checked = this.getAttribute("data-checked");

            if( checked ) {
                $(this).removeClass("no");
                $(this).addClass("ok");
            } else {
                $(this).removeClass("ok");
                $(this).addClass("no");
            }

            this.setAttribute("data-checked", !checked + "");
        });
    });

    $(function(){
        $('*[name=date_expired]').datetimepicker({
            step:30,
            format:'Y/m/d/H/i',
            minDate:'-1970/01/1',
            maxDate:'+1970/03/1',
            inline:true
        });
    });

    $("#datetimepicker").css({"display": "none"});

    $("#place").click( function() {
        $("#datetimepicker").css({"display": "block"});
    });
});

function openAddFriendsPopup() {
    $(document).css({"z-index": -1});
    $("#add-friends-popup").css({"display": "block", "z-index": 1});
    $("#whiteboard").css({"display": "block", "z-index": 0});
}

function closeAddFriendsPopup() {
    $(document).css({"z-index": 0});
    $("#add-friends-popup").css({"display": "none", "z-index": -1});
    $("#whiteboard").css({"display": "none", "z-index": -1});    
}