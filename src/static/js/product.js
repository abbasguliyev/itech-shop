$(document).ready(function () {
    let main_image = $('.main-prod-image')[0]
    $('.slider-prod-image').each(function () {
        $(this).click(function (e) { 
            e.preventDefault();
            let newSrc = this.getAttribute('data-main-image');
            main_image.src = newSrc
            magnify("main-prod-image-id", 3);

        });
    });
});
