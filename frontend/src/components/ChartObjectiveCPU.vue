<template>
  <div class="chart-container">
    <h2><i class="bi bi-bar-chart-line"></i>&nbsp;Mean CPU by Objective</h2>
    <div class="canvas-container"><canvas ref="barChartCanvas"></canvas></div>
  </div>
</template>

<script>
export default {
  name: 'BarChart',
  data() {
    return {
      chart: null,
      objectives: ['brand awareness', 'engagement', 'video views', 'lead generation'],
      metrics: ['cpr', 'cpc', 'cpm', 'cpv'],
      cpuData: [],
      metricColors: {
        'cpr': 'rgba(75, 192, 192, 0.5)',
        'cpc': 'rgba(255, 99, 132, 0.5)',
        'cpm': 'rgba(54, 162, 235, 0.5)',
        'cpv': 'rgba(153, 102, 255, 0.5)'
      },
    };
  },
  methods: {
    async fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/clients/1289/metrics/cpu?group-by=objective');
        
        // Check if the response is OK (status 200)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();

        this.cpuData = this.objectives.map(objective => {
          const objectiveData = data[objective] || {};

          return this.metrics.map(metric => {
            return objectiveData[metric] ? objectiveData[metric].mean : 0;
          });
        });

        this.initChart();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    initChart() {
      const ctx = this.$refs.barChartCanvas.getContext('2d');

      const datasets = this.metrics.map((metric, index) => ({
        label: metric.toUpperCase(),
        data: this.cpuData.map(data => data[index]),
        backgroundColor: this.metricColors[metric],
        borderColor: this.metricColors[metric].replace('0.5', '1'),
        borderWidth: 1,
      }));

      this.chart = new window.Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.objectives.map(objective => objective.charAt(0).toUpperCase() + objective.slice(1)),
          datasets: datasets,
        },
        options: {
          responsive: true,
          indexAxis: 'y',
          plugins: {
            legend: {
              position: 'top',
            },
          },
          scales: {
            x: {
              beginAtZero: true,
            },
            y: {
              stacked: false,
            },
          },
          barPercentage: 2.0,
          categoryPercentage: 0.5,
        },
      });
    },
  },
  mounted() {
    this.fetchData();
  },
  beforeUnmount() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
};
</script>

<style scoped>
canvas {
  max-width: 100%;
  display: block;
}

.canvas-container {
  flex-grow: 1;
  display: flex;
  justify-content: center;
  align-items: center;
}
</style>
