<template>
  <div class="methods-main-container w-100">
    <h2 class="w-100 text-left">Initial Parameters</h2>
    <div class="d-flex justify-content-center align-items-center middle-container">
      <div class="initial-params-container">
        <div class="initial-params">
          <b-form-group
            label="Initital angle"
            label-for="initial-angle"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'angular'"
          >
            <b-form-input id="initial-angle" v-model="initialAngle" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Final angle"
            label-for="final-angle"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'angular'"
          >
            <b-form-input id="final-angle" v-model="finalAngle" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Angle"
            label-for="angle"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'espectral'"
          >
            <b-form-input id="angle" v-model="angle" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Steps"
            label-for="steps"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="teps" v-model="steps" type="number"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Initial Wave Length"
            label-for="initialWaveLength"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'espectral'"
          >
            <b-form-input id="initialWaveLength" v-model="initialWaveLength" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Final Wave Length"
            label-for="finalWaveLength"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'espectral'"
          >
            <b-form-input id="finalWaveLength" v-model="finalWaveLength" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Wave Length"
            label-for="waveLength"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
            v-if="type === 'angular'"
          >
            <b-form-input id="waveLength" v-model="waveLength" type="number" step="0.1"></b-form-input>
          </b-form-group>

          
          <b-form-group 
          label="Polarization" 
          label-for="polarization"
          label-align-sm="right"
            class="d-flex align-items-center mr-3">
            <b-form-radio-group
              v-model="polarization"
              :options="polarizationOptions"
              class="d-flex align-items-center"
              value-field="item"
              text-field="name"
              id="polarization"
            ></b-form-radio-group>
          </b-form-group>
        </div>
        <div class="d-flex justify-content-center align-items-center flex-column method-options">
          <b-form-group 
            label="Substrate" 
            label-for="substrate"
            label-align-sm="right"
            class="d-flex align-items-center mr-3">
            <b-form-select v-model="substrate" id="substrate" @input="openMethodModal($event, 'substrate')">
              <b-form-select-option 
                :value="option.value"
                v-for="(option, index) in methodOptions"
                :key="index" 
              >
                {{ option.text }}
              </b-form-select-option>
            </b-form-select>
          </b-form-group>

          <b-form-group 
            label="Host" 
            label-for="host"
            label-align-sm="right"
            class="d-flex align-items-center mr-3">
            <b-form-select v-model="host" :options="methodOptions" id="host" @input="openMethodModal($event, 'host')"></b-form-select>
          </b-form-group>
        </div>
      </div>
      <div class="layers-container">
        <div class="layers-side">
          <div class="d-flex justify-content-between align-items-center title mb-4">
            <h5 class="mt-2">Layers</h5>
            <h5 class="mt-2 ml-4">Thicknesses</h5>
            <b-button variant="success" @click="addLayer">+</b-button>
          </div>
          <div v-for="(layer, index) in layers" :key="index" class="w-100 d-flex align-items-center layer-input">
            <div class="d-flex justify-content-center align-items-center layer-group">
              <b-form-group 
                :label="`Layer ${index+1}`" 
                :label-for="`layer-${index+1}`"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 mb-0"
              >
                <b-form-select v-model="layer.model" :id="`layer-${index+1}`"  @input="openMethodModal($event, `layer-${index+1}`)">
                  <b-form-select-option 
                    :value="option.value"
                    v-for="(option, index) in methodOptions"
                    :key="index" 
                  >
                    {{ option.text }}
                  </b-form-select-option>
                </b-form-select>
              </b-form-group>
            </div>
            <div class="thickness-input d-flex justify-content-center align-items-center">
              <b-form-group 
                :label="`Thickness ${index+1}`" 
                :label-for="`thickness-${index+1}`"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 mb-0"
              >
                <b-form-input :id="`thickness-${index+1}`" v-model="layer.thickness" type="number" step="0.1"></b-form-input>
              </b-form-group>
            </div>
            <b-button variant="danger" @click="removeLayer(index)">-</b-button>
          </div>
        </div>
      </div>
    </div>
    <div class="d-flex justify-content-center align-items-center">
      <b-button variant="info" class="align-self-end mt-4" @click="calculate">Calculate</b-button>
    </div>
    <!-- Modal Upload -->
    <b-modal id="modal-upload" title="Upload file" centered>
      <b-form-group label="File" label-cols-sm="2">
        <b-form-file id="file-default" accept=".csv, .txt" v-model="file"></b-form-file>
      </b-form-group>
      <template #modal-footer="{ ok, cancel }">
        <b-button size="sm" variant="success" @click="uploadFile(ok, 'modal-upload')">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>

    <!-- Modal Dielectric -->
    <b-modal id="modal-dielectric" title="Dielectric Function Models" centered>
      <b-form-select v-model="dielectricModel" id="dielectric-model">
        <b-form-select-option 
          :value="option.value"
          v-for="(option, index) in dielectricMethods"
          :key="index" 
        >
          {{ option.text }}
        </b-form-select-option>
      </b-form-select>

      <!-- Lorenz -->
      <div class="method-container" v-show="dielectricModel === 'lorenz'">
        <p class="w-100 font-weight-bold text-left my-2">Lorenz Model: For Dielectrics</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div>
          <b-form-group
            label="Ne"
            label-for="ne"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="ne" v-model="lorenz.ne" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="Wo"
            label-for="wo"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="wo" v-model="lorenz.wo" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="W"
            label-for="w"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="w" v-model="lorenz.w" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="r"
            label-for="r"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="r" v-model="lorenz.r" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>
        </div>
      </div>

      <!-- Drude -->
      <div class="method-container" v-show="dielectricModel === 'drude'">
        <p class="w-100 font-weight-bold text-left my-2">Drude Model: For Metals</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div>
          <b-form-group
            label="Ne"
            label-for="drude-ne"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="drude-ne" v-model="drude.ne" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="ε∞"
            label-for="drude-e"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="drude-e" v-model="drude.e" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="W"
            label-for="drude-w"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="drude-w" v-model="drude.w" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="r"
            label-for="drude-r"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="drude-r" v-model="drude.r" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>
        </div>
      </div>

      <!-- Sellmeier -->
      <div class="method-container" v-show="dielectricModel === 'sellmeier'">
        <p class="w-100 font-weight-bold text-left my-2">Sellmeier Model: For Transparents</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div>
          <b-form-group
            label="A"
            label-for="sellmeier-a"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="sellmeier-a" v-model="sellmeier.a" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="B"
            label-for="sellmeier-b"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="sellmeier-b" v-model="sellmeier.b" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="λ"
            label-for="sellmeier-lambda"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="sellmeier-lambda" v-model="waveLength" class="ml-3" disabled></b-form-input>
          </b-form-group>

          <b-form-group
            label="λo"
            label-for="sellmeier-lambdao"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="sellmeier-lambdao" v-model="sellmeier.lambdaO" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>
        </div>
      </div>

       <!-- Couchy -->
       <div class="method-container" v-show="dielectricModel === 'cauchy'">
        <p class="w-100 font-weight-bold text-left my-2">Cauchy Model: For Transparent Materials</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div>
          <b-form-group
            label="A"
            label-for="cauchy-a"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="cauchy-a" v-model="cauchy.a" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="B"
            label-for="cauchy-b"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="cauchy-b" v-model="cauchy.b" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="C"
            label-for="cauchy-c"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="cauchy-c" v-model="cauchy.c" class="ml-3" type="number" step="0.1"></b-form-input>
          </b-form-group>

          <b-form-group
            label="λ"
            label-for="cauchy-lambda"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-input id="cauchy-lambda" v-model="waveLength" class="ml-3" disabled></b-form-input>
          </b-form-group>
        </div>
      </div>
      <template #modal-footer="{ ok, cancel }">
        <b-button size="sm" variant="success"  @click="setDielectricMethod(ok, 'modal-dielectric')">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>

    <!-- Modal Manually -->
    <b-modal id="modal-manually" title="Manually" centered>
      <b-form-group
        label="n"
        label-for="manual-n"
        label-align-sm="right"
        class="d-flex align-items-center mr-3"
      >
        <b-form-input id="manual-n" v-model="manual.n" class="ml-3" type="number" step="0.1"></b-form-input>
      </b-form-group>

      <b-form-group
        label="k"
        label-for="manual-k"
        label-align-sm="right"
        class="d-flex align-items-center mr-3"
      >
        <b-form-input id="manual-k" v-model="manual.k" class="ml-3" type="number" step="0.1"></b-form-input>
      </b-form-group>
      <template #modal-footer="{ ok, cancel }">
        <b-button size="sm" variant="success"  @click="setManualMethod(ok, 'modal-manually')">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>

    <!-- Modal Effective Medium Theories -->
    <b-modal id="modal-efective" title="Effective Medium Theories" centered size="lg">
      <b-form-select v-model="effectiveMediumModel" id="effective-model">
        <b-form-select-option 
          :value="option.value"
          v-for="(option, index) in effectiveMethods"
          :key="index" 
        >
          {{ option.text }}
        </b-form-select-option>
      </b-form-select>

      <!-- Maxwell -->
      <div class="method-container" v-show="effectiveMediumModel === 'maxwell'">
        <p class="w-100 font-weight-bold text-left my-2">Maxwell Garnett Formula</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div class="w-100">
          <div class="w-100">
            <b-form-group
              label="ε"
              label-for="maxwell-em"
              label-align-sm="right"
              class="d-flex align-items-center mr-3"
            >
              <b-form-select v-model="maxwell.em" id="maxwell-em" class="ml-3">
                <b-form-select-option 
                  :value="option.value"
                  v-for="(option, index) in epsilonOptions"
                  :key="index" 
                >
                  {{ option.text }}
                </b-form-select-option>
              </b-form-select>
            </b-form-group>
            <div v-if="maxwell.em === 'manually'" class="d-flex align-items-center">
              <b-form-group 
                label="" 
                label-for="maxwell-em-manual"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 ml-2"
              >
                <b-form-radio-group
                  v-model="maxwell.emManual"
                  :options="maxwellManualOptions"
                  class="d-flex align-items-center"
                  value-field="item"
                  text-field="name"
                  id="maxwell-em-manual"
                ></b-form-radio-group>
              </b-form-group>

              <div v-if="maxwell.emManual === 'e'" class="d-flex align-items-center">
                <b-form-group
                  label="ε1"
                  label-for="manual-e1m"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3"
                >
                  <b-form-input id="manual-e1m" v-model="maxwell.e1m" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                </b-form-group>
                <b-form-group
                  label="ε2"
                  label-for="manual-e2m"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3 ml-3"
                >
                  <b-form-input id="manual-e2m" v-model="maxwell.e2m" class="ml-3" type="number" step="0.1"></b-form-input>
                </b-form-group>
              </div>
              <div v-if="maxwell.emManual === 'nk'" class="d-flex align-items-center">
                <b-form-group
                  label="n"
                  label-for="manual-nm"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3"
                >
                  <b-form-input id="manual-nm" v-model="maxwell.nm" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                </b-form-group>
                <b-form-group
                  label="k"
                  label-for="manual-km"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3 ml-3"
                >
                  <b-form-input id="manual-km" v-model="maxwell.km" class="ml-3" type="number" step="0.1"></b-form-input>
                </b-form-group>
              </div>
            </div>
            <div v-if="maxwell.em === 'file'">
              <b-form-group label="File" label-cols-sm="2" class="ml-2">
                <b-form-file id="file-maxwell-em" accept=".csv, .txt" v-model="maxwell.file" class="maxwell-file"></b-form-file>
              </b-form-group>
            </div>

            <div class="w-100">
              <div class="d-flex justify-content-between align-items-center title mb-4">
                <h5 class="my-4"># Inclusions</h5>
                <div class="d-flex justify-content-between align-items-center">
                  <h5 class="my-4 mr-4 pr-3">Volume Fraction</h5>
                  <b-button variant="success" @click="addInclusion">+</b-button>
                </div>
              </div>
              <div v-for="(inclusion, index) in inclusions" :key="index" class="w-100 d-flex justify-content-between align-items-center inclusions-container">
                <div>
                  <b-form-group 
                    :label="`ε${index+1}`" 
                    :label-for="`inclusion-maxwell-${index+1}`"
                    label-align-sm="right"
                    class="d-flex align-items-center mr-3 mb-0"
                  >
                    <b-form-select class="ml-4" v-model="inclusion.method" :id="`inclusion-maxwell-${index+1}`">
                      <b-form-select-option 
                        :value="option.value"
                        v-for="(option, index) in epsilonOptions"
                        :key="index" 
                      >
                        {{ option.text }}
                      </b-form-select-option>
                    </b-form-select>
                  </b-form-group>

                  <div v-if="inclusion.method === 'manually'" class="ml-3 mt-3">
                    <b-form-group 
                      label="" 
                      :label-for="`inclusion-maxwell-${index+1}`"
                      label-align-sm="right"
                      class="d-flex align-items-center mr-3 ml-2"
                    >
                      <b-form-radio-group
                        v-model="inclusion.manual"
                        :options="maxwellManualOptions"
                        class="d-flex align-items-center"
                        value-field="item"
                        text-field="name"
                        :id="`inclusion-maxwell-${index+1}`"
                      ></b-form-radio-group>
                    </b-form-group>

                    <div v-if="inclusion.manual === 'e'" class="d-flex align-items-center">
                      <b-form-group
                        label="ε1"
                        :label-for="`manual-e1m-${index+1}`"
                        label-align-sm="right"
                        class="d-flex align-items-center mr-3"
                      >
                        <b-form-input :id="`manual-e1m-${index+1}`" v-model="inclusion.e1m" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                      </b-form-group>
                      <b-form-group
                        label="ε2"
                        :label-for="`manual-e2m-${index+1}`"
                        label-align-sm="right"
                        class="d-flex align-items-center mr-3 ml-3"
                      >
                        <b-form-input :id="`manual-e2m-${index+1}`" v-model="inclusion.e2m" class="ml-3" type="number" step="0.1"></b-form-input>
                      </b-form-group>
                    </div>
                    <div v-if="inclusion.manual === 'nk'" class="d-flex align-items-center">
                      <b-form-group
                        label="n"
                        :label-for="`manual-nm-${index+1}`"
                        label-align-sm="right"
                        class="d-flex align-items-center mr-3"
                      >
                        <b-form-input :id="`manual-nm-${index+1}`" v-model="inclusion.nm" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                      </b-form-group>
                      <b-form-group
                        label="k"
                        :label-for="`manual-km-${index+1}`"
                        label-align-sm="right"
                        class="d-flex align-items-center mr-3 ml-3"
                      >
                        <b-form-input :id="`manual-km-${index+1}`" v-model="inclusion.km" class="ml-3" type="number" step="0.1"></b-form-input>
                      </b-form-group>
                    </div>
                  </div>
                  <div v-if="inclusion.method === 'file'" class="mt-3">
                    <b-form-group label="File" label-cols-sm="2" class="ml-3">
                      <b-form-file :id="`inclusion-file-${index+1}`" accept=".csv, .txt" v-model="inclusion.file" class="maxwell-file"></b-form-file>
                    </b-form-group>
                  </div>

                </div>

                <b-form-group 
                  :label="`f${index+1}`" 
                  :label-for="`maxwell-f-${index+1}`"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3 mb-0"
                >
                  <b-form-input class="ml-4" :id="`maxwell-f-${index+1}`" v-model="inclusion.volume" type="number" step="0.1"></b-form-input>
                </b-form-group>

                <b-button variant="danger" @click="removeInclusion(index)" v-if="index > 0">-</b-button>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Lorentz -->
      <div class="method-container" v-show="effectiveMediumModel === 'lorentz'">
        <p class="w-100 font-weight-bold text-left my-2">The Lorents-Lorenz Relation</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        <div class="w-100">
          <b-form-group
            label="εm"
            label-for="lorentz-em"
            label-align-sm="right"
            class="d-flex align-items-center mr-3"
          >
            <b-form-select v-model="lorentz.em" id="lorentz-em" class="ml-3">
              <b-form-select-option 
                :value="option.value"
                v-for="(option, index) in epsilonOptions"
                :key="index" 
              >
                {{ option.text }}
              </b-form-select-option>
            </b-form-select>
          </b-form-group>
          <div v-if="lorentz.em === 'manually'" class="d-flex align-items-center">
            <b-form-group 
              label="" 
              label-for="lorentz-em-manual"
              label-align-sm="right"
              class="d-flex align-items-center mr-3 ml-2"
            >
              <b-form-radio-group
                v-model="lorentz.emManual"
                :options="maxwellManualOptions"
                class="d-flex align-items-center"
                value-field="item"
                text-field="name"
                id="lorentz-em-manual"
              ></b-form-radio-group>
            </b-form-group>

            <div v-if="lorentz.emManual === 'e'" class="d-flex align-items-center">
              <b-form-group
                label="ε1m"
                label-for="lorentz-manual-e1m"
                label-align-sm="right"
                class="d-flex align-items-center mr-3"
              >
                <b-form-input id="lorentz-manual-e1m" v-model="lorentz.e1m" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
              <b-form-group
                label="ε2m"
                label-for="lorentz-manual-e2m"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 ml-3"
              >
                <b-form-input id="lorentz-manual-e2m" v-model="lorentz.e2m" class="ml-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
            </div>
            <div v-if="lorentz.emManual === 'nk'" class="d-flex align-items-center">
              <b-form-group
                label="nm"
                label-for="lorentz-nm"
                label-align-sm="right"
                class="d-flex align-items-center mr-3"
              >
                <b-form-input id="lorentz-nm" v-model="lorentz.nm" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
              <b-form-group
                label="km"
                label-for="lorentz-km"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 ml-3"
              >
                <b-form-input id="lorentz-km" v-model="lorentz.km" class="ml-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
            </div>
          </div>
          <div v-if="lorentz.em === 'file'">
            <b-form-group label="File" label-cols-sm="2" class="ml-2">
              <b-form-file id="file-lorentz-em" accept=".csv, .txt" v-model="lorentz.file" class="maxwell-file"></b-form-file>
            </b-form-group>
          </div>
        </div>

        <div class="w-100 mt-3">
          <b-form-group
            label="εi"
            label-for="lorentz-ei"
            label-align-sm="right"
            class="d-flex align-items-center mr-4"
          >
            <b-form-select v-model="lorentz.ei" id="lorentz-ei" class="ml-3">
              <b-form-select-option 
                :value="option.value"
                v-for="(option, index) in epsilonOptions"
                :key="index" 
              >
                {{ option.text }}
              </b-form-select-option>
            </b-form-select>
          </b-form-group>
          <div v-if="lorentz.ei === 'manually'" class="d-flex align-items-center">
            <b-form-group 
              label="" 
              label-for="lorentz-ei-manual"
              label-align-sm="right"
              class="d-flex align-items-center mr-3 ml-2"
            >
              <b-form-radio-group
                v-model="lorentz.eiManual"
                :options="maxwellManualOptions"
                class="d-flex align-items-center"
                value-field="item"
                text-field="name"
                id="lorentz-ei-manual"
              ></b-form-radio-group>
            </b-form-group>

            <div v-if="lorentz.eiManual === 'e'" class="d-flex align-items-center">
              <b-form-group
                label="ε1i"
                label-for="lorentz-manual-e1i"
                label-align-sm="right"
                class="d-flex align-items-center mr-3"
              >
                <b-form-input id="lorentz-manual-e1i" v-model="lorentz.e1i" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
              <b-form-group
                label="ε2i"
                label-for="lorentz-manual-e2i"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 ml-3"
              >
                <b-form-input id="lorentz-manual-e2i" v-model="lorentz.e2i" class="ml-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
            </div>
            <div v-if="lorentz.eiManual === 'nk'" class="d-flex align-items-center">
              <b-form-group
                label="ni"
                label-for="lorentz-ni"
                label-align-sm="right"
                class="d-flex align-items-center mr-3"
              >
                <b-form-input id="lorentz-ni" v-model="lorentz.ni" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
              <b-form-group
                label="ki"
                label-for="lorentz-ki"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 ml-3"
              >
                <b-form-input id="lorentz-ki" v-model="lorentz.ki" class="ml-3" type="number" step="0.1"></b-form-input>
              </b-form-group>
            </div>
          </div>
          <div v-if="lorentz.ei === 'file'">
            <b-form-group label="File" label-cols-sm="2" class="ml-2">
              <b-form-file id="file-lorentz-ei" accept=".csv, .txt" v-model="lorentz.filei" class="maxwell-file"></b-form-file>
            </b-form-group>
          </div>
        </div>
      </div>

      <!-- Bruggeman -->
      <div class="method-container" v-show="effectiveMediumModel === 'bruggeman'">
        <p class="w-100 font-weight-bold text-left my-2">Bruggeman Relation</p>
        <img src="https://www.researchgate.net/profile/Satyendra-Mourya/post/How_to_decide_realistic_parameters_in_Drude-Lorentz_model_for_fitting_ellipsometry_data/attachment/59d624ac6cda7b8083a20381/AS%3A400330371158017%401472457606803/image/Drude-Lorentz+equation.tif" alt="lorenz-model">
        
        <div class="w-100">
          <div class="d-flex justify-content-between align-items-center title mb-4">
            <h5 class="my-4"># Components</h5>
            <div class="d-flex justify-content-between align-items-center">
              <h5 class="my-4 mr-4 pr-3">Volume Fractions</h5>
              <b-button variant="success" @click="addComponent">+</b-button>
            </div>
          </div>
          <div v-for="(component, index) in components" :key="index" class="w-100 d-flex justify-content-between align-items-center inclusions-container">
            <div>
              <b-form-group 
                :label="`ε${index+1}`" 
                :label-for="`component-${index+1}`"
                label-align-sm="right"
                class="d-flex align-items-center mr-3 mb-0"
              >
                <b-form-select class="ml-4" v-model="component.method" :id="`component-${index+1}`">
                  <b-form-select-option 
                    :value="option.value"
                    v-for="(option, index) in epsilonOptions"
                    :key="index" 
                  >
                    {{ option.text }}
                  </b-form-select-option>
                </b-form-select>
              </b-form-group>

              <div v-if="component.method === 'manually'" class="ml-3 mt-3">
                <b-form-group 
                  label="" 
                  :label-for="`component-${index+1}`"
                  label-align-sm="right"
                  class="d-flex align-items-center mr-3 ml-2"
                >
                  <b-form-radio-group
                    v-model="component.manual"
                    :options="maxwellManualOptions"
                    class="d-flex align-items-center"
                    value-field="item"
                    text-field="name"
                    :id="`component-${index+1}`"
                  ></b-form-radio-group>
                </b-form-group>

                <div v-if="component.manual === 'e'" class="d-flex align-items-center">
                  <b-form-group
                    label="ε1"
                    :label-for="`component-e1i-${index+1}`"
                    label-align-sm="right"
                    class="d-flex align-items-center mr-3"
                  >
                    <b-form-input :id="`component-e1i-${index+1}`" v-model="component.e1i" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label="ε2"
                    :label-for="`component-e2i-${index+1}`"
                    label-align-sm="right"
                    class="d-flex align-items-center mr-3 ml-3"
                  >
                    <b-form-input :id="`component-e2i-${index+1}`" v-model="component.e2i" class="ml-3" type="number" step="0.1"></b-form-input>
                  </b-form-group>
                </div>
                <div v-if="component.manual === 'nk'" class="d-flex align-items-center">
                  <b-form-group
                    label="n"
                    :label-for="`component-ni-${index+1}`"
                    label-align-sm="right"
                    class="d-flex align-items-center mr-3"
                  >
                    <b-form-input :id="`component-ni-${index+1}`" v-model="component.ni" class="ml-3 mr-3" type="number" step="0.1"></b-form-input>
                  </b-form-group>
                  <b-form-group
                    label="k"
                    :label-for="`component-ki-${index+1}`"
                    label-align-sm="right"
                    class="d-flex align-items-center mr-3 ml-3"
                  >
                    <b-form-input :id="`component-ki-${index+1}`" v-model="component.ki" class="ml-3" type="number" step="0.1"></b-form-input>
                  </b-form-group>
                </div>
              </div>
              <div v-if="component.method === 'file'" class="mt-3">
                <b-form-group label="File" label-cols-sm="2" class="ml-3">
                  <b-form-file :id="`component-file-${index+1}`" accept=".csv, .txt" v-model="component.file" class="maxwell-file"></b-form-file>
                </b-form-group>
              </div>

            </div>

            <b-form-group 
              :label="`f${index+1}`" 
              :label-for="`component-f-${index+1}`"
              label-align-sm="right"
              class="d-flex align-items-center mr-3 mb-0"
            >
              <b-form-input class="ml-4" :id="`component-f-${index+1}`" v-model="component.volume" type="number" step="0.1"></b-form-input>
            </b-form-group>

            <b-button variant="danger" @click="removeComponent(index)" v-if="index > 0">-</b-button>
          </div>
        </div>
         
      </div>
      <template #modal-footer="{ ok, cancel }">
        <b-button size="sm" variant="success"  @click="setEffectiveMethod(ok, 'modal-efective')">
          OK
        </b-button>
        <b-button size="sm" variant="danger" @click="cancel()">
          Cancel
        </b-button>
      </template>
    </b-modal>

  </div>
  </template>

  
  
