const submit = document.getElementById('submit');
const dofb = document.getElementById('dob');
const req = document.querySelectorAll('[required]');

submit.addEventListener('click', (event) => {
  event.preventDefault();

  let reqcheck = true;
  const selcheck =

  req.forEach(field => {
    if (field.value === '' || field.value === 'null') {
      reqcheck = false;
      console.log(field.value);
    }
  });

  if (reqcheck) {
    const userData = {
      surname: document.getElementById('surname').value,
      middlename: document.getElementById('middlename').value,
      firstname: document.getElementById('firstname').value,
      email: document.getElementById('email').value,
      password: document.getElementById('password').value,
      phone: document.getElementById('phone').value,
      sex: document.getElementById('sex').value,
      user: document.getElementById('jurisdiction').value,
      nin: document.getElementById('nin').value,
      license: document.getElementById('license').value,
      dob: dofb.value,
      address: document.getElementById('address').value,
      workaddress: document.getElementById('workaddress').value,
      religion: document.getElementById('religion').value,
      occupation: document.getElementById('occupation').value,
      nextofkinnin: document.getElementById('nextofkinnin').value
    };
    console.log(userData);

    axios.post('http://127.0.0.1:5000/api/v1/signup', userData, {
      // method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
      // body: JSON.stringify(userData)
    })
      .then(response => {
        console.log(response);
        if (response.data.status === "saved") {
          alert("your data has been saved. Please sign in now")
        window.location.href = '/sigin';
        } else {
          alert("There was an error Registering you. If Error Persists Please contact IT");
        }
      });
  } else {
    alert('please fill all required field');
  }
});
