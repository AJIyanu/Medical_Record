const steps = Array.from(document.querySelectorAll('form .step'));
const nxtBtn = document.querySelectorAll('form .nxt-btn');
const prevBtn = document.querySelectorAll('form .prev-btn');
const form = document.querySelectorAll('form');

nxtBtn.forEach((button) => {
  button.addEventListener('click', () => {
    changeStep('next');
  });
});
prevBtn.forEach((button) => {
  button.addEventListener('click', () => {
    changeStep('prev');
  });
});

form[0].addEventListener('find', (event) => {
  event.preventDefault();
  const nin = document.getElementById('find');
  const err = document.getElementById('errmsg');
  let patientData;
  fetch('/findpatient', {
    method: 'POST',
    body: { NIN: nin }
  })
    .then(function (response) {
      if (response.ok) {
        response.json().then(function (data) {
          patientData = data;
          changeStep('next');
        }).catch(function (error) {
          console.error(error);
        });
      } else {
        response.json().then(function (data) {
          err.innerHTML = 'Patient not found'; // "data.error;
        }).catch(function (error) {
          console.error(error);
        });
      }
    })
    .catch(function (error) {
      console.error(error);
    });
});

form[1].addEventListener('submit', (e) => {
  e.preventDefault();
  const inputs = [];
  form.querySelectorAll('input').forEach((input) => {
    const { name, value } = input;
    inputs.push({ name, value });
  });
  console.log(inputs);
  form.reset();
});

function changeStep (btn) {
  let index = 0;
  const active = document.querySelector('.active');
  index = steps.indexOf(active);
  steps[index].classList.remove('active');
  if (btn === 'next') {
    index++;
  } else if (btn === 'prev') {
    index--;
  }
  steps[index].classList.add('active');
}
