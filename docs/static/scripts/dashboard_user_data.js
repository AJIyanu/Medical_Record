const title = document.querySelector('title');
const welcome = document.getElementById('welcome');
const logout = document.getElementById('logout');
const hospidbold = document.getElementById('hospidbold');
const hospid = document.getElementById('hospid');
const nin = document.getElementById('nin-variable').dataset.nin;
let accessToken = sessionStorage.getItem('healthvaultaccesstoken');
const freshToken = localStorage.getItem('healthvaultrefreshtoken');

const freshconfig = {
  headers: {
    Authorization: `Bearer ${freshToken}`
  }
};

let config = {
  headers: {
    Authorization: `Bearer ${accessToken}`
  }
};

const getUser = axios.create();

let count = 4;

function refreshtoken () {
  console.log('refreshing...');
  count = count - 1;
  return axios.get('http://127.0.0.1:5000/api/v1/refresh', freshconfig).then(response => {
    sessionStorage.setItem('healthvaultaccesstoken', response.data.access_token);
    accessToken = response.data.access_token;
    config = {
      headers: {
        Authorization: `Bearer ${accessToken}`
      }
    };
  });
}

getUser.interceptors.response.use(
  response => response,
  async function (error) {
    if (error.response.status == 401 && count > 1) {
      await refreshtoken();
      accessToken = sessionStorage.getItem('healthvaultaccesstoken');
      return getUser.get('http://127.0.0.1:5000/api/v1/dashboarddata/' + nin, config);
    }
    return Promise.reject(error);
  });

getUser.get('http://127.0.0.1:5000/api/v1/dashboarddata/' + nin, {
  headers: {
    Authorization: 'Bearer ' + accessToken
  }
})
  .then(function (response) {
    const userData = response.data;
    const user = userData.user;
    welcome.innerText = `${user.personality} ${user.surname} ${user.firstname}`;
    // console.log(userData);
    title.innerText = `${user.personality} ${user.surname} ${user.firstname}`;

    if (userData.institution) {
      const institution = userData.institution;
      hospid.innerText = ` - ${institution.name}`;
      hospidbold.innerText = 'You have 2 appointments here';
    } else {
      try {
      hospidbold.innerText = 'You\'re not logged into any hospital';
      } catch (err) {
        console.error(err);
      }
    }
  })
  .catch(function (error) {
    console.error(error);
    window.location.href = '/signin';
  });

logout.style.cursor = "pointer";
logout.addEventListener('click', (e) => {
  sessionStorage.removeItem('healthvaultaccesstoken');
  const fresh = localStorage.getItem('healthvaultfreshtoken');
  localStorage.removeItem('healthvaultfreshtoken');

  axios.delete('http://127.0.0.1:5000/api/v1/logout', config)
    .then(function (response) {
      sessionStorage.removeItem('healthvaultaccesstoken');
      axios.delete('http://127.0.0.1:5000/api/v1/logout', fresh)
        .then(function (res) {
          localStorage.removeItem('healthvaultrefreshtoken');
          window.location.href = '/signin';
        });
    });
});
