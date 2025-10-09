<script setup>
import CampaignTablePanel from './components/CampaignTablePanel.vue';
import ChartPanel from './components/ChartPanel.vue';
</script>

<template>
  <div class="container">
    <CampaignTablePanel />
    <ChartPanel />
  </div>
</template>

<style scoped>
.container {
  width: 95%;
}
</style>
