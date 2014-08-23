$(document).ready(function () {
	$("#add-friends").click( function() {
		openAddFriendsPopup();
	});

	$("#whiteboard").click( function() {
		closeAddFriendsPopup();
	});

	$("#add-friends-lockin").click( function() {
		$("#friends input").each( function(e) {
			if( e.checked ) {
				dom = "<img src=\"\" width=\"50px\" height=\"50px\" />";
				$("#add-friends").before(dom);	
			}
		});
	});
});

function openAddFriendsPopup() {
	$("#add-friends-popup").css({"display": "block", "z-index": 2});
	$("#whiteboard").css({"display": "block", "z-index": 1});
}

function closeAddFriendsPopup() {
	$("#add-friends-popup").css({"display": "none", "z-index": -1});
	$("#whiteboard").css({"display": "none", "z-index": -1});	
}