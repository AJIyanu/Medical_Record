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
        document.cookie = 'nin=' + data.nin + ';path=/';
        sessionStorage.setItem('healthvaultaccesstoken', data.access_token);
        localStorage.setItem('healthvaultrefreshtoken', data.refresh_token);
        window.location.href = '/dashboard/' + data.role.toLowerCase();
      //  })
      } else {
        errormsg.innerText = data.error;
      }
      // console.log(data.user.personality);
      // window.location.href = "/dashboard/" + data.user.personality;
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
  const errormsg = document.getElementById('error');

  const email = emailInput.value;
  const password = passwordInput.value;

  if (email === '') {
    errormsg.innerText = 'please fill in your email';
    return;
  }
  if (password === '') {
    errormsg.innerText = 'please fill in your password';
    return;
  }

  const login_details = {
    email: emailInput.value,
    pwd: passwordInput.value
  };

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
        document.cookie = 'nin=' + data.nin + ';path=/';
        sessionStorage.setItem('healthvaultaccesstoken', data.access_token);
        localStorage.setItem('healthvaultrefreshtoken', data.refresh_token);
        window.location.href = '/dashboard/' + data.role.toLowerCase();
      } else {
        errormsg.innerText = data.error;
      }
    })
    .catch(function (error) {
      console.error(error);
    });
});
