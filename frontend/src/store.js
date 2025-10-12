import { reactive } from 'vue'

export const store = reactive({
  selectedPlatform: '',
  selectedObjective: '',
  fileUploaded: false
})