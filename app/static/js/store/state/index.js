import Vue from 'vue'
import Vuex from 'vuex'
import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

const debug = true;

export default new Vuex.Store({
  modules: {
  },
  strict: debug,
  plugins: [
    createPersistedState({
      paths: [],
    }),
],
})