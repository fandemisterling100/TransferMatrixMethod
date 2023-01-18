<template>
  <div class="main-container">
    hola
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
export default {
  components: {
  },
  data() {
    return {
      value: "",
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