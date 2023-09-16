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