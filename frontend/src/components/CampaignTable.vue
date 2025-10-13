<template>
  <div class="container">
    <LoadingTransition :loading="loading" />

    <transition name="fade">
      <table class="table table-sm" v-if="!loading">
        <thead>
          <tr>
            <th scope="col">Campaign</th>
            <th scope="col">Objective</th>
            <th scope="col">Buy&nbsp;Type</th>
            <th scope="col">Placement</th>
            <th scope="col">CPU</th>
            <th scope="col">Estimated KPI</th>
            <th scope="col">Cost</th>
            <th scope="col">Start Date</th>
            <th scope="col">End Date</th>
          </tr>
        </thead>
        <tbody>
          <tr v-if="loading">
            <td colspan="10" class="text-center">Loading...</td>
          </tr>

          <tr v-for="(campaign, index) in campaigns" :key="index">
            <td><i :class="getPlatformIcon(campaign.platform)"></i>&nbsp;{{ campaign['campaign-name'] }}</td>
            <td>{{ campaign.objective }}</td>
            <td>{{ campaign['buy-type'] }}</td>
            <td>{{ campaign.placement }}</td>
            <td>{{ campaign.cpu }}</td>
            <td>{{ campaign['est-kpi'] }}</td>
            <td>{{ campaign.cost }}</td>
            <td>{{ campaign.start }}</td>
            <td>{{ campaign.end }}</td>
          </tr>

          <tr v-if="campaigns.length < 10" v-for="n in 10 - campaigns.length" :key="'empty-' + n">
            <td colspan="9" class="invisible">No data</td>
          </tr>

          <tr v-if="error" class="text-danger">
            <td colspan="10" class="text-center">Error loading data: {{ errorMessage }}</td>
          </tr>
        </tbody>
      </table>
    </transition>
  </div>
</template>

<script>
import { store } from '../store.js';
import LoadingTransition from './common/LoadingTransition.vue';

export default {
  data() {
    return {
      campaigns: [],
      loading: false,
      error: false,
      errorMessage: ''
    };
  },
  computed: {
    selectedPlatform() {
      return store.selectedPlatform;
    },
    selectedObjective() {
      return store.selectedObjective;
    },
    fileUploaded() {
      return store.fileUploaded;
    }
  },
  watch: {
    selectedPlatform(newPlatform) {
      this.fetchCampaignData(newPlatform, store.selectedObjective);
    },
    selectedObjective(newObjective) {
      this.fetchCampaignData(store.selectedPlatform, newObjective);
    },
    fileUploaded() {      
      this.fetchCampaignData(store.selectedPlatform, store.selectedObjective);
    }
  },
  mounted() {
    this.fetchCampaignData(this.selectedPlatform, this.selectedObjective);
  },
  methods: {
    async fetchCampaignData(platform, objective) {      
      let url = `http://127.0.0.1:8000/api/clients/1289/campaigns`;
      
      if (platform != '') {
        url += `?platform=${platform}`;
      }
      
      if (objective != '') {
        url += platform == '' ? "?" : "&" 
        url += `objective=${objective}`;
      }

      try {
        this.loading = true;
        this.error = false;

        const response = await fetch(url);

        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }

        const data = await response.json();
        this.campaigns = data.campaigns;

        this.loading = false;
      } catch (error) {
        this.loading = false;
        this.error = true;
        this.errorMessage = error.message;
        console.error('Error fetching campaign data:', error);
      }
    },
    
    getPlatformIcon(platform) {
      switch (platform.toUpperCase()) {
        case 'FACEBOOK':
          return 'bi bi-facebook';
        case 'INSTAGRAM':
          return 'bi bi-instagram';
        case 'YOUTUBE':
          return 'bi bi-youtube';
        case 'TIKTOK':
          return 'bi bi-tiktok';
        case 'GOOGLE':
          return 'bi bi-google';
        case 'PINTEREST':
          return 'bi bi-pinterest';
        case 'LINKEDIN':
          return 'bi bi-linkedin';
        case 'TWITTER':
          return 'bi bi-twitter';
        default:
          return '';
      }
    }
  },
  components: {
    LoadingTransition
  }
};
</script>

<style scoped>
div.container {
  padding: 0;
  width: 100%;
}

table {
  margin: 0;
  font-size: 0.85rem;
}

th {
  background-color: #0E3386;
  color: white;
}


td.invisible {
  visibility: hidden;
}
</style>
