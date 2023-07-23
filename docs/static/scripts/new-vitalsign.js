
const form = document.querySelector('form');
const save = document.querySelector('button');
const formData = new FormData();
const patient_name = document.getElementById('pat-name');
const search = document.getElementById('nin-search')
const searchinput = document.getElementById('ninsearch');

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
    alert("your data has been saved")
    window.location.href = 'doctor.html'
    // console.log(searchinput.value)
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
    axios.get("http://127.0.0.1:5000/api/v1/user_from_nin/" + nin)
    .then((res) => {
        const result = document.querySelector('li');
        result.innerText = res.data.surname + " " + res.data.firstname;
    }).catch((err) => {
        console.error(err)
    });
    // result.innerText = "Aderemi Joseph Iyanu"
  } else {
    const result = document.querySelector('li');
    result.innerText = ""
  }
})

const update = document.querySelector('li');
update.addEventListener('click', function(event) {
  const patient_nameclear = document.querySelector('h4');
  patient_nameclear.textContent = "AJ Iyanu";
  search.style.display = 'none';
})
