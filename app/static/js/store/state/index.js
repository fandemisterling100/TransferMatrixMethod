import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import transfer from './modules/transfer';

Vue.use(Vuex)

const debug = true;

// We make available all the values on the state of the file transfer.js
// as well as the actions and mutations to use them from differente .vue files
export default new Vuex.Store({
  modules: {
    transfer,
  },
  strict: debug,
  plugins: [
    createPersistedState({
      paths: [],
    }),
],
})