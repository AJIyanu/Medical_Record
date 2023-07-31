import { allergy, tags, disability } from "./casefile-taginput.js";
const form = document.querySelector('form');
const submit = document.querySelector('button.submit-btn');
const displayName = document.querySelector('h3.patient-name');
const searchPat = document.getElementById("search-patient");
const errorDisplay = document.getElementById("error");
const nin = document.getElementById('nin-variable').dataset.nin;

let allData;
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

searchPat.addEventListener("input", function(event) {
    let patNin = event.target.value;
    if (patNin.length === 11) {
        axios.get(`http://127.0.0.1:5000/api/v1/user_from_nin/${patNin}`, {
        headers: {
            Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken')
        }
    })
    .then((response) => {
        allData = response.data;
        const patientName = `${allData.patient_data.surname} ${allData.patient_data.firstname} ${allData.patient_data.middlename}`;
        displayName.innerText = patientName;
        searchPat.style.display = 'none';
        displayName.style.display = 'block';
    })
    .catch((error) => {
        console.error(error);
        errorDisplay.innerText = 'error finding patient\'s data or NIN does not exist. click to try again';
        searchPat.style.display = 'none';
        errorDisplay.style.display = 'block';
        patNin = '';
    })
    }
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
    .catch()
})
