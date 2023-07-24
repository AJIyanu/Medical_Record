
const form = document.querySelector('form');
const save = document.querySelector('button');
let formData = {};
const patient_name = document.getElementById('pat-name');
const search = document.getElementById('nin-search');
const searchinput = document.getElementById('ninsearch');
const nin = document.getElementById('nin-variable').dataset.nin;
let patientName;
let allData;
let staffData;

const config = {
  headers: {
    Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken')
  }
};

axios.get('http://127.0.0.1:5000/api/v1/dashboarddata/' + nin, config)
  .then(res => {
    staffData = res.data;
    if (!res.data.institution) {
      alert('you have not signed into any institution. Please sign in again');
      window.location.href = '/signin';
    }
  })
  .catch(err => {
    console.error(err);
    window.location.href = '/signin';
  })

save.addEventListener('click', function (event) {
  event.preventDefault();
  form.querySelectorAll('input').forEach((input) => {
    const { name, value } = input;
    formData[name] = value;
  });
  try {
  formData.staff_id = staffData.user.id;
  formData.healthcare_id = staffData.institution.id;
  formData.patient_id = allData.patient_data.id
  } catch { err => {console.error(err)}
  }

  if (searchinput.value.length !== 11) {
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'red';
    patient_nameclear.textContent = 'please find a patient first';
    setTimeout(function () {
      patient_name.style.color = 'black';
      patient_nameclear.textContent = 'Click to find Patient';
    }, 4000);
  } else if (search.style.display !== 'none') {
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'red';
    patient_nameclear.textContent = 'please click patient name';
  } else {
    axios.post('http://127.0.0.1:5000/api/v1/vitalsign', formData, {
      headers: {
        'Content-Type': 'application/json'
      }
    })
    .then(res => {
      Swal.fire({
        text: res.data.status.success,
        icon: 'success',
        allowOutsideClick: false,
        showCancelButton: true,
        confirmButtonText: 'Home',
        cancelButtonText: 'New'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/dashboard/nurses";
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          window.location.href = "/vitalsign";
        }
      });
    })
    .catch(err => {
      Swal.fire({
          title: err.response.data.status.error,
          text: 'if error persist contact IT',
          icon: 'error',
          allowOutsideClick: false,
          showCancelButton: true,
          confirmButtonText: 'Home',
          cancelButtonText: 'New'
        }).then((result) => {
          if (result.isConfirmed) {
            window.location.href = "/dashboard/nurses";
          } else if (result.dismiss === Swal.DismissReason.cancel) {
            window.location.href = "/vitalsign";
          }

  })
});
}
});

patient_name.addEventListener('click', function (event) {
  if (search.style.display === '') {
    search.style.display = 'none';
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'black';
    patient_nameclear.textContent = 'Click to find patient';
  } else {
    search.style.display = null;
    const patient_nameclear = document.querySelector('h4');
    patient_name.style.color = 'black';
    patient_nameclear.textContent = 'searching...';
  }
});

search.addEventListener('input', function (event) {
  const nin = event.target.value;
  if (nin.length === 11) {
    axios.get(`http://127.0.0.1:5000/api/v1/user_from_nin/${nin}`, config)
      .then((res) => {
        allData = res.data;
        const result = document.querySelector('li');
        patientName = allData.patient_data.surname + ' ' + allData.patient_data.firstname;
        result.innerText = patientName;
      }).catch((err) => {
        console.error(err);
      });
  } else {
    const result = document.querySelector('li');
    result.innerText = '';
  }
});

const update = document.querySelector('li');
update.addEventListener('click', function (event) {
  const patient_nameclear = document.querySelector('h4');
  patient_nameclear.textContent = patientName;
  search.style.display = 'none';
});
