<template>
  <h2><i class="bi bi-lightbulb"></i>&nbsp;Insights</h2>
  <InsightsCostDistribution v-if="!store.selectedPlatform" />
  <InsightsPlatformCPU v-else />
</template>


<script>
import { store } from '../store.js';
import InsightsCostDistribution from './InsightsCostDistribution.vue';
import InsightsPlatformCPU from './InsightsPlatformCPU.vue';

export default {
  components: {
    InsightsCostDistribution,
    InsightsPlatformCPU
  },
  setup() {
    return { store };
  }
}
</script>


<style scoped>
h2 { margin-bottom: 1.5rem }
</style>