<script>
import { mapState, mapActions } from "vuex"
export default {
  data() {
    return {
      initialAngle: 0,
      finalAngle: 90,
      angle: 0,
      steps: 50,
      initialWaveLength: 0,
      finalWaveLength: 0,
      waveLength: 0.1,
      polarization: 'p',
      substrate: null, 
      host: null,
      file: null,
      polarizationOptions: [
        { item: 'p', name: 'P' },
        { item: 's', name: 'S' },
      ],
      dielectricMethods: [
        { value: null, text: 'Select a model...' },
        { value: 'lorenz', text: 'Lorenz Model' },
        { value: 'drude', text: 'Drude Model' },
        { value: 'sellmeier', text: 'Sellmeier Model' },
        { value: 'cauchy', text: 'Cauchy Model' },
      ],
      manual: {
        n: null,
        k: null,
      },
      entityPointer: null,
      dielectricModel: null,
      lorenz: {
        ne: null,
        wo: null,
        w: null,
        r: null,
      },
      drude: {
        ne: null,
        e: null,
        w: null,
        r: null,
      },
      sellmeier: {
        a: null,
        b: null,
        lambdaO: null,
      },
      cauchy: {
        a: null,
        b: null,
        c: null,
      },
      layers: [],
      effectiveMediumModel: null,
      effectiveMethods: [
        { value: null, text: 'Select a model...' },
        { value: 'maxwell', text: 'Maxwell Garnett Formula' },
        { value: 'lorentz', text: 'The Lorentz-Lorenz Relation' },
        { value: 'bruggeman', text: 'Bruggeman Relation' },
      ],
      maxwell: {
        em: null,
        file: null,
        emManual: null,
        e1m: null,
        e2m: null,
        nm: null,
        km: null,
      },
      epsilonOptions: [
        { value: null, text: 'Select a model...' },
        { value: 'manually', text: 'Manually' },
        { value: 'file', text: 'File' },
      ],
      maxwellManualOptions: [
        { item: 'e', name: 'Dielectric Function' },
        { item: 'nk', name: 'Refractive Index' },
      ],
      inclusions: [
        {
          method: null,
          file: null,
          manual: null,
          e1m: null,
          e2m: null,
          nm: null,
          km: null,
          volume: null,
        }
      ],
      lorentz: {
        em: null,
        file: null,
        emManual: null,
        e1m: null,
        e2m: null,
        nm: null,
        km: null,

        ei: null,
        filei: null,
        eiManual: null,
        e1i: null,
        e2i: null,
        ni: null,
        ki: null,
      },
      components: [
        {
          method: null,
          file: null,
          manual: null,
          e1i: null,
          e2i: null,
          ni: null,
          ki: null,
          volume: null,
        }
      ],
      materials: {},
    }
  },
  computed: {
    ...mapState({
      type: state => state.transfer.type,
    }),
    methodOptions() {
      let methods = [
        { value: null, text: 'Select a method...' },
        { value: 'upload', text: 'Upload file' },
        { value: 'dielectric', text: 'Dielectric Function Models' },
        { value: 'efective', text: 'Efective Medium Theories' },
      ]
      if (this.type === 'angular') {
        methods.push({ value: 'manually', text: 'Manually' })
      }
      return methods
    }, 
  },
  methods: {
    ...mapActions({
      sendData: "transfer/sendData",
    }),
    openMethodModal(method, entity) {
      this.$bvModal.show(`modal-${method}`)
      this.entityPointer = entity
    },
    addLayer() {
      this.layers.push({
        model: null,
        thickness: 0,
      })
    },
    addInclusion() {
      this.inclusions.push({
        method: null,
        file: null,
        manual: null,
        e1m: null,
        e2m: null,
        nm: null,
        km: null,
        volume: null,
      })
    },
    addComponent() {
      this.components.push({
        method: null,
        file: null,
        manual: null,
        e1i: null,
        e2i: null,
        ni: null,
        ki: null,
        volume: null,
      })
    },
    removeLayer(index) {
      this.layers.splice(index, 1);
    },
    removeInclusion(index) {
      this.inclusions.splice(index, 1);
    },
    removeComponent(index) {
      this.components.splice(index, 1);
    },
    renameFile(originalFile, newName) {
      return new File([originalFile], newName, {
          type: originalFile.type,
          lastModified: originalFile.lastModified,
      });
    },
    calculate() {
      const formData = new FormData()
      formData.append("initialAngle", this.initialAngle)
      formData.append("finalAngle", this.finalAngle)
      formData.append("angle", this.angle)
      formData.append("steps", this.steps)
      formData.append("initialWaveLength", this.initialWaveLength)
      formData.append("finalWaveLength", this.finalWaveLength)
      formData.append("waveLength", this.waveLength)
      formData.append("polarization", this.polarization)
      formData.append("substrate", this.substrate)
      formData.append("host", this.host)
      formData.append("materialsQuantity", 2 + this.layers.length)
      
      Object.keys(this.materials).forEach(key => {
        // Different logic for maxwell and its inclusions
        if (this.materials[key].option.includes('maxwell')) {
          // Maxwell with file in the main E
          if (this.materials[key].option.includes('file')) {
            formData.append("materials", this.materials[key].value)
          } else {
            // Add manual data
            let material = {}
            material[key] = {}
            Object.keys(this.materials[key]).forEach(subkey => {
              // Omit inclusions data
              if (!subkey.includes('inclusion')) {
                material[key][subkey] = this.materials[key][subkey]
              } else {
                // Add inclusion data
                if (this.materials[key][subkey].option == 'file') {
                  const volume = this.materials[key][subkey].volume
                  material[key][subkey] = {volume: volume}
                  formData.append("materials", this.materials[key][subkey].value)
                } else {
                  material[key][subkey] = this.materials[key][subkey]
                }
              }
            })
            formData.append("materials", JSON.stringify(material))
          }
        } else if (this.materials[key].option.includes('bruggeman')) {
          let material = {}
          material[key] = {}
          Object.keys(this.materials[key]).forEach(subkey => {
            // Add component data
            if (this.materials[key][subkey].option == 'file') {
              const volume = this.materials[key][subkey].volume
              material[key][subkey] = {volume: volume}
              formData.append("materials", this.materials[key][subkey].value)
            } else {
              material[key][subkey] = this.materials[key][subkey]
            }
          })
          formData.append("materials", JSON.stringify(material))
          
        } else if (this.materials[key].option === 'file' || this.materials[key].option.includes('file')) {  
          formData.append("materials", this.materials[key].value)
        } 
        else if (this.materials[key].option === 'lorentz') {
          // For Lorentz add two files, one for Em and another one for Ei
          // Also add manual parameters en each case
          if ('em' in this.materials[key]) {
            formData.append("materials", this.materials[key].em.value)
          } 
          if ('e-em' in this.materials[key]) {
            let material = {}
            material[key] = this.materials[key]
            formData.append("materials", JSON.stringify(material))
          }
          if ('ei' in this.materials[key]) {
            formData.append("materials", this.materials[key].ei.value)
          }
          if ('e-ei' in this.materials[key]) {
            let material = {}
            material[key] = this.materials[key]
            formData.append("materials", JSON.stringify(material))
          }
        } else {
          let material = {}
          material[key] = this.materials[key]
          formData.append("materials", JSON.stringify(material))
        }
        if (key.includes('layer')) {
          const index = key.split('-')[1] - 1 
          let material = {}
          material[key] = {
            thickness: this.layers[index].thickness
          }
          formData.append("materials", JSON.stringify(material))
        } 
      });

      this.sendData(formData);
    }, 
    uploadFile(method, modal) {
      // Get entity (subtract, host, layers) to update
      // its option and file uploaded
      let currentEntity = this.entityPointer
      let data = {
        option: 'file',
        value: this.renameFile(this.file, currentEntity),
      }
      method();
      this.materials[currentEntity] = data
      this.disableEntity()
      this.cleanModal(modal)
    }, 
    setDielectricMethod(method, modal) {
      // get current material (substract, host or layer)
      let currentEntity = this.entityPointer
      const option = this.dielectricModel
      let data = {
        option: option,
      }
      // Identify dielectric method and get parameters
      if (option === 'lorenz') {
        data = {
          ...data,
          ne: this.lorenz.ne,
          wo: this.lorenz.wo,
          w: this.lorenz.w,
          r: this.lorenz.r,
        }
      }

      if (option === 'drude') {
        data = {
          ...data,
          ne: this.drude.ne,
          e: this.drude.e,
          w: this.drude.w,
          r: this.drude.r,
        }
      }

      if (option === 'sellmeier') {
        data = {
          ...data,
          a: this.sellmeier.a,
          b: this.sellmeier.b,
          lambdaO: this.sellmeier.lambdaO,
        }
      }

      if (option === 'cauchy') {
        data = {
          ...data,
          a: this.cauchy.a,
          b: this.cauchy.b,
          c: this.cauchy.c,
        }
      }

      if (currentEntity.includes('layer')) {
        const index = parseInt(currentEntity.split('-')[1]) - 1;
        data = {
          ...data,
          thickness: this.layers[index].thickness,
        }
      }
      method();
      this.materials[currentEntity] = data
      this.disableEntity()
      this.cleanModal(modal)
    },
    setManualMethod(method, modal) {
      let currentEntity = this.entityPointer
      let data = {
        option: 'manual',
        k: this.manual.k,
        n: this.manual.n,
      }
      method();
      this.materials[currentEntity] = data
      this.disableEntity()
      this.cleanModal(modal)
    },
    setEffectiveMethod(method, modal) {
      // Get current material (substract, host or layer)
      let currentEntity = this.entityPointer
      const option = this.effectiveMediumModel
      let data = {
        option: option,
      }
      // Identify dielectric method and get parameters
      if (option === 'maxwell') {
        // Send parameters for manual Maxwell
        if (this.maxwell.em === 'manually') {
          data[this.maxwell.emManual] = {
            e1m: this.maxwell.e1m,
            e2m: this.maxwell.e2m,
            nm: this.maxwell.nm,
            km: this.maxwell.km,
          }
        }
        // Send file for Maxwell with filename 'entity-maxwell'
        if (this.maxwell.em === 'file') {
          const newFileName = `${currentEntity}-${option}`
          data = {
            option: `${option}-file`,
            value: this.renameFile(this.maxwell.file, newFileName),
          }
        }

        //  Add inclusions
        this.inclusions.forEach((inclusion, index) => {
          if (inclusion.method === "manually") {
            data[`${currentEntity}-inclusion-${index + 1}`] = {
              option: inclusion.manual,
              e1m: inclusion.e1m,
              e2m: inclusion.e2m,
              km: inclusion.km,
              nm: inclusion.nm,
              volume: inclusion.volume,
            }
          }
          if (inclusion.method === "file") {
            const newFileName = `${currentEntity}-inclusion-${index + 1}`
            data[`${currentEntity}-inclusion-${index + 1}`] = {
              option: 'file',
              value: this.renameFile(inclusion.file, newFileName),
              volume: inclusion.volume,
            }
          }
        });
      }

      if (option === 'lorentz') {
        // Send parameters for manual Lorentz
        if (this.lorentz.em === 'manually') {
          data[`${this.lorentz.eiManual}-em`] = {
            e1m: this.lorentz.e1m,
            e2m: this.lorentz.e2m,
            nm: this.lorentz.nm,
            km: this.lorentz.km,
          }
        }
        if (this.lorentz.ei === 'manually') {
          data[`${this.lorentz.eiManual}-ei`] = {
            e1i: this.lorentz.e1i,
            e2i: this.lorentz.e2i,
            ni: this.lorentz.ni,
            ki: this.lorentz.ki,
          }
        }
        // Send file for Lorentz with filename 'entity-lorentz'
        if (this.lorentz.em === 'file') {
          const newFileName = `${currentEntity}-em-${option}`
          data['em'] = {
            option: `${option}-file`,
            value: this.renameFile(this.lorentz.file, newFileName),
          }
        }

        if (this.lorentz.ei === 'file') {
          const newFileName = `${currentEntity}-ei-${option}`
          data['ei'] = {
            option: `${option}-file`,
            value: this.renameFile(this.lorentz.filei, newFileName),
          }
        }
      }

      if (option === 'bruggeman') {
        //  Add components
        this.components.forEach((component, index) => {
          if (component.method === "manually") {
            data[`${currentEntity}-component-${index + 1}`] = {
              option: component.manual,
              e1i: component.e1i,
              e2i: component.e2i,
              ni: component.ni,
              ki: component.ki,
              volume: component.volume,
            }
          }
          if (component.method === "file") {
            const newFileName = `${currentEntity}-component-${index + 1}`
            data[`${currentEntity}-component-${index + 1}`] = {
              option: 'file',
              value: this.renameFile(component.file, newFileName),
              volume: component.volume,
            }
          }
        });
      }

      method();
      this.materials[currentEntity] = data
      this.disableEntity()
      this.cleanModal(modal)
    },
    disableEntity() {
      const currentEntity = this.entityPointer;
      $( `#${currentEntity}` ).prop( "disabled", true );
    },
    cleanModal(modal) {
      if (modal === 'modal-upload') {
        this.file = null
      }

      if (modal === 'modal-dielectric') {
        this.dielectricModel = null
        this.lorenz = {
          ne: null,
          wo: null,
          w: null,
          r: null,
        }
        this.drude = {
          ne: null,
          e: null,
          w: null,
          r: null,
        }
        this.sellmeier = {
          a: null,
          b: null,
          lambdaO: null,
        }
        this.cauchy = {
          a: null,
          b: null,
          c: null,
        }
      }

      if (modal === 'modal-manually') {
        this.manual = {
          n: null,
          k: null,
        }
      }

      if (modal === 'modal-efective') {
        this.effectiveMediumModel = null

        this.maxwell = {
          em: null,
          file: null,
          emManual: null,
          e1m: null,
          e2m: null,
          nm: null,
          km: null,
        }

        this.inclusions = [
          {
            method: null,
            file: null,
            manual: null,
            e1m: null,
            e2m: null,
            nm: null,
            km: null,
            volume: null,
          }
        ]

        this.lorentz = {
          em: null,
          file: null,
          emManual: null,
          e1m: null,
          e2m: null,
          nm: null,
          km: null,

          ei: null,
          filei: null,
          eiManual: null,
          e1i: null,
          e2i: null,
          ni: null,
          ki: null,
        }
      }

      this.components = [
        {
          method: null,
          file: null,
          manual: null,
          e1i: null,
          e2i: null,
          ni: null,
          ki: null,
          volume: null,
        }
      ]
    },
  },
  mounted() {
  },
}
</script>