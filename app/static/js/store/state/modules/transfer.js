import Api from '../../utils/api'

// initial state
const state = ({
  currentPage: "first", // We start at the first page
  type: null, // Answer selected by the user
  isLoadingResult: false, // Variable to know if the backend is currently calculating the graphs data
  result: null, // Variable to store the graphs data as a result of the POST
})

// getters
const getters = {}

// actions
const actions = {
  // Action to send data to backend
  sendData({ commit, state }, data) {
    // Endpoint to receive data
    let url = `/api/v1/transfer-method/`
    // We indicate that the backend starts to calculate data
    commit('toggleLoadingResult', true)

    // Add the answer of the user
    data.append("answer", state.type)

    // Do the post to the server to the url indicated using the
    // data collected (payload)
    return Api.post(url, data).then((response) => {
      // Once we have a response and a confirmation from the 
      //server we store the results and change the status of the 
      // 'loadingResult' since now we have a result
      commit('setResult', response.data)
      commit('toggleLoadingResult', false)
      commit('setCurrentPage', 'third')
      return response.data
    }).catch(error => {
      // If an error occurs print it on the browser console
      commit('toggleLoadingResult', false)
      console.log(error);
    })
  },
}

// mutations
const mutations = {
  // Mutation to change page (initial, method selection or graphs screen)
  setCurrentPage (state, value) {
    state.currentPage = value
  },
  // Mutation to set the answer selected by the user
  setType (state, value) {
    state.type = value
  },
  // Mutation to save the results with the graphs data
  setResult (state, value) {
    state.result = value
  },
  // Mutation to change the status of the isLoadingResult key 
  // so we will know when the server is calculating results
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
