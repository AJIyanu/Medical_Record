const error = document.getElementById("error");
const nin = document.getElementById("nin");
const email = document.getElementById("email")

// console.log(error.dataset.error, typeof(error.dataset.error));
if (error.dataset.error.indexOf("nin") !== -1 || error.dataset.error.indexOf("NIN") !== -1) {
    nin.value = "";
    nin.placeholder = error.dataset.error;
    // console.log("was here")
}

if (error.dataset.error.indexOf("email") !== -1) {
    email.value = "";
    email.placeholder = error.dataset.error;
}
