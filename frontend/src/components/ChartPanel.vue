<template>
  <div class="panel-container">
    <ChartCostDistribution />
  </div>
</template>

<script>
import ChartCostDistribution from './ChartCostDistribution.vue';

export default {
  name: 'ChartPanel',
  components: { ChartCostDistribution }
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
