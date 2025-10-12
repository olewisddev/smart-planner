<template>
  <div>
    <button class="btn btn-primary btn-sm" @click="triggerFileInput">
      <i class="bi bi-upload"></i> Upload CSV
    </button> 
    <!-- Hidden input element --> 
    <input ref="fileInput" type="file" class="d-none" @change="handleFileUpload" />
  </div>
</template>

<script>
import { store } from '../store.js';

export default {
  watch: {
    fileUploaded() {
      store.selectedPlatform = '',
      store.selectedObjective = ''
    }
  },
  computed: {
    fileUploaded() {
      return store.fileUploaded;
    }
  },  
  methods: {
    triggerFileInput() {
      // Simulate input click
      this.$refs.fileInput.click();
    },
    async handleFileUpload(event) {
      const file = event.target.files[0];
      if (file) {
        // Input validation
        if (!file.name.endsWith('.csv')) {
          alert('Please upload a CSV file.');
          return;
        }

        const formData = new FormData();
        formData.append('file', file);

        try {
          const response = await fetch('http://127.0.0.1:8000/api/clients/1289/campaigns', {
            method: 'POST',
            body: formData,
          });

          
          if (!response.ok) {
            throw new Error(`File upload failed with status ${response.status}`);
          }

          const result = await response.json();
          console.log('File uploaded successfully:', result);
          
          store.fileUploaded = !store.fileUploaded;
          alert('File uploaded successfully!');
        } catch (error) {
          alert('Failed to upload the file. Please try again.');
        }
      }
    }
  }
}
</script>


<style scoped>
</style>
