<template>
  <div class="panel-container">
    <select 
      class="form-select form-select-sm platform-select" 
      v-model="selectedPlatform"
      @change="updateSelectedPlatform"
    >
      <option value="" selected>Select platform...</option>
      <option value="facebook">Facebook</option>
      <option value="instagram">Instagram</option>
      <option value="youtube">Youtube</option>
      <option value="tiktok">Tiktok</option>
    </select>
    <CampaignTable />
  </div>
</template>


<script>
import { store } from '../store.js';
import CampaignTable from './CampaignTable.vue';

export default {
  name: 'CampaignTablePanel',
  components: {
    CampaignTable
  },
  computed: {
    selectedPlatform: {
      get() {
        return store.selectedPlatform;
      },
      set(value) {
        store.selectedPlatform = value;
      }
    }
  },
  methods: {
    updateSelectedPlatform() {
      if (this.selectedPlatform === '') {
        store.selectedPlatform = '';
      }
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

.form-select-sm {
  width: 25%;
}

</style>
