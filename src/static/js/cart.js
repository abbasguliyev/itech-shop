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
        var slugs = $(".product-slug-class").toArray()
        var totalPrice = $("#total-price-id").text();
        products_arr = []
        for(var i=0; i<products.length; i++) {
            prod_obj = {}
            prod_obj.slug = slugs[i].innerText
            prod_obj.product = products[i].text
            prod_obj.count = counts[i].value
            products_arr.push(prod_obj)
            console.log(slugs[i].innerText)
        }
        href+=`&text=Salam. Aşağıdakı məhsulları almaq istəyirəm. `
        prod_url = ''
        for(var i=0; i<products_arr.length; i++) {
            href+=`\n${i+1}. ${products_arr[i].product} - ${products_arr[i].count} ədəd, \n`
            prod_url += `\n ${products_arr[i].product}-https://itechshop.az/products/${products_arr[i].slug}/, \n`
        }
        href+=`Ümumi məbləğ: ${totalPrice} AZN.`
        href+=prod_url
        console.log(href)
        window.location.href = href;
    });
});