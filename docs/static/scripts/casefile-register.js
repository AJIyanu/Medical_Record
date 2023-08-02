import { tags } from "./casefile-taginput.js";
import { allData } from "./casefile-api-data.js";
const form = document.querySelector('form');
const searchPat = document.getElementById("search-patient");
const submit = document.querySelector('button.submit-btn');
const displayName = document.querySelector('h3.patient-name');
const errorDisplay = document.getElementById("error");
const nin = document.getElementById('nin-variable').dataset.nin;

let staffData;

const config = {
    headers: {
      Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken'),
      'Content-Type': 'application/json',
    }
  };

// console.log(form, submit, formdata);
axios.get('http://127.0.0.1:5000/api/v1/dashboarddata/' + nin, {
  headers: {
    Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken')
}
})
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

displayName.addEventListener('click', function() {
    displayName.style.display = 'none';
    searchPat.style.display = 'block';
})

errorDisplay.addEventListener('click', () => {
    errorDisplay.style.display = 'none';
    searchPat.style.display = 'block';
})

submit.addEventListener("click", (register) => {
    register.preventDefault();
    const formdata = new FormData(form);

    const filedata = {};
    formdata.forEach((value, key) => {
        filedata[key] = value;
    })
    filedata["symptoms"] = JSON.stringify(tags);
    try {
        filedata.staff_id = staffData.user.id;
        filedata.healthcare_id = staffData.institution.id;
        filedata.patient_id = allData.patient_data._Person__nin
        } catch { err => {console.error(err)}
    }

    axios.post("http://127.0.0.1:5000/api/v1/casefile", filedata, config)
    .then(response => {
      Swal.fire({
        text: response.data.status.success,
        icon: 'success',
        allowOutsideClick: false,
        showCancelButton: true,
        confirmButtonText: 'Home',
        cancelButtonText: 'New'
      }).then((result) => {
        if (result.isConfirmed) {
          window.location.href = "/dashboard/doctor";
        } else if (result.dismiss === Swal.DismissReason.cancel) {
          window.location.href = "/casefile";
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
            window.location.href = "/casefile";
          }
        });
      });
})
