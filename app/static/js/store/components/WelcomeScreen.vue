<template>
  <div class="main-container">
    <div class="welcome-header">
      <h3>Transfer Matrix Method</h3>
      <img src="https://cdn-icons-png.flaticon.com/512/508/508970.png" alt="semillero">
    </div>
    <div class="introduction">
      <div>
        <h5>Introducción del método y la App</h5>
        <div>
          Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.
        </div>
      </div>
      <div>
        <img src="data:image/png;base64,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" alt="transfer_matrix_method">
      </div>
    </div>
    <div class="d-flex w-50 justify-content-center align-items-center mt-5">
      <b-form-select v-model="type" :options="options" id="input-type"></b-form-select>
      <b-button variant="success" class="ml-3">Ir</b-button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
export default {
  components: {
  },
  data() {
    return {
      type: null,
      options: [
        { value: null, text: 'Respuesta' },
        { value: 'angular', text: 'Angular' },
        { value: 'espectral', text: 'Espectral' },
      ],
    }
  },
  computed: {
    ...mapState({
    }),
  },
  methods: {
    ...mapActions({

    }),
  },
  mounted() {
  },
}
</script>

<style scoped>
>>>.button {
  width: 50%;
}
</style>