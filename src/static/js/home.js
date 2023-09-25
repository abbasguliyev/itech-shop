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
    
});