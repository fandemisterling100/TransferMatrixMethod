import Api from '../../utils/api'

// initial state
const state = ({
  currentPage: "first",
  type: null,
  isLoadingResult: false,
})

// getters
const getters = {}

// actions
const actions = {
  sendData({ commit, state }, data) {
    let url = `/api/v1/transfer-method/`
    commit('toggleLoadingResult', true)
    data.append("answer", state.type)

    return Api.post(url, data).then((response) => {
      commit('setResult', response.data)
      commit('toggleLoadingResult', false)
      commit('setCurrentPage', 'third')
      return response.data
    }).catch(error => {
      commit('toggleLoadingResult', false)
      console.log(error);
    })
  },
}

// mutations
const mutations = {
  setCurrentPage (state, value) {
    state.currentPage = value
  },
  setType (state, value) {
    state.type = value
  },
  setResult (state, value) {
    state.result = value
  },
  toggleLoadingResult(state, value) {
    state.isLoadingResult = value
  },
}

export default {
    namespaced: true,
    state,
    getters,
    actions,
    mutations
}
