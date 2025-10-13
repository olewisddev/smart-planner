<template>
  <div class="panel-container">
    <h2>Brewtopia Coffee House</h2>
    <div class="controls-container">
      <div class="filters-container">
        <select 
          class="form-select platform-select" 
          v-model="selectedPlatform"
          @change="updateSelectedPlatform"
        >    
          <option value="" selected>Select platform...</option>
          <option value="facebook">Facebook</option>
          <option value="instagram">Instagram</option>
          <option value="youtube">Youtube</option>
          <option value="tiktok">Tiktok</option>
        </select>
        <select class="form-select" v-model="selectedObjective">
          <option value="" selected>Select objective...</option>
          <option value="video views">Video views</option>
          <option value="brand awareness">Brand awareness</option>
          <option value="engagement">Engagement</option>
          <option value="lead generation">Lead generation</option>
        </select>
        <button type="button" class="btn btn-outline-secondary" @click="handleClearClicked">
          Clear
        </button>
      </div>
      <UploadButton />
    </div>
    <CampaignTable />
  </div>
</template>


<script>
import { store } from '../store.js';
import CampaignTable from './CampaignTable.vue';
import UploadButton from './UploadButton.vue';

export default {
  name: 'CampaignTablePanel',
  components: {
    CampaignTable,
    UploadButton
  },
  computed: {
    selectedPlatform: {
      get() {
        return store.selectedPlatform;
      },
      set(value) {
        store.selectedPlatform = value;
      }
    },
    selectedObjective: {
      get() { 
        return store.selectedObjective; 
      },
      set(value) { 
        return store.selectedObjective = value; 
      }
    }
  },
  methods: {
    updateSelectedPlatform() {
      if (this.selectedPlatform === '') {
        store.selectedPlatform = '';
      }
    },
    handleClearClicked() {
      store.selectedPlatform = '';
      store.selectedObjective = '';
    }
  }
}
</script>


<style scoped>
.panel-container {
  display: flex;
  flex-direction: column;
  row-gap: 10px;
}

.form-select {
  width: 20%;
}

.controls-container {
  display: flex;
  justify-content: space-between;
}

.filters-container {
  display: flex;
  column-gap: 0.5rem;
  flex-grow: 1;
}
</style>
