<template>
  <div class="main-container container">
    <h2 class="w-100 text-left calculations-title">Calculations</h2>
    <h4 class="w-50 mt-3 text-center graphics-title">Graphics</h4>
    <LineChartGenerator
      :chart-options="chartOptions"
      :chart-data="chartData"
      :chart-id="chartId"
      :dataset-id-key="datasetIdKey"
      :plugins="plugins"
      :css-classes="cssClasses"
      :styles="styles"
      :width="width"
      :height="height"
      class="my-4"
    />
    <div class="d-flex justify-content-center align-items-center mt-3">
      <b-form-group 
        label="" 
        label-for="graph-download"
        label-align-sm="right"
        class="d-flex align-items-center mr-3 mb-0"
      >
        <b-form-select class="ml-4" v-model="download" id="graph-download">
          <b-form-select-option 
            :value="option.value"
            v-for="(option, index) in downloadOptions"
            :key="index" 
          >
            {{ option.text }}
          </b-form-select-option>
        </b-form-select>
      </b-form-group>
      <b-button class="ml-3" variant="success" @click="downloadData">Download</b-button>
    </div>
  </div>
</template>

<script>
import { mapState, mapActions } from "vuex"
import { Line as LineChartGenerator } from 'vue-chartjs/legacy'

import {
  Chart as ChartJS,
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement
} from 'chart.js'

ChartJS.register(
  Title,
  Tooltip,
  Legend,
  LineElement,
  LinearScale,
  CategoryScale,
  PointElement
)

export default {
  components: {
    LineChartGenerator
  },
  props: {
    chartId: {
      type: String,
      default: 'line-chart'
    },
    datasetIdKey: {
      type: String,
      default: 'label'
    },
    width: {
      type: Number,
      default: 400
    },
    height: {
      type: Number,
      default: 400
    },
    cssClasses: {
      default: '',
      type: String
    },
    styles: {
      type: Object,
      default: () => {}
    },
    plugins: {
      type: Array,
      default: () => []
    }
  },
  data() {
    return {
      download: null,
      downloadOptions: [
        { value: null, text: 'Select an option...' },
        { value: 'reflectance', text: 'Reflectance' },
        { value: 'transmittance', text: 'Transmittance' },
        { value: 'absorptance', text: 'Absorptance' },
      ],
      chartData: {
        labels: [
          'January',
          'February',
          'March',
          'April',
          'May',
          'June',
          'July'
        ],
        datasets: [
          {
            label: 'Transfer Data',
            backgroundColor: '#f87979',
            data: [40, 39, 10, 40, 39, 80, 40]
          }
        ]
      },
      chartOptions: {
        responsive: true,
        maintainAspectRatio: false
      },
    }
  },
  computed: {
    ...mapState({
    }),
  },
  methods: {
    ...mapActions({
    }),
    downloadData() {
      console.log("download")
    }
  },
  mounted() {
  },
}
</script>