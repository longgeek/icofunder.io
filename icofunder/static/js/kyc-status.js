$(document).ready(function() {
    $("#kyc_form input[name='kyc_status']").bind("input propertychange", function() {
        var kyc_status = $("#kyc_form input[name='kyc_status']")[0].value;
        if (kyc_status.length == 0) {
            $('.modal-button').addClass('modal-button--disabled');
        } else {
            $('.modal-button').removeClass('modal-button--disabled');
        }
    })

    kyc_status_submit = function() {
        regex = ['None', 'true', 'false', 'progress'];
        if ($('.modal-button').hasClass('modal-button--disabled')) { return false; };
        var user_id = $("#kyc_form input[name='kyc_status']").data("user-id");
        var kyc_status = $("#kyc_form input[name='kyc_status']")[0].value;

        if (regex.indexOf(kyc_status) !== -1) {
            $('.modal-button').addClass('modal-button--disabled');

            $.ajax({
                url: "/kyc/set/",
                type: "POST",
                cache: false,
                data: {"user_id": user_id, "kyc_status": kyc_status},
                success : function(result) {
                    $("#modalSuccess").modal("show");
                }
            });
        } else {
            alert('无效的参数，请重新输入。');
        }
    }
});
