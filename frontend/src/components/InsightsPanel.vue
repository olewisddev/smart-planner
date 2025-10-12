<template>
  <h2><i class="bi bi-lightbulb"></i>&nbsp;Insights</h2>
  <InsightsCostDistribution v-if="showChart === 'InsightsCostDistribution'" />
  <InsightsPlatformCPU v-if="showChart === 'InsightsPlatformCPU'" />
  <InsightsObjectiveCPU v-if="showChart === 'InsightsObjectiveCPU'" />
</template>

<script>
import { store } from '../store.js';
import InsightsCostDistribution from './InsightsCostDistribution.vue';
import InsightsPlatformCPU from './InsightsPlatformCPU.vue';
import InsightsObjectiveCPU from './InsightsObjectiveCPU.vue';

export default {
  components: {
    InsightsCostDistribution,
    InsightsPlatformCPU,
    InsightsObjectiveCPU
  },
  data() {
    return {
      showChart: 'InsightsCostDistribution',
    };
  },
  computed: {
    selectedPlatform() {
      return store.selectedPlatform;
    },
    selectedObjective() {
      return store.selectedObjective;
    }
  },
  watch: {
    selectedPlatform(newPlatform) {
      this.updateChart(newPlatform, this.selectedObjective);
    },
    selectedObjective(newObjective) {
      this.updateChart(this.selectedPlatform, newObjective);
    }
  },
  mounted() {
    this.updateChart(this.selectedPlatform, this.selectedObjective);
  },
  methods: {
    updateChart(platform, objective) {
      if (platform && objective) {
        this.showChart = 'InsightsPlatformCPU';
      } else if (platform && !objective) {
        this.showChart = 'InsightsPlatformCPU';
      } else if (!platform && objective) {
        this.showChart = 'InsightsObjectiveCPU';
      } else {
        this.showChart = 'InsightsCostDistribution'; // Default chart
      }
    }
  }
}
</script>


<style scoped>
h2 { margin-bottom: 1.5rem }
</style>