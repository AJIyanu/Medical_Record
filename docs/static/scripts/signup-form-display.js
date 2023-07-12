
const proceed = document.getElementById('proceed');
const steps = Array.from(document.querySelectorAll('form .step'));
const nxtBtn = document.querySelectorAll('form .nxt-btn');
const prevBtn = document.querySelectorAll('form .prev-btn');
const nin = document.getElementById('nin');
const left = document.getElementById('left-nav');
const right = document.getElementById('right-nav');

const formData = new FormData();

let patientData;

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

left.addEventListener('click', () => {
  changeStep('prev');
  right.style.display = 'bkock';
});
right.addEventListener('click', () => { changeStep('next'); });

proceed.addEventListener('click', (event) => {
  event.preventDefault();
  const pwd = document.getElementById('password');
  const vpwd = document.getElementById('vpassword');
  const err = document.getElementById('errmsg');
  const email = document.getElementById('email');

  if (pwd.value !== vpwd.value) {
    err.innerHTML = '<p>password must be same</p>';
  } else {
    formData.set('email', email.value);
    formData.set('password', pwd.value);
    changeStep('next');
    right.style.display = 'block';
  }
});

function changeStep (btn) {
  let index = 0;
  const active = document.querySelector('.active');
  index = steps.indexOf(active);
  steps[index].classList.remove('active');
  if (btn === 'next') {
    index++;
    if (index === steps.length - 1) {
      right.style.display = 'none';
    } else if (index > 0) {
      left.style.display = 'block';
    }
  } else if (btn === 'prev') {
    index--;
    if (index === 0) {
      left.style.display = 'none';
    } else if (index === steps.length - 2) {
      right.style.display = 'block';
    }
  }
  steps[index].classList.add('active');
}

nin.addEventListener('input', () => {
  if (nin.value.length === 11) {
    changeStep('next');
    left.style.display = 'block';
  }
});

const person = document.getElementById('personality');
const jurislabel = document.getElementById('staff');
const juris = document.getElementById('jurisdiction');
const license = document.getElementById('license');
const licenselabel = document.getElementById('licnse');

person.addEventListener('change', () => {
  if (person.value === 'Staff') {
    juris.style.display = 'block';
    jurislabel.style.display = 'block';
    license.style.display = 'block';
    licenselabel.style.display = 'block';
    revealElements();
  } else {
    juris.style.display = 'none';
    jurislabel.style.display = 'none';
    license.style.display = 'none';
    licenselabel.style.display = 'none';
  }
});

const elements = document.querySelectorAll('.slide-in');

// Function to apply "reveal" class for slide-in animation
function revealElements () {
  elements.forEach(element => {
    element.classList.add('reveal');
  });
}

// let index = 0;
// const active = document.querySelector('.active');
// index = steps.indexOf(active);

// if (index > 0) {
//  left.style.display = 'block';
//  console.log("here");
// } else {
//  left.style.display = 'none';
// }
//
// if (index === steps.length - 1) {
//  right.style.display = 'none';
// } else if (index === 0 || index === 1) {
//  right.style.display = 'none';
// } else {
//  right.style.display = 'block';
// }
