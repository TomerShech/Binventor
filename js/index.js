import hljs from "./highlight.pack.js";

let ta = document.getElementById("ta");

document.addEventListener("DOMContentLoaded", event => {
  document.querySelectorAll("pre code").forEach(block => {
    hljs.highlightBlock(block);
  });
});

function insertTab(o, e) {
  let kC = e.keyCode ? e.keyCode : e.charCode ? e.charCode : e.which;
  if (kC == 9 && !e.shiftKey && !e.ctrlKey && !e.altKey) {
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

document.addEventListener(
  "keydown",
  function(e) {
    if (
      (window.navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey) &&
      e.keyCode == 83 // S
    ) {
      e.preventDefault();

      if (ta.value) {
        let code = document.getElementsByTagName("code");
        let code_node = document.createTextNode(ta.value);
        ta.remove();
        code[0].appendChild(code_node);
        hljs.highlightAuto(code[0].value);
      } else {
        swal(
          "Seems like no code was pasted",
          "Ugh! I can't see any code here.. Try again.",
          "error"
        );
      }
    }
  },
  false
);
