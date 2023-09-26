$(document).ready(function() {
    $("#home-products").owlCarousel({
 
        //Basic Speeds
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : true,
        goToFirst : true,
        goToFirstSpeed : 1000,
        items : 5,

        // Navigation
        navigation : false,
        navigationText : ["prev","next"],
        pagination : true,
        paginationNumbers: false,
    })
    $("#home-services").owlCarousel({
 
        //Basic Speeds
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : true,
        goToFirst : true,
        goToFirstSpeed : 1000,
        items : 5,

        // Navigation
        navigation : false,
        navigationText : ["prev","next"],
        pagination : true,
        paginationNumbers: false,
    })
    $("#home-partners").owlCarousel({
 
        //Basic Speeds
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : true,
        goToFirst : true,
        goToFirstSpeed : 1000,
        items : 5,

        // Navigation
        navigation : false,
        navigationText : ["prev","next"],
        pagination : true,
        paginationNumbers: false,
    })
    $("#home-banner").owlCarousel({
 
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : 10000,
        goToFirst : true,
        goToFirstSpeed : 1000,
        items : 1,

        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false,

        navigation : false,
        navigationText : ["prev","next"],
        pagination : false,
        paginationNumbers: false,
    })

    $("#home-offer").owlCarousel({
 
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : 10000,
        goToFirst : true,
        goToFirstSpeed : 1000,
        items : 1,

        itemsDesktop : false,
        itemsDesktopSmall : false,
        itemsTablet: false,
        itemsMobile : false,

        navigation : false,
        navigationText : ["prev","next"],
        pagination : false,
        paginationNumbers: false,
    })
});