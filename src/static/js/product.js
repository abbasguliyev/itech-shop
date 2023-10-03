$(document).ready(function () {
    let main_image = $('.main-prod-image')[0]
    $('.slider-prod-image').each(function () {
        $(this).click(function (e) { 
            e.preventDefault();
            main_image.src = this.src
        });
    });
});