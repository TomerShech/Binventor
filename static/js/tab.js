document.querySelectorAll("textarea").forEach(function(ta) {
  ta.addEventListener(
    "keydown",
    function(e) {
      if (e.keyCode === 9) {
        // tab was pressed
        // get caret position/selection
        let start = this.selectionStart;
        let end = this.selectionEnd;

        let target = e.target;
        let value = target.value;

        // set textarea value to: text before caret + tab + text after caret
        target.value = value.substring(0, start) + "\t" + value.substring(end);

        // put caret at right position again (add one for the tab)
        this.selectionStart = this.selectionEnd = start + 1;

        // prevent the focus lose
        e.preventDefault();
      }
    },
    false
  );
});
