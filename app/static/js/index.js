let ta = document.getElementById("ta");
let code = document.querySelector("code");

document.addEventListener(
  "keydown",
  function(e) {
    if (
      (window.navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey) &&
      e.keyCode == 83 // S key
    ) {
      e.preventDefault();

      if (ta.value) {
        let temp = ta.value;
        ta.parentNode.removeChild(ta);
        code.textContent = temp;
        hljs.highlightBlock(code);
      } else {
        swal(
          "Seems like no code was pasted",
          "Ugh! I can't see any code here. maybe try again?",
          "error"
        );
      }
    }
  },
  false
);

function insertTab(o, e) {
  let kC = e.keyCode ? e.keyCode : e.charCode ? e.charCode : e.which;
  if (kC === 9 && !e.shiftKey && !e.ctrlKey && !e.altKey) {
    let oS = o.scrollTop;
    if (o.setSelectionRange) {
      let sS = o.selectionStart;
      let sE = o.selectionEnd;
      o.value = o.value.substring(0, sS) + "\t" + o.value.substr(sE);
      o.setSelectionRange(sS + 1, sS + 1);
      o.focus();
    } else if (o.createTextRange) {
      document.selection.createRange().text = "\t";
      e.returnValue = false;
    }
    o.scrollTop = oS;
    if (e.preventDefault) {
      e.preventDefault();
    }
    return false;
  }
  return true;
}

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
