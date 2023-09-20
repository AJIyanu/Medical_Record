let userData = document.getElementById('all-data').getAttribute('data-user')
const cards = document.querySelectorAll(".cards");
// const title = document.querySelector("title");

userData = JSON.parse(userData);
console.log(userData);

// title.innerText = `Dashboard - `


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
            window.location.href = "/casefile.html"
        }
        if (card.id == "vitalsign") {
            window.location.href = "/vitalsign.html"
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


const test_data = [
    {
        date: '2-3-2021',
        doctor: 'Doctor Rihanna Titilayo',
        diagnosis: 'Malaria',
        prescription: 'Paracetamol'
      },
      {
        date: '2-3-2021',
        doctor: 'Doctor Rihanna Titilayo',
        diagnosis: 'Malaria',
        prescription: 'Paracetamol'
      },
      {
        date: '2-3-2021',
        doctor: 'Doctor Rihanna Titilayo',
        diagnosis: 'Malaria',
        prescription: 'Paracetamol'
      }
]

test_data.forEach((user) => {
    newRow(user);
})
