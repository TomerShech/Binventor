const ta = document.getElementsByClassName("codeta")[0];
const form = document.querySelector("form");
const submitBtn = document.getElementById("submit_btn");
const MAX_ALLOWED_CHARS = 40000;

function getOS() {
  let platform = window.navigator.platform,
    macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    os = null;

  if (macosPlatforms.indexOf(platform) !== -1) os = "MacOS";
  else if (windowsPlatforms.indexOf(platform) !== -1) os = "Windows";
  else if (!os && /Linux/.test(platform)) os = "Linux";

  return os;
}

function submitWithCtrlS(e) {
  const len = ta.value.length;

  if (getOS() === "MacOS" ? e.metaKey : e.ctrlKey && e.key.toLowerCase() === "s") {
    e.preventDefault(); // prevent saving of website as html file

    if (ta.value !== null && ta.value.trim() !== "" && len <= MAX_ALLOWED_CHARS) {
        form.submit();
    } else if (len > MAX_ALLOWED_CHARS) {
        Notiflix.Report.Failure("THAT'S A LONG ONE!", `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed. (You have ${len})`, "OK");
    } else {
      Notiflix.Report.Failure("Where is the text?", "Paste some code here and try again!", "OK");
    }
  }
}

function submitWithBtn(e) {
  const len = ta.value.length;
  
  e.preventDefault();

  if (ta.value !== null && ta.value.trim() !== "" && len <= MAX_ALLOWED_CHARS) {
    form.submit();
  } else if (len > MAX_ALLOWED_CHARS) {
    Notiflix.Report.Failure("THAT'S A LONG ONE!", `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed. (You have ${len})`, "OK");
  } else {
    Notiflix.Report.Failure("Where is the text?", "Paste some code here and try again!", "OK");
  }
}

ta.onkeydown = function(e) {
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
}

document.addEventListener("keydown", submitWithCtrlS, false);
submitBtn.addEventListener("click", submitWithBtn, false);
