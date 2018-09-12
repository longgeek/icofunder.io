$(document).ready(function() {
    var regex = /(.jpg|.jpeg|.gif|.png|.bmp|.svg)$/;

    kyc_one = function() {
        check_kyc_form();
        file = $("#kyc_form input[name='image1']")[0].files[0];
        if (file.size > 2*1024*1024) {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(gettext('上传的图片大小不能超过 2MB，请重新选择。'));
            $("#kyc_form input[name='image1']").val("");
            return false;
        }
        preview = $(".kyc-upload-action.one");
        if (regex.test(file.name.toLowerCase())) {
            var reader = new FileReader();
            reader.onload = function (e) {
                preview.css("background-image", "url('" + e.target.result + "')");
            }
            reader.readAsDataURL(file);
        } else {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(file.name + gettext(' 不是有效的图片文件类型。'));
            preview.css("background-image", "none");
        }
    }

    kyc_two = function() {
        check_kyc_form();
        file = $("#kyc_form input[name='image2']")[0].files[0];
        if (file.size > 2*1024*1024) {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(gettext('上传的图片大小不能超过 2MB，请重新选择。'));
            $("#kyc_form input[name='image2']").val("");
            return false;
        }
        preview = $(".kyc-upload-action.two");
        if (regex.test(file.name.toLowerCase())) {
            var reader = new FileReader();
            reader.onload = function (e) {
                preview.css("background-image", "url('" + e.target.result + "')");
            }
            reader.readAsDataURL(file);
        } else {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(file.name + gettext(' 不是有效的图片文件类型。'));
            preview.css("background-image", "none");
        }
    }

    kyc_three = function() {
        check_kyc_form();
        file = $("#kyc_form input[name='image3']")[0].files[0];
        if (file.size > 2*1024*1024) {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(gettext('上传的图片大小不能超过 2MB，请重新选择。'));
            $("#kyc_form input[name='image3']").val("");
            return false;
        }
        preview = $(".kyc-upload-action.three");
        if (regex.test(file.name.toLowerCase())) {
            var reader = new FileReader();
            reader.onload = function (e) {
                preview.css("background-image", "url('" + e.target.result + "')");
            }
            reader.readAsDataURL(file);
        } else {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(file.name + gettext(' 不是有效的图片文件类型。'));
            preview.css("background-image", "none");
        }
    }


    check_kyc_form = function() {
        fullname = $("#kyc_form input[name='fullname']")[0].value;
        image1 = $("#kyc_form input[name='image1']")[0].files[0];
        image2 = $("#kyc_form input[name='image2']")[0].files[0];
        image3 = $("#kyc_form input[name='image3']")[0].files[0];
        if (fullname && image1 && image2 && image3) {
            $("#kyc_form .btn")[0].removeAttribute('disabled');
            return true;
        } else {
            $("#kyc_form .btn")[0].setAttribute('disabled', 'disabled');
            return false;
        }
    }

    /* KYC FULLNAME CHANGE */
    $("#kyc_form input[name='fullname']").bind("input propertychange", function() {
        check_kyc_form();
    })


    /* KYC SUBMIT */
    kyc_submit = function() {
        if (check_kyc_form() != true) { return false; }
        $("#kyc_form .btn")[0].setAttribute('disabled', 'disabled');
        var formData = new FormData($('#kyc_form')[0]);

        $.ajax({
            url: "/kyc/upload/",
            type: "POST",
            cache: false,
            data: formData,
            processData: false,
            contentType: false,
            success : function(result) {
                $("#modalSuccess").modal("show");
            }
        });
    }
});
