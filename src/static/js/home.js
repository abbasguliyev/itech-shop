$(document).ready(function() {
    $("#home-products").owlCarousel({
        autoplay:true,
        autoplayTimeout:5000,
        responsiveClass:true,
        margin:5,
        dots: false,
        autoWidth: true,
        items : 7,
        loop: true,
    })
    $("#home-services").owlCarousel({
        autoplay:true,
        autoplayTimeout:5000,
        responsiveClass:true,
        margin:5,
        dots: false,
        autoWidth: true,
        items : 7,
        loop: true,
    })
    $("#home-partners").owlCarousel({
        autoplay:true,
        autoplayTimeout:5000,
        responsiveClass:true,
        margin:5,
        dots: false,
        autoWidth: true,
        items : 7,
        loop: true,
    })
    $("#home-banner").owlCarousel({
        autoplay:true,
        autoplayTimeout:10000,
        responsiveClass:true,
        dots: false,
        loop:true,
        margin:10,
        items : 1,
    })

    $("#home-offer").owlCarousel({
        autoPlay:true,
        autoplayTimeout:5000,
        responsiveClass:true,
        dots: false,
        loop:true,
        margin:10,
        items : 1,
    })
});