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

    fetch('/signup', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(userData)
    })
      .then(response => {
        console.log(response);
      });
  } else {
    alert('please fill all required field');
  }
});
