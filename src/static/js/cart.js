$(document).ready(function() {    
    $('.minus').click(function () {
        let all_price = parseFloat($("#total-price-id").text())

        var $input = $(this).parent().find('input');
        var count = parseInt($input.val()) - 1;
        if(count >= 1) {
            count = count < 1 ? 1 : count;
            $input.val(count);
            $input.change();
            var quantity = parseInt($input.val());
            var price = parseFloat($(this).closest("li").find("#cart-prod-default-price-id").text());
            var totalPrice = price * quantity;
            $(this).closest("li").find("#cart-prod-price-id").text(totalPrice.toFixed(2));
            all_price -= price
            all_price = all_price.toFixed(2);
            $("#total-price-id").text(all_price)
            return false;
        }
    });
    $('.plus').click(function () {
        let all_price = parseFloat($("#total-price-id").text())

        var $input = $(this).parent().find('input');
        $input.val(parseInt($input.val()) + 1);
        $input.change();
        var quantity = parseInt($input.val());
        var price = parseFloat($(this).closest("li").find("#cart-prod-default-price-id").text());
        var totalPrice = quantity * price;
        $(this).closest("li").find("#cart-prod-price-id").text(totalPrice.toFixed(2));
        all_price += price
        all_price = all_price.toFixed(2);
        $("#total-price-id").text(all_price)
        return false;
    });

    $("#submit-order-btn-id").click(function() {
        var href = $("#submit-order-btn-id").attr('href')
        var products = $(".product-name-class").toArray()
        var counts = $(".cart-prod-count").toArray()
        var totalPrice = $("#total-price-id").text();
        products_arr = []
        for(var i=0; i<products.length; i++) {
            prod_obj = {}
            prod_obj.product = products[i].text
            prod_obj.count = counts[i].value
            products_arr.push(prod_obj)
        }
        href+=`&text=Salam. Aşağıdakı məhsulları almaq istəyirəm. `
        for(var i=0; i<products_arr.length; i++) {
            href+=`${i+1}. ${products_arr[i].product} - ${products_arr[i].count} ədəd, `
        }
        href+=` Ümumi məbləğ: ${totalPrice} AZN.`
        console.log(href)
        window.location.href = href;
    });
});