<template>
  <div class="panel-container">
    <!-- Conditionally render components based on selectedPlatform -->
    <ChartCostDistribution v-if="!store.selectedPlatform" />
    <ChartMeanCPU v-else />
  </div>
</template>

<script>
import { store } from '../store.js';
import ChartCostDistribution from './ChartCostDistribution.vue';
import ChartMeanCPU from './ChartMeanCPU.vue';

export default {
  name: 'ChartPanel',
  components: { 
    ChartCostDistribution,
    ChartMeanCPU
  },
  setup() {
    return { store };
  }
}
</script>

<style scoped>
.panel-container {
  width: 50%;
  padding: 15px;
  border: 1px solid #000000;
  margin: 10px 0;
}
</style>
