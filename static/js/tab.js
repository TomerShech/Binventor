document.querySelector("textarea").onkeydown = function(e) {
  if (e.keyCode === 9 || e.which === 9) {
    e.preventDefault();

    // get caret position/selection
    let val = this.value,
      start = this.selectionStart,
      end = this.selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    this.value = val.substring(0, start) + "\t" + val.substring(end);

    // put caret at right position again
    this.selectionStart = this.selectionEnd = start + 1;

    // prevent the focus lose
    return false;
  }
};
