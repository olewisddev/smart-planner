<template>
  <transition name="fade">
    <div v-if="loading" class="loading-cover">
      <div class="spinner-border text-primary" role="status">
        <span class="visually-hidden">Loading...</span>
      </div>
    </div>
  </transition>
</template>

<script>
export default {
  name: 'LoadingTransition',
  props: {
    loading: {
      type: Boolean,
      required: true
    }
  }
}
</script>

<style scoped>
.loading-cover {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background: rgba(255, 255, 255, 0.7);
  display: flex;
  justify-content: center;
  align-items: center;
  z-index: 9999;
}

.spinner-border {
  width: 3rem;
  height: 3rem;
  border-width: 0.3em;
}

.fade-enter-active, .fade-leave-active { transition: opacity 0.8s ease; }

.fade-enter, .fade-leave-to  { opacity: 0; }
</style>
