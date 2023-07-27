import { allergy, tags, disability } from "./casefile-taginput.js";
const form = document.querySelector('form');
const submit = document.querySelector('button.submit-btn');
const formdata = new FormData(form);
const config = {
    headers: {
      Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken'),
      'Content-Type': 'application/json',
    }
  };

// console.log(form, submit, formdata);

submit.addEventListener("click", (register) => {
    register.preventDefault();

    const filedata = {};
    formdata.forEach((value, key) => {
        filedata[key] = value;
    })

    axios.post("http://127.0.0.1:5000/api/v1/casefile", config)
    .then(response => console.log(response.data));
    console.log(filedata);
})
