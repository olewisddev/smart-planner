<template>
  <div class="chart-container">
    <h2><i class="bi bi-bar-chart-line"></i>&nbsp;Mean CPU by Platform</h2>
    <div class="canvas-container"><canvas ref="barCanvas"></canvas></div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      chart: null,
      platforms: ['facebook', 'instagram', 'youtube', 'tiktok'],
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
  mounted() {
    this.fetchCpuStats();
  },
  methods: {
    async fetchCpuStats() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/clients/1289/metrics/cpu?group-by=platform');
        
        // Check if the response is OK (status 200)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        this.cpuData = this.platforms.map(platform => {
          const platformData = data[platform] || {};

          const metricsData = this.metrics.map(metric => {
            return platformData[metric] ? platformData[metric].mean : 0;
          });

          return metricsData;
        });

        this.createChart();
      } catch (error) {
        console.error('Error fetching CPU stats:', error);
      }
    },
    createChart() {
      const ctx = this.$refs.barCanvas.getContext('2d');
      
      const datasets = this.metrics.map((metric, metricIndex) => ({
        label: metric.toUpperCase(),
        data: this.cpuData.map(data => data[metricIndex]),
        backgroundColor: this.metricColors[metric],
        borderColor: this.metricColors[metric].replace('0.5', '1'),
        borderWidth: 1
      }));

      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.platforms.map(platform => platform.charAt(0).toUpperCase() + platform.slice(1)),
          datasets: datasets
        },
        options: {
          responsive: true,
          plugins: {
            legend: {
              position: 'top'
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'Mean Value'
              }
            }
          },
        }
      });
    }
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy();
    }
  }
};
</script>

<style scoped>
.canvas-container {
  flex-grow: 1; /* Take up remaining space */
  display: flex; /* Use Flexbox in this container */
  justify-content: center; /* Center the canvas horizontally */
  align-items: center; /* Center the canvas vertically */
}
</style>
