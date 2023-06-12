const bpg = document.getElementById("bp-graph").getContext('2d');

const data ={
    labels: ['5', '4', '3', '2', '1'],
    datasets: [
        {
            label: "dias",
            data: [120, 124, 132, 129, 119],
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.2)',
            fill: false,
        },
        {
            label: "syst",
            data: [80, 87, 72, 90, 85],
            borderColor: 'rgb(54, 162, 235)',
            backgroundColor: 'rgba(54, 162, 235, 0.2)',
            fill: false,
        },
    ],
}

    const options = {
        responsive: true,
        scales: {
          x: {
            display: true,
            title: {
              display: true,
              text: 'X Axis',
            },
          },
          y: {
            display: true,
            title: {
              display: true,
              text: 'Y Axis',
            },
          },
        },
      };

      // Create the chart
      const bpgraph = new Chart(bpg, {
        type: 'line',
        data: data,
        options: options,
      });
