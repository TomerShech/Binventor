const ta = document.getElementsByClassName("codeta")[0];
const form = document.querySelector("form");
const submitBtn = document.getElementById("submit_btn");
const MAX_ALLOWED_CHARS = 35000;
const len = ta.value.length;

function getOS() {
  let userAgent = window.navigator.userAgent,
    platform = window.navigator.platform,
    macosPlatforms = ["Macintosh", "MacIntel", "MacPPC", "Mac68K"],
    windowsPlatforms = ["Win32", "Win64", "Windows", "WinCE"],
    iosPlatforms = ["iPhone", "iPad", "iPod"],
    os = null;

  if (macosPlatforms.indexOf(platform) !== -1) os = "MacOS";
  else if (iosPlatforms.indexOf(platform) !== -1) os = "iOS";
  else if (windowsPlatforms.indexOf(platform) !== -1) os = "Windows";
  else if (/Android/.test(userAgent)) os = "Android";
  else if (!os && /Linux/.test(platform)) os = "Linux";

  return os;
}

let submitWithCtrlS = function(e) {
  if (
    getOS() === "MacOS" ? e.metaKey : e.ctrlKey && e.key.toLowerCase() === "s"
  ) {
    e.preventDefault(); // prevent saving of website as html file

    if (ta.value !== null && ta.value.trim() !== "") {
      if (len <= MAX_ALLOWED_CHARS) form.submit();
      else {
        Swal.fire(
          "WOW! THAT'S A LONG ONE!",
          `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed. (You have ${len})`,
          "error"
        );
      }
    } else {
      Swal.fire(
        "Where is the text?",
        "I don't see any code here, please try again.",
        "question"
      );
    }
  }
};

let submitWithBtn = function(e) {
  e.preventDefault();

  if (ta.value !== null && ta.value.trim() !== "") {
    if (len <= MAX_ALLOWED_CHARS) form.submit();
    else {
      Swal.fire(
        "WOW! THAT'S A LONG ONE!",
        `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed. (You have ${len})`,
        "error"
      );
    }
  } else {
    Swal.fire(
      "Where is the text?",
      "I don't see any code here, please try again.",
      "question"
    );
  }
};

document.addEventListener("keydown", submitWithCtrlS, false);
document.addEventListener("submit", submitWithBtn, false);

ta.onkeydown = function(e) {
  if (e.keyCode === 9 || e.which === 9) {
    e.preventDefault();

    // get caret position/selection
    let val = this.value;
    let start = this.selectionStart;
    let end = this.selectionEnd;

    // set textarea value to: text before caret + tab + text after caret
    this.value = val.substring(0, start) + "\t" + val.substring(end);

    // put caret at right position again
    this.selectionStart = this.selectionEnd = start + 1;

    // prevent the focus lose
    return false;
  }
};
