$(document).ready(function() {
    $("#eth_form input[name='eth_wallet']").bind("input propertychange", function() {
        var eth_wallet = $("#eth_form input[name='eth_wallet']")[0].value;
        if (eth_wallet.length == 0) {
            $('.modal-button').addClass('modal-button--disabled');
        } else {
            $('.modal-button').removeClass('modal-button--disabled');
        }
    })

    eth_wallet_submit = function() {
        if ($('.modal-button').hasClass('modal-button--disabled')) { return false; };
        var eth_wallet = $("#eth_form input[name='eth_wallet']")[0].value;
        if (eth_wallet.length == 42 && eth_wallet.startsWith('0x')) {
            $('.modal-button').addClass('modal-button--disabled');

            $.ajax({
                url: "/eth/wallet/",
                type: "POST",
                cache: false,
                data: {"eth_wallet": eth_wallet},
                success : function(result) {
                    $("#modalSuccess").modal("show");
                }
            });
        } else {
            $("#modalNotFound").modal("show");
            $("#modalNotFound p.text-center").text(gettext('无效的 ETH 钱包地址，请重新输入。'));
        }
    }
});
