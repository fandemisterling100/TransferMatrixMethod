<template>
    <div class="d-flex justify-content-center align-items-center w-100 flex-column">
      <welcome-screen v-if="currentPage === 'first'"/>
      <method-selection-screen v-if="currentPage === 'second'"/>
      <graph-screen v-if="currentPage === 'third'"/>
    </div>
  </template>
  <script>
  import WelcomeScreen from './store/components/WelcomeScreen.vue';
  import MethodSelectionScreen from './store/components/MethodSelectionScreen.vue';
  import GraphScreen from './store/components/GraphScreen.vue';
  import { mapState, mapActions } from 'vuex'

  export default {
    components: {
      WelcomeScreen,
      MethodSelectionScreen,
      GraphScreen,
    },
    computed: {
      ...mapState({
        currentPage: state => state.transfer.currentPage,
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
