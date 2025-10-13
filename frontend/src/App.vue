<script setup>
import CampaignTablePanel from './components/CampaignTablePanel.vue';
import ChartPanel from './components/ChartPanel.vue';
import InsightsPanel from './components/InsightsPanel.vue';
</script>

<template>
  <div class="app-container">
    <div class="card top-card shadow-lg">
      <CampaignTablePanel />
    </div>

    <div class="card bottom-left-card shadow-lg">
      <ChartPanel />
    </div>

    <div class="card bottom-right-card shadow-lg">
      <InsightsPanel />
    </div>
  </div>
</template>

<style>
html {
  font-size: 12px;
}

body {
  font-size: 1rem;
  background-color: #005A9C;
}

h2 {
  font-size: 1.40rem;
  font-weight: bold; 
  color: #0E3386; 
}

li { font-size: 1.20rem; }

.app-container {
  display: grid;
  height: 100vh;
  max-width: 910px;
  margin: 0 auto;
  
  /* GRID LAYOUT */
  grid-template-columns: 1fr 1fr;
  grid-template-rows: 1fr 1fr;
  gap: 20px;
  padding: 20px;
  box-sizing: border-box;
}

.card {
  border-radius: 8px;
  border: none;
  height: 100%;
  padding: 1.5rem;
}

/* CARD LAYOUT */
.top-card {
  grid-column: span 2;
  grid-row: 1 / 2;
}

.bottom-left-card {
  grid-column: 1 / 2;
  grid-row: 2 / 3;
}

.bottom-right-card {
  grid-column: 2 / 3;
  grid-row: 2 / 3;
}
</style>
