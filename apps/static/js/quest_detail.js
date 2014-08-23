$('#detail .btn-bath').click(function () {
    $.ajax({
        url: "/owner/checkin",
        dataType: 'JSON',
        data: {
            quest_id : $('.quest-body input').val()
        },
        success: function () {
            $('#detail .btn-bath').hide();
        }
    });
});