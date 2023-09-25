const form = document.querySelectorAll('form');
const steps = Array.from(document.querySelectorAll('form .step'));
const nxtBtn = document.querySelectorAll('form .nxt-btn');
const prevBtn = document.querySelectorAll('form .prev-btn');
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
