<template>
  <div class="container">
    <LoadingTransition :loading="loading" />

    <transition-group name="fade" tag="ul">
      <li v-for="(insight, index) in insights" :key="index">{{ insight }}</li>
    </transition-group>
  </div>
</template>

<script>
import { store } from '../store.js';
import LoadingTransition from './common/LoadingTransition.vue';

export default {  
  components: { LoadingTransition },
  data() {
    return {
      insights: [],
      loading: false
    };
  },
  computed: {
    selectedPlatform() {
      return store.selectedPlatform;
    }
  },
  watch: {
    selectedPlatform(newPlatform) {
      this.fetchCampaignData(newPlatform);
    }
  },
  mounted() {
    this.fetchCampaignData(this.selectedPlatform);
  },
  methods: {
    async fetchCampaignData(newPlatform) {
      try {
        this.loading = true;
        const response = await fetch(`http://127.0.0.1:8000/api/clients/1298/campaigns/insights/platforms/${newPlatform}`);
        const data = await response.json();
        
        this.insights = data.insights || [];
        this.loading = false;
      } catch (error) {
        console.error('Error fetching campaign data:', error);
        this.loading = false;
      }
    }
  }
};
</script>

<style scoped>
li { font-size: 1.5rem; }
</style>
