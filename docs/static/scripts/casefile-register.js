import { tags } from "./casefile-taginput.js";
// import { allData } from "./casefile-api-data.js";
const form = document.querySelector('form');
const searchPat = document.getElementById("search-patient");
const submit = document.querySelector('button.submit-btn');
const displayName = document.querySelector('h3.patient-name');
const errorDisplay = document.getElementById("error");
const addDrug = document.getElementById("add-drug");
let patient_id
let diastolic = [];
let systolic = [];
let DateTime = [];
let drugs = [];

// let staffData;

// GET CSRF TOKEN

const getCookies = function () {
  const pairs = document.cookie.split(";");
  let cookies = {};
  for (let i = 0; i < pairs.length; i++) {
    const pair = pairs[i].split("=");
    cookies[(pair[0] + "").trim()] = unescape(pair.slice(1).join("="));
  }
  return cookies;
};

const getCookieValue = function (cookieName) {
const cookies = getCookies();
return cookies[cookieName];
};

const csrf = getCookieValue('csrf_access_token');

// GET PATIENT DETAILS

searchPat.addEventListener("input", () => {
  if (searchPat.value.length == 11) {
    let search = new FormData();
    search.append("nin", searchPat.value);

    $.ajax({
      url: "/casefile",
      type: "POST",
      data: search,
      headers: {
        "X-CSRF-Token": csrf
      },
      processData: false,
      contentType: false,
      success: (response) => {
        console.log(response)
        if (response.hasOwnProperty("error")) {
          errorDisplay.style.display = 'block';
          searchPat.style.display = 'none';
          errorDisplay.innerText = response.error;
        } else {
          displayName.style.display = 'block';
          searchPat.style.display = 'none';
          displayName.innerText = response.name;
          patient_id = response.pat_id;
        }

        // Fill in Patient's Details

        fillPatientDetails(response.patientdata, response.vitalsign[0]);


        // CREATE CHARTS FOR BP

  const bpData = response.vitalsign
  if (bpData !== undefined) {
    bpData.forEach((vts) => {
      console.log(vts)
      diastolic.push(vts.diastolic);
      systolic.push(vts.systolic);
      const date = new Date(Date.parse(vts.updated_at));
      const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', hour: 'numeric', minute: 'numeric' };
      DateTime.push(date.toLocaleString('en-US', options))
    })

    const xValues = DateTime.reverse()

    new Chart("bp-graph", {
      type: "line",
      data: {
        datasets: [{
          data: diastolic.reverse(),
          borderColor: "blue",
          label: "Diastolic",
          fill: true,
          backgroundColor: "rgba(255,255,255,1)",
        },{
          data: systolic.reverse(),
          borderColor: "green",
          fill: true,
          backgroundColor: "#B8F0F0",
          label: "Systolic"
        }],
        labels: xValues
      },
      options: {
        // legend: {display: true},
        scales: {
            x: {
                scaleLabel: {
                  display: true,
                  text: 'Date and Time'
                }
              },
            y: {
              beginAtZero: true,
              scaleLabel: {
                display: true,
                text: 'Pressure (mmHg)'
              }
            }
          }
        }
      });
  }

      },
      error: (error) => {console.error(error)}
    })
  }
})


// ADD DRUGS

addDrug.addEventListener("click", (e) => {
  e.preventDefault();
  drugs.push({
    drug: document.getElementById('drug').value,
    dosage: document.getElementById("dosage").value,
    days: document.getElementById("days").value
  })

  document.getElementById("drug").value = "";
  document.getElementById("days").value = "";
  document.getElementById("dosage").value = "";

  // console.log(drugs);
})


// CHANGE DISPLAY

displayName.addEventListener('click', function() {
    displayName.style.display = 'none';
    searchPat.style.display = 'block';
})

errorDisplay.addEventListener('click', () => {
    errorDisplay.style.display = 'none';
    searchPat.style.display = 'block';
})

// SUBMIT FORM

submit.addEventListener("click", (register) => {
    register.preventDefault();
    if (patient_id !== undefined) {
      submitForm(form);
    }
})

function submitForm(form) {
  const url = form.action;
  let formdata = new FormData();

  $(form).find("input[name]").each((index, node) => {
    formdata.append(node.name, node.value);
  })
  $(form).find("textarea[name]").each((index, node) => {
    formdata.append(node.name, node.value);
  })

  formdata.append("symptoms", tags);
  formdata.append("prescription", JSON.stringify(drugs))
  formdata.append("patient_id", patient_id);

  $.ajax({
    url: url,
    data: formdata,
    type: "POST",
    processData: false,
    contentType:false,
    headers: {
      "X-CSRF-Token": csrf
    },
    success: (response) => {
      console.log(response);
    },
    error: (error) => {
      console.error(error);
    }
  })
}


// FUNCTIONS TO FILL IN PATIENT's DETAILS AND LAST VT

function fillPatientDetails (patientObject, vitalsign) {
  document.getElementById("age").innerText = `AGE: ${calculateAge(patientObject.age)} Years`
  document.getElementById("sex").innerText = `Sex: ${patientObject.sex}`
  document.getElementById("vital-sign-header").innerText = `Latest Vital Sign as at ${formatDate(vitalsign.updated_at)}`
  document.getElementById("temperature").innerHTML = `TEMPERATURE: ${vitalsign.temp} &deg;C`
  document.getElementById("heart-rate").innerText = `HEART_RATE: ${vitalsign.hrtbt} PER MINUTE`
  document.getElementById("respiration").innerText = `RESPIRATION: ${vitalsign.resprt}`
  document.getElementById("weight").innerText = `WEIGT: ${vitalsign.weight} KG`
  document.getElementById("blood-pressure").innerText = `BLOOD-PRESSURE: ${vitalsign.systolic}/${vitalsign.diastolic}mmHg`
  document.getElementById("spo2").innerText = `SPO2: ${vitalsign.oxygen}`
}


function calculateAge(dateOfBirth) {
  const dob = new Date(dateOfBirth);
  const today = new Date();

  const yearsDiff = today.getFullYear() - dob.getFullYear();
  const monthsDiff = today.getMonth() - dob.getMonth();
  const daysDiff = today.getDate() - dob.getDate();

  // Check if the birthday for this year has not occurred yet
  if (monthsDiff < 0 || (monthsDiff === 0 && daysDiff < 0)) {
    return yearsDiff - 1;
  } else {
    return yearsDiff;
  }
}


function formatDate(inputDate) {
  const months = [
    "Jan", "Feb", "Mar", "Apr", "May", "Jun",
    "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"
  ];

  const date = new Date(inputDate);
  const month = months[date.getMonth()];
  const day = date.getDate();
  const year = date.getFullYear();
  const hours = date.getHours();
  const minutes = date.getMinutes();
  const ampm = hours >= 12 ? 'pm' : 'am';
  const formattedHours = hours % 12 === 0 ? 12 : hours % 12;
  const formattedMinutes = minutes < 10 ? '0' + minutes : minutes;

  const formattedDate = `${month} ${day}, ${year} at ${formattedHours}:${formattedMinutes} ${ampm}`;
  return formattedDate;
}
