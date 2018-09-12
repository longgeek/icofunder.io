$(document).ready(function() {
    ico_url_jump = function(url) {
        window.location.href = window.location.protocol + "//" + window.location.host + url;
    }


    $(".user-dropdown").mouseenter(function(e) {
        e.stopPropagation();
        $.ajax({
            url: "/accounts/user/extra/",
            type: "GET",
            cache: false,
            success : function(result) {
                if (result === "None") {
                    $(".kyc-status b").html("未进行 KYC 认证");
                } else if (result === "progress") {
                    $(".kyc-status b").html("已提交 KYC 信息，正在审核中");
                } else {
                    $(".kyc-status b").html("恭喜，您已通过 KYC 认证");
                }
            }
        });
    });
});
