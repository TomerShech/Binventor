const ta = document.getElementsByClassName("codeta")[0];
const form = document.querySelector("form");
const MAX_ALLOWED_CHARS = 35000;

function getOS() {
  var userAgent = window.navigator.userAgent,
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

document.addEventListener(
  "keydown",
  function(e) {
    if (
      getOS() === "MacOS" ? e.metaKey : e.ctrlKey && e.key.toLowerCase() === "s"
    ) {
      e.preventDefault(); // prevents saving of website as html file

      let len = ta.value.length;

      if (ta.value !== null && ta.value.trim() !== "") {
        if (len <= MAX_ALLOWED_CHARS) {
          form.submit();
        } else {
          Swal.fire(
            "WOW! THAT'S A LONG ONE!",
            `Sorry buddy, currently we only allow pastes with max ${MAX_ALLOWED_CHARS} characters. (You pasted ${len})`,
            "error"
          );
        }
      } else {
        Swal.fire(
          "Where is the text?",
          "I can't see any code here, please try again.",
          "question"
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
