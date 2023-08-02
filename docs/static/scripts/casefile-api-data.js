const searchPat = document.getElementById("search-patient");
const displayName = document.querySelector('h3.patient-name');
const errorDisplay = document.getElementById("error");
const age = document.getElementById("age");
const sex = document.getElementById("sex");
const blood = document.getElementById("blood-group");
const allergies = document.getElementById("allergies");
const genotype = document.getElementById("genotype");
const admission = document.getElementById("admission-status");
export let allData;

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
        console.log(allData);
        fetch_vitalsign(allData.patient_data.id);
        age.innerText = `Age: ${calculateAgeFromStrpDate(allData.patient_data.dob)} years`;
        sex.innerText = `Sex: ${allData.patient_data.sex}`;

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

const vt_header = document.getElementById("vital-sign-header");
const temp = document.getElementById("temperature");
const heart = document.getElementById("heart-rate");
const resp = document.getElementById("respiration");
const weight = document.getElementById("weight");
const spo2 = document.getElementById("spo2");
const pressure = document.getElementById("blood-pressure");


function fetch_vitalsign (patnin) {
    axios.post(`http://127.0.0.1:5000/api/v1/lastvitalsign`,
    {patient_id: patnin},
    {
    headers: {
        Authorization: 'Bearer ' + sessionStorage.getItem('healthvaultaccesstoken'),
        "Content-Type": "application/json"
        }
    })
    .then(response => {
        console.log(response.data.record);
        vt_header.innerText = `PATIENT'S VITAL SIGN ${formatDateAsAt(response.data.record.updated_at)}`;
        temp.innerHTML = `TEMPERATURE: ${response.data.record.temp}&deg;C`
        heart.innerText = `HEART_RATE: ${response.data.record.hrtbt}`
        resp.innerText = `RESPIRATION: ${response.data.record.resprt}`
        weight.innerText = `HEART_RATE: ${response.data.record.weight}kg`
        spo2.innerText = `HEART_RATE: ${response.data.record.oxygen}`
        pressure.innerText = `BLOOD-PRESUURE: ${response.data.record.systolic}/${response.data.record.diastolic}mmHg`
    })

}



function calculateAgeFromStrpDate(strpDate) {
    const currentDate = new Date();
    const birthDate = new Date(strpDate);

    const ageInMilliseconds = currentDate - birthDate;
    const ageInYears = ageInMilliseconds / (1000 * 60 * 60 * 24 * 365.25); // Consider leap years

    return Math.floor(ageInYears);
  }

  function formatDateAsAt(strpDate) {
    const date = new Date(strpDate);
    const year = date.getFullYear();
    const month = date.getMonth();
    const day = date.getDate();
    const hours = date.getHours();
    const minutes = date.getMinutes();

    const monthNames = [
      'January', 'February', 'March', 'April', 'May', 'June', 'July',
      'August', 'September', 'October', 'November', 'December'
    ];
    const monthName = monthNames[month];

    const formattedDate = `as at ${day}th ${monthName}, ${year} ${hours}:${minutes.toString().padStart(2, '0')}`;

    return formattedDate;
  }

  const strpDate = '2018-01-16T00:00:00';
  const formattedDate = formatDateAsAt(strpDate);
  console.log(formattedDate);
