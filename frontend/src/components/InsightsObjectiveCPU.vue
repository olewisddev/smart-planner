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
    selectedObjective() {
      return store.selectedObjective;
    }
  },
  watch: {
    selectedObjective(newObjective) {
      this.fetchCampaignData(newObjective);
    }
  },
  mounted() {
    this.fetchCampaignData(this.selectedObjective);
  },
  methods: {
    async fetchCampaignData(newObjective) {
      try {
        this.loading = true;
        const response = await fetch(`http://127.0.0.1:8000/api/clients/1298/campaigns/insights/objectives/${newObjective}`);
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
</style>
