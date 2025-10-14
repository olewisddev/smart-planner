<template>
  <div class="panel-container">
    <ChartCostDistribution v-if="showChart === 'ChartCostDistribution'" />
    <ChartPlatformCPU v-if="showChart === 'ChartPlatformCPU'" />
    <ChartObjectiveCPU v-if="showChart === 'ChartObjectiveCPU'" />
  </div>
</template>

<script>
import { store } from '../store.js';
import ChartCostDistribution from './ChartCostDistribution.vue';
import ChartPlatformCPU from './ChartPlatformCPU.vue';
import ChartObjectiveCPU from './ChartObjectiveCPU.vue';

export default {
  name: 'ChartPanel',
  components: { 
    ChartCostDistribution,
    ChartPlatformCPU,
    ChartObjectiveCPU
  },
  data() {
    return {
      showChart: 'ChartCostDistribution', // Default chart
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
    // Initialize the chart when the component is mounted
    this.updateChart(this.selectedPlatform, this.selectedObjective);
  },
  methods: {
    // Update the chart based on the selected platform and objective
    updateChart(platform, objective) {
      // If both are selected, don't change the chart
      if (platform && objective) return;

      if (platform && !objective) {
        this.showChart = 'ChartPlatformCPU';
      } else if (!platform && objective) {
        this.showChart = 'ChartObjectiveCPU';
      } else {
        this.showChart = 'ChartCostDistribution';
      }
    }
  }
}
</script>

<style scoped>
.panel-container { height: 100%; }

.chart-container {
  display: flex;
  flex-direction: column;
  height: 100%;
  justify-content: flex-start; 
}

</style>
