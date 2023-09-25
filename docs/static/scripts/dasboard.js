let userData = document.getElementById('all-data').getAttribute('data-user')
const cards = document.querySelectorAll(".cards");
let diastolic = []
let systolic = []
let DateTime = []

userData = JSON.parse(userData);
console.log(userData.record)
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


const newRow = function (rowData) {
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
  doctorP.textContent = rowData.doctor;
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
  var prescriptionP = document.createElement('p');
  prescriptionP.textContent = rowData.prescription;
  prescriptionDiv.appendChild(prescriptionP);
  row.appendChild(prescriptionDiv);

  const container = document.querySelector('.report');
  container.appendChild(row);
   console.log("function called and done");
}
