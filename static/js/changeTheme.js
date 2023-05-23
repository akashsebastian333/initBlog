var root = document.querySelector(":root");
var changeTheme = document.querySelector(".changeTheme");

var theme = "theme";

if (localStorage.getItem(theme) === "dark") {
  toDark();
}
else {
  toDark(); // set theme to dark by default
}

function toDark() {
  localStorage.setItem(theme, "dark");
  root.style.setProperty("--themePrimary", "#fff");
  root.style.setProperty("--themeSecondary", "#000");
  root.style.setProperty("--themeHelper", "#C6C6C6");
  changeTheme.setAttribute("onclick", "javascript: toDark();");
}
