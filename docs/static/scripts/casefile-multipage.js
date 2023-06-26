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

// form[0].addEventListener('submit', (event) => {
//   event.preventDefault();
// //   const nin = document.getElementById('findpatient');
// //   const err = document.getElementById('errmsg');
// //   const formData = new FormData();
// //   const patdata = document.getElementById('patdata')
// //   const patdisease = document.getElementById('patdisease')
// //   const patmedics = document.getElementById('patmedics')
// //   formData.append('NIN', nin.value);
// // //  let patientData;
// //   fetch('/findpatient', {
// //     method: 'POST',
// //     body: formData
// //   })
// //     .then(function (response) {
// //       if (response.ok) {
// //         response.json().then(function (data) {
// //           patientData = data;
// 	 // err.innerHTML = JSON.stringify(data)
//           changeStep('next');
// 	  // patdata.innerHTML = `<b>${data.surname} ${data.firstname}<br>Age:</b> ${data.age}`;
// 	  // patdisease.innerHTML = `<b>Past diagnosis</b>: ${data.diseases.map(d => `<li>${d}</li>`).join("")}`;
// 	  // patmedics.innerHTML = `<b>Medications</b>: ${data.medications.map(m => `<li>${m}</li>`).join("")}<br>`;
//     //     }).catch(function (error) {
//     //       console.error(error);
//     //     });
//     //   } else {
//     //     response.json().then(function (data) {
//     //       err.innerHTML = data.error;
//     //     }).catch(function (error) {
//     //       console.error(error);
//     //     });
//     //   }
//     // })
//     // .catch(function (error) {
//     //   console.error(error);
//     // });
// });


form[0].addEventListener('submit', (e) => {
  e.preventDefault();
  form[1].querySelectorAll('input').forEach((input) => {
    const { name, value } = input;
    formData.append( name, value );
  });
  formData.set("symptoms", tags);
  formData.set("patient_id", patientData.id);


  fetch('/doctor/savecasefile', {
    method: 'POST',
    body: formData
  })
  .then(response => {
  if (response.redirected) {
    window.location.href = response.url;
  } else { console.log(response.json())}
})
  .catch(error => console.error(error));
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
