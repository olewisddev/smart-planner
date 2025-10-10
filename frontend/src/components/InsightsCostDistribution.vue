<template>
  <ul>
    <li v-for="(insight, index) in insights" :key="index">{{ insight }}</li>
  </ul>
</template>

<script>
export default {
  data() {
    return {
      insights: []
    };
  },
  mounted() {
    this.fetchCampaignData();
  },
  methods: {
    async fetchCampaignData() {
      try {
        const response = await fetch('http://127.0.0.1:8000/api/clients/1298/campaigns/insights');
        const data = await response.json();
        
        // Store the insights array directly
        this.insights = data.insights || [];
      } catch (error) {
        console.error('Error fetching campaign data:', error);
      }
    }
  }
};
</script>

<style scoped>
li { font-size: 1.5rem; }
</style>
