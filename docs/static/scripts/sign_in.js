const docsignInBtn = document.getElementById('doc_signin');

docsignInBtn.addEventListener('click', function (event) {
  event.preventDefault();
  const emailInput = document.getElementById('email-input');
  const passwordInput = document.getElementById('password-input');
  const hosIDInput = document.getElementById('hosID');
  const errormsg = document.getElementById('error');

  const email = emailInput.value;
  const password = passwordInput.value;
  const hosID = hosIDInput.value;

  if (email === '') {
    errormsg.innerText = 'please fill in your email';
    // errormsg.style = "red";
    return;
  }
  if (password === '') {
    errormsg.innerText = 'please fill in your password';
    return;
  }

  const login_details = {
    email: emailInput.value,
    pwd: passwordInput.value,
    role: 'Doctor',
    user: 'staff'
  };

  if (hosID !== '') {
    login_details.hosID = hosID;
  }

  fetch('http://127.0.0.1:5000/api/v1/authme', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(login_details)
  })
    .then(response => response.json())
    .then(data => {
      if (!data.hasOwnProperty('error')) {
        localStorage.setItem('healthvaultaccesstoken', data.access_token);
      } else {
      errormsg.innerText = data.error;
      }
      console.log(data.user.personality);
      window.location.href = "/dashboard/" + data.user.personality;
    })
    .catch(function (error) {
      console.error(error);
    });

  // fetch('http://127.0.0.1:5000/api/v1/dashboarddata', {
  //   method: 'GET',
  // })
  // .then(response => response.json())
  // .then(data => {
  // console.log(data)
  // })
});

const signInBtn = document.getElementById('pat_signin');

signInBtn.addEventListener('click', function (event) {
  event.preventDefault();
  const emailInput = document.getElementById('emailinput');
  const passwordInput = document.getElementById('passwordinput');

  const email = emailInput.value;
  const password = passwordInput.value;

  const formData = new FormData();
  formData.append('email', email);
  formData.append('password', password);

  fetch('/signin', {
    method: 'POST',
    body: formData
  })
    .then(function (response) {
      if (response.ok) {
        window.location.href = '/status';
      } else {
      // Handle the case where the server returns an error
        window.location.href = '/signup';
      }
    })
    .catch(function (error) {
      console.error(error);
    });
});
