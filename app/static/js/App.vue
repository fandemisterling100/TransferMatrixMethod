<template>
  <!-- Main container of the three possible screens (initial or welcome, methods selection and graphs screen) -->
    <div class="d-flex justify-content-center align-items-center w-100 flex-column">
      <welcome-screen v-if="currentPage === 'first'"/>
      <method-selection-screen v-if="currentPage === 'second'"/>
      <graph-screen v-if="currentPage === 'third'"/>
      <experimental-data v-if="currentPage === 'fourth'"/>
      <loading-pop-up/>
    </div>
  </template>
  <script>
  import WelcomeScreen from './store/components/WelcomeScreen.vue';
  import MethodSelectionScreen from './store/components/MethodSelectionScreen.vue';
  import GraphScreen from './store/components/GraphScreen.vue';
  import ExperimentalData from './store/components/ExperimentalData.vue';
  import { mapState, mapActions } from 'vuex'
  import LoadingPopUp from './store/components/LoadingPopUp.vue';

  export default {
    components: {
      WelcomeScreen,
      MethodSelectionScreen,
      GraphScreen,
      ExperimentalData,
      LoadingPopUp,
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
