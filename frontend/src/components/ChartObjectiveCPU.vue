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
      data: [],
      labels: [],
      colors: [
        'rgba(255, 99, 132, 0.5)', // Red
        'rgba(54, 162, 235, 0.5)', // Blue
        'rgba(255, 206, 86, 0.5)', // Yellow
        'rgba(75, 192, 192, 0.5)', // Green
        'rgba(153, 102, 255, 0.5)', // Purple
        'rgba(255, 159, 64, 0.5)', // Orange
      ],
    };
  },
  methods: {
    // Fetch data from the API endpoint using fetch
    async fetchData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/clients/1289/campaigns/stats/cpu-per-objective');
        const data = await response.json();

        this.labels = Object.keys(data);
        this.data = this.labels.map(label => data[label].mean_cpu);

        // Initialize the chart once the data is fetched
        this.initChart();
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    },

    initChart() {
      const ctx = this.$refs.barChartCanvas.getContext('2d');

      const backgroundColors = this.colors.slice(0, this.labels.length);

      this.chart = new window.Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.labels,
          datasets: [
            {
              label: 'CPU Usage (Mean)',
              data: this.data,
              backgroundColor: backgroundColors,
              borderColor: backgroundColors.map(color => color.replace('0.5', '1')),
              borderWidth: 1,
            },
          ],
        },
        options: {
          indexAxis: 'y',
          responsive: true,
          plugins: {
            legend: {
              display: false,
            },
          },
          scales: {
            x: {
              beginAtZero: true,
            },
          },
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
