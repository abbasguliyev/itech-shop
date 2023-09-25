hamburger = document.querySelector(".hamburger");
hamburger.onclick = function() {
    navBar = document.querySelector(".nav-bar")
    navBar.classList.toggle("active")
}

main = document.querySelector("#main-wrapper").addEventListener('click', closeHamburger);

function closeHamburger() {
    navBar = document.querySelector(".nav-bar")
    navBar.classList.remove("active")
}

$(document).ready(function() {
 
    $(".owl-carousel").owlCarousel({
 
        //Basic Speeds
        slideSpeed : 200,
        paginationSpeed : 800,
     
        //Autoplay
        autoPlay : true,
        goToFirst : true,
        goToFirstSpeed : 1000,
     
        // Navigation
        navigation : false,
        navigationText : ["prev","next"],
        pagination : true,
        paginationNumbers: true,
     
        // Responsive
        responsive: true,
        items : 1,
        itemsDesktop : [1199,4],
        itemsDesktopSmall : [980,3],
        itemsTablet: [768,2],
        itemsMobile : [479,1]
     
    })
   
});