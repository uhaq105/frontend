function changeColor(color) {
  document.querySelector(".section-hero").style.backgroundColor = color;
}

function changeBackground(colors) {
  document.querySelector(".box-a").style.backgroundColor = colors;
  document.querySelector(".box-b").style.backgroundColor = colors;
  document.querySelector(".box-c").style.backgroundColor = colors;
  document.querySelector(".box-d").style.backgroundColor = colors;
}

function changeLogoColor(logo) {
  document.querySelector(".header").style.backgroundColor = logo;
}

const btnNavEl = document.querySelector(".btn-mobile-nav");
const headerEl = document.querySelector(".header");

btnNavEl.addEventListener("click", function () {
  headerEl.classList.toggle("nav-open");
});
