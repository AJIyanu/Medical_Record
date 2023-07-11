
const proceed = document.getElementById('proceed');
const steps = Array.from(document.querySelectorAll('form .step'));
const nxtBtn = document.querySelectorAll('form .nxt-btn');
const prevBtn = document.querySelectorAll('form .prev-btn');
const nin = document.getElementById("nin");

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

proceed.addEventListener('click', (event) => {
  event.preventDefault();
  const pwd = document.getElementById('password');
  const vpwd = document.getElementById('vpassword');
  const err = document.getElementById('errmsg');
  const email = document.getElementById('email');

  if (pwd.value !== vpwd.value) {
    err.innerHTML = `<p>password must be same</p>`
  } else {
    formData.set("email", email.value);
    formData.set("password", pwd.value);
    changeStep('next');
  }
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

nin.addEventListener("input", () => {
  if (nin.value.length == 11) {
    changeStep("next");
  }
})

const person = document.getElementById("personality");
const jurislabel = document.getElementById("staff");
const juris = document.getElementById("jurisdiction");
const license = document.getElementById("license");
const licenselabel = document.getElementById("licnse");

person.addEventListener("change", () => {
  if (person.value == "Staff") {
    juris.style.display = "block";
    jurislabel.style.display = "block";
    license.style.display = "block";
    licenselabel.style.display = "block";
    revealElements();
  } else {
    juris.style.display = "none";
    jurislabel.style.display = "none";
    license.style.display = "none";
    licenselabel.style.display = "none";
  }
})

const elements = document.querySelectorAll('.slide-in');

  // Function to apply "reveal" class for slide-in animation
  function revealElements() {
    elements.forEach(element => {
      element.classList.add('reveal');
    });
  }
