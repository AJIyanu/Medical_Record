const submit = document.querySelector(".submit-btn");
const dofb = document.getElementById("dob");

dateofbirth = new Date(dofb);
const formData = {
    surname: document.getElementById("surname").value,
    middlename: document.getElementById("middlename").value,
    firstname: document.getElementById("firstname").value,
    email: document.getElementById("email").value,
    password: document.getElementById("password").value,
    phone: document.getElementById("phone").value,
    sex: document.getElementById("sex").value,
    user: document.getElementById("jurisdiction").value,
    nin: document.getElementById("nin").value,
    license: document.getElementById("license").value,
    dob: dateofbirth.toJson(),
    address: document.getElementById("address").value,
    workaddress: document.getElementById("workaddress").value,
    religion: document.getElementById("religion").value,
    occupation: document.getElementById("occupation").value,
    nextofkinnin: document.getElementById("nextofkinnin").value,
}

submit.addEventListener("click", (event) => {
    event.preventDefault();

    fetch("/signup", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(formData)
    })
    .then(response, () => {
        console.log(response);
    })
})
