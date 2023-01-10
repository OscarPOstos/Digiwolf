loader = document.getElementById("loader");
submit = document.getElementById("button-submit")

function showLoader() {
    loader.style.display = "block";
}

submit.addEventListener("click", showLoader, false);