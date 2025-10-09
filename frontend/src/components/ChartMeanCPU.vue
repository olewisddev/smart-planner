<template>
  <div>
    <canvas ref="barCanvas"></canvas>
  </div>
</template>

<script>
export default {
  name: 'BarChart',
  data() {
    return {
      chart: null,
      platforms: ['FACEBOOK', 'INSTAGRAM', 'YOUTUBE', 'TIKTOK'],
      cpuCostData: [],
      colors: [
        'rgba(75, 192, 192, 0.5)',  // Facebook
        'rgba(255, 99, 132, 0.5)',  // Instagram
        'rgba(54, 162, 235, 0.5)',  // YouTube
        'rgba(153, 102, 255, 0.5)'  // TikTok
      ],
    };
  },
  mounted() {
    this.fetchCpuStats();
  },
  methods: {
    async fetchCpuStats() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/clients/1289/campaigns/stats/cpu-per-platform');
        
        // Check if the response is OK (status 200)
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        
        // Extract the cost (mean_cpu) for each platform
        this.cpuCostData = this.platforms.map(platform => data[platform]?.mean_cpu || 0);
        
        // Create the chart after data is fetched
        this.createChart();
      } catch (error) {
        console.error('Error fetching CPU stats:', error);
      }
    },
    createChart() {
      const ctx = this.$refs.barCanvas.getContext('2d');
      
      
      this.chart = new Chart(ctx, {
        type: 'bar',
        data: {
          labels: this.platforms,
          datasets: [{
            label: 'Mean CPU',
            data: this.cpuCostData,
            backgroundColor: this.colors,
            borderColor: this.colors.map(color => color.replace('0.5', '1')),
            borderWidth: 1
          }]
        },
        options: {
          responsive: true,
          plugins: {
            title: {
              display: true,
              text: 'Mean CPU by Platform'
            },
            legend: {
              display: false
            }
          },
          scales: {
            y: {
              beginAtZero: true,
              title: {
                display: true,
                text: 'CPU'
              }
            }
          }
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
</style>
