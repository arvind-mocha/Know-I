// nav links state
var path = window.location.pathname;

if (path == "/events/") {
  document.querySelector(".navbar-nav").children[0].children[0].classList.add("active");
}

if (path == "/members/") {
  document.querySelector(".navbar-nav").children[1].children[0].classList.add("active");
}

if (path == "/blog/") {
  document.querySelector(".navbar-nav").children[2].children[0].classList.add("active");
}

if (path == "/resources/") {
  document.querySelector(".navbar-nav").children[3].children[0].classList.add("active");
}
