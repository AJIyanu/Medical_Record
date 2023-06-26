const docsignInBtn = document.getElementById('doc_signin');

docsignInBtn.addEventListener('click', function (event) {
  event.preventDefault();
  const emailInput = document.getElementById('email-input');
  const passwordInput = document.getElementById('password-input');
  const hosIDInput = document.getElementById('hosID');

  const email = emailInput.value;
  const password = passwordInput.value;
  const hosID = hosIDInput.value;

  const formData = new FormData();
  formData.append('email', email);
  formData.append('password', password);
  formData.append('institution_id', hosID);

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
