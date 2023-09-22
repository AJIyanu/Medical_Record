// get csfr token value to be used for header

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
let patient_id

const btn = document.querySelector("button");
const vsform = document.querySelector("form");
console.log(vsform);

// make a post request to submit form

btn.addEventListener("click", (e) => {
    e.preventDefault();
    submitForm(vsform);
})

function submitForm(form) {
    var url = form.action;
    var formData = new FormData();
    $(form).find("input[name]").each(function(index, node) {
      formData.append(node.name, node.value);
    });

    formData.append("patient_id", patient_id);

    $.ajax({
      url: url,
      type: "POST",
      data: formData,
      processData: false,
      contentType: false,
      headers: {
        "X-CSRF-Token": csrf
      },
      success: function(response) {
        if (response.hasOwnProperty("success")) {
            Swal.fire({
                text: response.success,
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
        } else if (response.hasOwnProperty("error")) {
            Swal.fire({
                text: "There has been an error! Either you are not authorized or an internal error. If error persist, contact administrator",
                icon: 'error',
                allowOutsideClick: false,
                showCancelButton: true,
                confirmButtonText: 'Sign in as a Nurse',
                cancelButtonText: 'Try Again'
              }).then((result) => {
                if (result.isConfirmed) {
                  window.location.href = "/dashboard/nurses";
                } else if (result.dismiss === Swal.DismissReason.cancel) {
                  window.location.href = "/vitalsign";
                }
              });
        }
      },
      error: function(xhr, status, error) {
        console.error(error);
      }
    });
  }

// get patient data neccessary for submitting form

const patient_nin = document.getElementById("ninsearch");
const patient_name = document.getElementById("pat-name");

patient_name.addEventListener("click", () => {
    patient_nin.style.display = "block";
    patient_name.style.display = "none";
})

patient_nin.addEventListener("input", () => {
    // console.log(patient_nin.value)
    if (patient_nin.value.length == 11) {
        get_patient_data(patient_nin.value);
    }
})

function get_patient_data(ninvalue) {
    let ninform = new FormData();
    ninform.append("nin", ninvalue);
    console.log(typeof(ninform));
    console.log(ninform);
    $.ajax({
        url: "http://127.0.0.1:5000/vitalsign",
        type: "POST",
        data: ninform,
        processData: false,
        contentType: false,
        headers: {
            "X-CSRF-Token": csrf
        },
        success: (response) => {
            patient_nin.style.display = "none";
            patient_name.style.display = "block";

            if (response.hasOwnProperty("error")) {
                patient_name.innerText = response.error;
                patient_name.style.color = "red";
            } else if (response.hasOwnProperty("name")) {
                patient_name.innerText = response.name;
                patient_name.style.color = "black";
                patient_id = response.pat_id;
            }
        },
        error: (error) => {
            console.error(error);
        }
    });
}
