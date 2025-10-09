<template>
  <div class="cost-distribution-container">
    <label>Cost Distribution</label>
    <div><canvas ref="myChart"></canvas></div>
  </div>
</template>


<script>
export default {
  name: 'ChartCostDistribution',
  data() {
    return {
      chart: null,
      campaigns: [],
    };
  },
  mounted() {
    this.fetchCampaignData();
  },
  methods: {
    async fetchCampaignData() {
      try {
        // Call the API to fetch campaign data
        const response = await fetch(`http://127.0.0.1:8000/api/clients/1298/campaigns/costs`);
        const data = await response.json();

        // Set the campaigns data
        this.campaigns = data.campaigns;

        // Process the data for the chart
        this.createChart();
      } catch (error) {
        console.error('Error fetching campaign data:', error);
      }
    },
    createChart() {
      const labels = this.campaigns.map(campaign => campaign['campaign-name']);
      const data = this.campaigns.map(campaign => campaign['cost-value']);

      // Generate a dynamic color palette based on the number of campaigns
      const backgroundColors = this.generateColorPalette(this.campaigns.length);
      const borderColors = backgroundColors.map(color => color.replace('0.2', '1')); // Darker border colors

      this.chart = new Chart(this.$refs.myChart, {
        type: 'doughnut',
        data: {
          labels: labels,
          datasets: [
            {
              label: 'Campaign Costs',
              data: data,
              backgroundColor: backgroundColors,
              borderColor: borderColors,
              borderWidth: 1,
            },
          ],
        },
        options: {
          responsive: true,
          maintainAspectRatio: false,
          plugins: {
            legend: {
              display: false, // Disable the legend
            },
            tooltip: {
              callbacks: {
                label: (context) => {
                  return `${context.label}: ${context.raw}`;
                },
              },
            },
          },
        },
      });
    },
    generateColorPalette(num) {
      // Predefined colors
      const baseColors = [
        'rgba(255, 99, 132, 0.2)', // Red
        'rgba(54, 162, 235, 0.2)', // Blue
        'rgba(255, 205, 86, 0.2)', // Yellow
        'rgba(75, 192, 192, 0.2)', // Green
        'rgba(153, 102, 255, 0.2)', // Purple
        'rgba(255, 159, 64, 0.2)', // Orange
        'rgba(255, 99, 71, 0.2)',  // Tomato
        'rgba(0, 255, 255, 0.2)',  // Cyan
        'rgba(255, 165, 0, 0.2)',  // Dark Orange
        'rgba(128, 0, 128, 0.2)',  // Purple
      ];

      const extendedColors = [...baseColors];
      while (extendedColors.length < num) {
        extendedColors.push(`rgba(${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, ${Math.floor(Math.random() * 256)}, 0.2)`);
      }

      return extendedColors.slice(0, num);
    },
  },
  beforeDestroy() {
    if (this.chart) {
      this.chart.destroy();
    }
  },
}
</script>


<style scoped>
.cost-distribution-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  row-gap: 5px;
}
</style>