let currentLanguage = localStorage.getItem("openeyes_language") || "en";

function setLanguage(language) {
  currentLanguage = language;
  localStorage.setItem("openeyes_language", language);

  document.documentElement.lang = language;
  document.documentElement.dir = language === "ar" ? "rtl" : "ltr";

  document.querySelectorAll("[data-i18n]").forEach((element) => {
    const key = element.getAttribute("data-i18n");
    element.textContent =
      translations[language]?.[key] ||
      translations.en[key] ||
      element.textContent;
  });
}

function loginWithPi() {
  const scopes = ["username"];

  function onIncompletePaymentFound(payment) {
    console.log("Incomplete payment:", payment);
  }

  Pi.authenticate(scopes, onIncompletePaymentFound)
    .then(function (auth) {
      const welcome = translations[currentLanguage]?.welcome || "Welcome";
      document.getElementById("output").textContent =
        `${welcome}, ${auth.user.username}.`;
    })
    .catch(function (error) {
      document.getElementById("output").textContent =
        "Login error: " + error;
    });
}

document.addEventListener("DOMContentLoaded", () => {
  document.getElementById("languageSelect").value = currentLanguage;
  setLanguage(currentLanguage);
});