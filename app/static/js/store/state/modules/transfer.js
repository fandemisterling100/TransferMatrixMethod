import Api from '../../utils/api'

// initial state
const state = ({
  currentPage: "first",
  type: null,
})

// getters
const getters = {}

// actions
const actions = {
}

// mutations
const mutations = {
  setCurrentPage (state, value) {
    state.currentPage = value
  },
  setType (state, value) {
    state.type = value
  },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
