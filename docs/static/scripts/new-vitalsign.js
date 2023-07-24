
const form = document.querySelector('form');
const save = document.querySelector('button');
const formData = new FormData();
const patient_name = document.getElementById('pat-name');
const search = document.getElementById('nin-search')
const searchinput = document.getElementById('ninsearch');
let patientName;
let allData;

save.addEventListener('click', function (event) {
  event.preventDefault();
  form.querySelectorAll('input').forEach((input) => {
    const { patient_name, value } = input;
    formData.append( patient_name, value );
    });

  if ( searchinput.value.length !== 11 ) {
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'red';
    patient_nameclear.textContent = "please find a patient first";
    setTimeout(function() {
      patient_name.style.color = 'black'
      patient_nameclear.textContent = "Click to find Patient";
        }, 4000);
  } else if (search.style.display !== 'none') {
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'red';
    patient_nameclear.textContent = "please click patient name"
  } else {

  }
});

patient_name.addEventListener('click', function(event) {
  if (search.style.display === '') {
    search.style.display = 'none';
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'black'
    patient_nameclear.textContent = "Click to find patient";
  } else {
  search.style.display = null;
  const patient_nameclear = document.querySelector('h4');
  patient_name.style.color = 'black'
  patient_nameclear.textContent = "searching...";
  }
})

search.addEventListener('input', function(event) {
  const nin = event.target.value;
  if (nin.length === 11) {
    axios.get(`http://127.0.0.1:5000/api/v1/user_from_nin/${nin}`)
    .then((res) => {
        allData = res.data;
        const result = document.querySelector('li');
        patientName = allData.patient_data.surname + " " + allData.patient_data.firstname;
        result.innerText = patientName;
    }).catch((err) => {
        console.error(err)
    });
  } else {
    const result = document.querySelector('li');
    result.innerText = ""
  }
})

const update = document.querySelector('li');
update.addEventListener('click', function(event) {
  const patient_nameclear = document.querySelector('h4');
  patient_nameclear.textContent = patientName;
  search.style.display = 'none';
})
