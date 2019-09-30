const ta = document.querySelector("textarea");
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

  if (
    getOS() === "MacOS" ? e.metaKey : e.ctrlKey && e.key.toLowerCase() === "s"
  ) {
    e.preventDefault(); // prevent saving of website as html file

    if (
      ta.value !== null &&
      ta.value.trim() !== "" &&
      len <= MAX_ALLOWED_CHARS
    ) {
      form.submit();
    } else if (len > MAX_ALLOWED_CHARS) {
      Swal.fire({
        title: "WOW! THAT'S A LONG ONE!",
        text: `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed (you have ${len})`,
        type: "error"
      });
    } else {
      Swal.fire({
        title: "Where is the text?",
        text: "Paste some code here and try again!",
        type: "question"
      });
      document.documentElement.classList.add("fix");
    }
  }
}

function submitWithBtn(e) {
  const len = ta.value.length;

  e.preventDefault();

  if (ta.value !== null && ta.value.trim() !== "" && len <= MAX_ALLOWED_CHARS) {
    form.submit();
  } else if (len > MAX_ALLOWED_CHARS) {
    Swal.fire({
      title: "WOW! THAT'S A LONG ONE!",
      text: `Sorry buddy, currently only pastes with max ${MAX_ALLOWED_CHARS} characters are allowed (you have ${len})`,
      type: "error"
    });
  } else {
    Swal.fire({
      title: "Where is the text?",
      text: "Paste some code here and try again!",
      type: "question"
    });
  }
}

document.addEventListener("keydown", submitWithCtrlS, false);
submitBtn.addEventListener("click", submitWithBtn, false);
