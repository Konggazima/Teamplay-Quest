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
		closeAddFriendsPopup();
	});

	$(".btn-circle").click( function() {
		checked = this.getAtrribute('data-checked');

		if( checked ) {
			$(this).removeClass("glyphicon glyphicon-remove-circle");
			$(this).addClass("glyphicon glyphicon-ok-circle");
		} else {
			$(this).removeClass("glyphicon glyphicon-ok-circle");
			$(this).addClass("glyphicon glyphicon-remove-circle");
		}

		this.setAttribute('data-checked', !checked);
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