// Navbar
const burger = document.querySelector("nav .burger");
const close = document.querySelector("nav .close-btn");
const nav = document.querySelector("nav ul");
const navLinks = document.querySelectorAll("nav ul li");

burger.addEventListener("click", () => {
  nav.classList.add("nav-show");

  // Animate the nav links
  navLinks.forEach((link, index) => {
    link.style.animation = `navFadeIn 0.5s ease forwards ${index / 7}s`;
  });
});

close.addEventListener("click", () => {
  nav.classList.remove("nav-show");

  // Animate the nav links
  navLinks.forEach(link => {
    link.style.animation = "navFadeOut 0.2s ease backwards";
  });
});
// End of navbar
