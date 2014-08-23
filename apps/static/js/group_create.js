$(document).ready(function () {
    $("#add-friends").click( function() {
        openAddFriendsPopup();
    });

    $("#whiteboard").click( function() {
        closeAddFriendsPopup();
    });

    $("#add-friends-lockin").click( function() {
        $(".btn-circle").each( function(k,v) {
            if( v.checked ) {;
                dom = $(this).next().clone();
                $(dom).css({"display": "inline", "margin": "20px"});
                $("#add-friends").before( dom );
            }
        });
        closeAddFriendsPopup();
    });

    $(".btn-circle").each( function() {
        $(this).click( function() {
            checked = this.getAttribute('data-checked');

            if( checked ) {
                $(this).removeClass("no");
                $(this).addClass("ok");
            } else {
                $(this).removeClass("ok");
                $(this).addClass("no");
            }

            this.setAttribute('data-checked', !checked);
        });
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