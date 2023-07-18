const title = document.querySelector('title');
const welcome = document.getElementById('welcome');
const logout = document.getElementById('logout');
const hospidbold = document.getElementById('hospidbold');
const hospid = document.getElementById('hospid');

let count = 4;

while (count !== 0) {
  const accessToken = sessionStorage.getItem('healthvaultaccesstoken');
  const nin = document.getElementById('nin-variable').dataset.nin;

  axios.get('http://127.0.0.1:5000/api/v1/dashboarddata/' + nin, {
    headers: {
      Authorization: 'Bearer ' + accessToken
    }
  })
    .then(function (response) {
      const userData = response.data;
      const user = userData.user;
      welcome.innerText = `${user.personality} ${user.surname} ${user.firstname}`;
      console.log(userData);
      title.innerText = `${user.personality} ${user.surname} ${user.firstname}`;

      if (userData.institution) {
        const institution = userData.institution;
        hospid.innerText = ` - ${institution.name}`;
        hospidbold.innerText = 'You have 2 appointments here';
      } else {
        hospidbold.innerText = 'You\'re not logged into any hospital';
      }
    })
    .catch(function (error) {
      console.error(error);
    });
  count = count - 1;
}

logout.addEventListener('click', () => {
  sessionStorage.removeItem('healthvaultaccesstoken');
  const fresh = localStorage.getItem('healthvaultfreshtoken');
  localStorage.removeItem('healthvaultfreshtoken');

  const freshconfig = {
    headers: {
      Authorization: `Bearer ${fresh}`
    }
  };

  const config = {
    headers: {
      Authorization: `Bearer ${accessToken}`
    }
  };

  axios.delete('http://127.0.0.1:5000/logout', config)
    .then(function (response) {
      axios.delete('http://127.0.0.1:5000/logout', freshconfig)
        .then(function (res) {
          window.location.href = '/signin';
        });
    });
});
