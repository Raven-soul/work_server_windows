window.ajax_cart_update = function(t, e, n) {
    console.log("ajax_cart_update");
    var r = ""
      , i = (r = t.closest("tr")).find(".total_price").val()
      , a = t.attr("min");
    if (n <= a && (n = a),
    -1 == n) {
        var s = _t("Are you sure you want to remove this item from cart?");
        if (!confirm(s))
            return;
        r.fadeOut("fast", (function() {
            r.remove(),
            $.ajax({
                type: "POST",
                dataType: "json",
                url: g_params.url_prefix + "/ajax_cart_update",
                data: {
                    ciid: e,
                    qty: n
                },
                success: function(t) {
                    if ($(".error-message").remove(),
                    $(".success-message").remove(),
                    t.warnings && t.warnings.length)
                        for (var e in t.warnings)
                            $(t.warnings[e]).insertBefore($("#uc-cart-view-form"));
                    1 == t.result && 1 == t.isflowers ? (r.find(".total_in_product").val(t.price),
                    r.find(".price").find(".uc-price").text(o(t.price))) : (r.find(".total_in_product").val(i * n),
                    r.find(".price").find(".uc-price").text(o(i * n))),
                    t.points && $(".discount-msg").html(t.points);
                    var a = 0;
                    $(".total_in_product").each((function() {
                        var t = $(this).val();
                        a += 1 * t
                    }
                    )),
                    $(".products_subtotal").find(".uc-price").text(o(a)),
                    parseInt($(".delivery_cost").val()) && (a += 1 * parseInt($(".delivery_cost").val())),
                    a -= 1 * t.discount,
                    $(".total").find(".uc-price").text(o(a)),
                    t.discount > 0 ? ($(".discount-subtotal").find(".uc-price").text(o(t.discount)),
                    $(".discount-subtotal").closest(".subtotal").removeClass("hidden")) : $(".discount-subtotal").closest(".subtotal").addClass("hidden"),
                    ($(".error-message").length || $(".success-message").length) && $(".error-message,.success-message").on("click touch", (function(t) {
                        t.offsetX > $(this).width() + parseInt($(this).css("padding-left")) && $(this).closest("div").fadeOut()
                    }
                    ))
                }
            })
        }
        ))
    } else
        $.ajax({
            type: "POST",
            dataType: "json",
            url: g_params.url_prefix + "/ajax_cart_update",
            data: {
                ciid: e,
                qty: n
            },
            success: function(t) {
                if ($(".error-message").remove(),
                $(".success-message").remove(),
                t.warnings && t.warnings.length)
                    for (var e in t.warnings)
                        $(t.warnings[e]).insertBefore($("#uc-cart-view-form"));
                r.find(".qty_cart_update").val(n),
                1 == t.result && 1 == t.isflowers ? (r.find(".total_in_product").val(t.price),
                r.find(".price").find(".uc-price").text(o(t.price))) : (r.find(".total_in_product").val(i * n),
                r.find(".price").find(".uc-price").text(o(i * n))),
                "" != t.url && r.find(".imagecache-cart").attr("src", t.url),
                t.points && $(".discount-msg").html(t.points);
                var a = 0;
                $(".total_in_product").each((function() {
                    var t = $(this).val();
                    a += 1 * t
                }
                )),
                $(".products_subtotal").find(".uc-price").text(o(a)),
                parseInt($(".delivery_cost").val()) && (a += 1 * parseInt($(".delivery_cost").val())),
                a -= 1 * t.discount,
                a = Math.round(a),
                $(".total").find(".uc-price").text(o(a)),
                t.discount > 0 ? ($(".discount-subtotal").find(".uc-price").text(o(t.discount)),
                $(".discount-subtotal").closest(".subtotal").removeClass("hidden")) : $(".discount-subtotal").closest(".subtotal").addClass("hidden"),
                ($(".error-message").length || $(".success-message").length) && $(".error-message,.success-message").on("click touch", (function(t) {
                    t.offsetX > $(this).width() + parseInt($(this).css("padding-left")) && $(this).closest("div").fadeOut()
                }
                ))
            }
        })
}