<template>
    <div class="d-flex justify-content-center align-items-center w-100 flex-column">
      <welcome-screen/>
    </div>
  </template>
  <script>
  import WelcomeScreen from './store/components/WelcomeScreen.vue';
  import { mapState, mapActions } from 'vuex'

  export default {
    components: {
      WelcomeScreen,
    },
    computed: {
      ...mapState({
      }),
    },
    data() {
      return {
      };
    },
    methods: {
      ...mapActions({
      }),
    },
    mounted() {
  },
  };
  </script>
