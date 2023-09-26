let userData = document.getElementById('all-data').getAttribute('data-user')
const cards = document.querySelectorAll(".cards");
let diastolic = []
let systolic = []
let DateTime = []

userData = JSON.parse(userData);
// console.log(userData.record)


// BLOOD PRESSURE DATA AND GRAPH
const bpData = userData.vitalsign
if (bpData !== undefined) {
  bpData.forEach((vts) => {
    diastolic.push(vts.diastolic);
    systolic.push(vts.systolic);
    const date = new Date(Date.parse(vts.updated_at));
    const options = { weekday: 'short', day: 'numeric', month: 'short', year: 'numeric', hour: 'numeric', minute: 'numeric' };
    DateTime.push(date.toLocaleString('en-US', options))
  })

  const xValues = DateTime.reverse()

  new Chart("myChart", {
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

// console.log(bpData);
// console.log(systolic)
// console.log(diastolic)
// console.log(DateTime)


// THE DASHBOARD CARD LINKS
cards.forEach((card) => {
    card.addEventListener("click", () => {
        if (card.id == "bookme") {
            window.location.href = "https://calendly.com/app/login"
        }
        if (card.id == "findhealth") {
            window.location.href = "https://www.google.com/search?q=nearest+hospital%2C+heath+service"
        }
        if (card.id == "finddrug") {
            window.location.href = "https://medplusnig.com/"
        }
        if (card.id == "ai") {
            window.location.href = "https://chat.openai.com/"
        }
        if (card.id == "casefile") {
            window.location.href = "/casefile"
        }
        if (card.id == "vitalsign") {
            window.location.href = "/vitalsign"
        }
        if (card.id == "medscape") {
            window.location.href = "https://reference.medscape.com/drug-interactionchecker"
        }
        if (card.id == "precord") {
            window.location.href = ""
        }
    })
})
// console.log(userData);


// CASEFILE TABLE CONSTRUCT

const casefileData = userData.record;

if (casefileData  !== undefined ) {
  if (casefileData.length !== 0) {
    casefileData.forEach((rowData) => {
      newRow(rowData);
    })
    createLastPrescription(JSON.parse(casefileData[0].prescription))
    let lastRow = document.querySelectorAll(".row")
    lastRow = lastRow[lastRow.length - 1]
    lastRow.style.borderBottom = "2px solid";
    lastRow.style.borderBottomLeftRadius = "7px"
    lastRow.style.borderBottomRightRadius = "7px"
  } else {
    document.querySelector(".title").style.display = 'none';
    document.querySelector('.no-data').style.display = 'block';
  }
} else {
  document.querySelector(".title").style.display = 'none';
  document.querySelector('.no-data').style.display = 'block';
}

function newRow (rowData) {
  const row = document.createElement('div');
  row.className = 'row';

  const dateDiv = document.createElement('div');
  dateDiv.className = 'date';
  const dateP = document.createElement('p');
  dateP.textContent = rowData.date;
  dateDiv.appendChild(dateP);
  row.appendChild(dateDiv);

  const doctorDiv = document.createElement('div');
  doctorDiv.className = 'doctor';
  const doctorP = document.createElement('p');
  doctorP.textContent = rowData.name;
  doctorDiv.appendChild(doctorP);
  row.appendChild(doctorDiv);

  const diagnosisDiv = document.createElement('div');
  diagnosisDiv.className = 'diagnosis';
  const diagnosisP = document.createElement('p');
  diagnosisP.textContent = rowData.diagnosis;
  diagnosisDiv.appendChild(diagnosisP);
  row.appendChild(diagnosisDiv);

  const prescriptionDiv = document.createElement('div');
  prescriptionDiv.className = 'prescribe';
  const prescriptionUL = document.createElement('ul');

  const prescribeME = JSON.parse(rowData.prescription);
  prescribeME.forEach((prescribe) => {
    const adj = `<li><b><i>Drug:</i></b> ${prescribe.drug},<br><b><i>Dosage:</i></b> ${prescribe.dosage}<br><b><i>To be used for:</i></b> ${prescribe.days} days`
    prescriptionUL.insertAdjacentHTML("beforeend", adj)
  })
  // prescriptionP.textContent = rowData.prescription;
  prescriptionDiv.appendChild(prescriptionUL);
  row.appendChild(prescriptionDiv);

  const container = document.querySelector('.report');
  container.appendChild(row);
  //  console.log("function called and done");
}

function createLastPrescription (presObj) {
  // console.log(presObj);
  const prescrip = document.querySelector('.drugs');
  const dList = document.createElement('ul');
  presObj.forEach((drug) => {
    const adj = `<li><b><i>Drug:</i></b> ${drug.drug},<br><b><i>Dosage:</i></b> ${drug.dosage}<br><b><i>To be used for:</i></b> ${drug.days} days`
    prescrip.insertAdjacentHTML("beforeend", adj)
  })
  prescrip.appendChild(dList)
}
