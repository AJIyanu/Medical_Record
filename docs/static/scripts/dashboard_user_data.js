const title = document.querySelector('title');
const welcome = document.getElementById('welcome');
const logout = document.getElementById('logout');
const hospidbold = document.getElementById('hospidbold');
const hospid = document.getElementById('hospid');
const nin = document.getElementById('nin-variable').dataset.nin;
const accessToken = sessionStorage.getItem('healthvaultaccesstoken');
const freshToken = localStorage.getItem('healthvaultfreshtoken');

const freshconfig = {
  headers: {
    Authorization: `Bearer ${freshToken}`
  }
};

const config = {
  headers: {
    Authorization: `Bearer ${accessToken}`
  }
};

const getUser = axios.create();

function refreshtoken () {
  console.log('refreshing...');
  return axios.post('http://127.0.0.1:5000/api/v1/refresh', freshcoinfig).then(response => {
    console.log(response.data);
    sessionStorage.setItem('healthvaultaccesstoken', response.data.access_token);
  });
}

getUser.interceptors.response.use(
  response => response,
  async function (error) {
    const config = error.config;
    console.log(config);
    if (error.response.status == 401) {
      console.log('jwt expired');
      await refreshtoken();
      return getUser(config);
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

logout.addEventListener('click', () => {
  sessionStorage.removeItem('healthvaultaccesstoken');
  const fresh = localStorage.getItem('healthvaultfreshtoken');
  localStorage.removeItem('healthvaultfreshtoken');

  axios.delete('http://127.0.0.1:5000/logout', config)
    .then(function (response) {
      axios.delete('http://127.0.0.1:5000/logout', freshconfig)
        .then(function (res) {
          window.location.href = '/signin';
        });
    });
});
