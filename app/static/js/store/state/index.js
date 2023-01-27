import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";
import transfer from './modules/transfer';

Vue.use(Vuex)

const debug = true;

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