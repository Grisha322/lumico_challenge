<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <h1>Vessels</h1>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.vessel-modal>Add Vessel</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Latitude</th>
              <th scope="col">Longitude</th>
              <th></th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(vessel, index) in vessels" :key="index">
              <td>{{ vessel.name }}</td>
              <td>{{ vessel.lat }}</td>
              <td>{{ vessel.long }}</td>
              <td>
                <div class="btn-group" role="group">
                  <button type="button" class="btn btn-warning btn-sm" v-b-modal.book-update-modal
        @click="editBook(book)">>Update</button>
                  <button type="button" class="btn btn-danger btn-sm" @click="deleteVessel(vessel.id)">Delete</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
    <b-modal ref="addVesselModal"
         id="vessel-modal"
         title="Add a new vessel"
         hide-footer>
      <b-form @submit="onSubmit" @reset="onReset" class="w-100">
        <b-form-group id="form-name-group"
                      label="Name:"
                      label-for="form-name-input">
          <b-form-input id="form-name-input"
                        type="text"
                        v-model="addVesselForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-lat-group"
                      label="Latitude:"
                      label-for="form-lat-input">
          <b-form-input id="form-lat-input"
                        type="number"
                        step="0.000001"
                        min="-99.999999"
                        max="99.999999"
                        v-model="addVesselForm.lat"
                        required
                        placeholder="Enter latitude">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-long-group"
                      label="Longitude:"
                      label-for="form-long-input">
          <b-form-input id="form-long-input"
                        type="number"
                        step="0.000001"
                        max="999.999999"
                        min="-999.999999"
                        v-model="addVesselForm.long"
                        required
                        placeholder="Enter longitude">
          </b-form-input>
        </b-form-group>
        <b-button type="submit" variant="primary">Submit</b-button>
        <b-button type="reset" variant="danger">Reset</b-button>
      </b-form>
    </b-modal>
    <b-modal ref="editVesselModal"
         id="vessel-update-modal"
         title="Update"
         hide-footer>
      <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
        <b-form-group id="form-name-edit-group"
                      label="Name:"
                      label-for="form-name-edit-input">
          <b-form-input id="form-name-edit-input"
                        type="text"
                        v-model="editForm.name"
                        required
                        placeholder="Enter name">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-lat-edit-group"
                      label="Latitude:"
                      label-for="form-lat-edit-input">
          <b-form-input id="form-lat-edit-input"
                        type="number"
                        step="0.000001"
                        max="99.999999"
                        min="-99.999999"
                        v-model="editForm.lat"
                        required
                        placeholder="Enter latitude">
          </b-form-input>
        </b-form-group>
        <b-form-group id="form-long-edit-group"
                      label="Longtitude:"
                      label-for="form-long-edit-input">
          <b-form-input id="form-long-edit-input"
                        type="number"
                        step="0.000001"
                        max="999.999999"
                        min="-999.999999"
                        v-model="editForm.long"
                        required
                        placeholder="Enter longtitude">
          </b-form-input>
        </b-form-group>
        <b-button-group>
          <b-button type="submit" variant="primary">Update</b-button>
          <b-button type="reset" variant="danger">Cancel</b-button>
        </b-button-group>
      </b-form>
    </b-modal>
  </div>
</template>

<script>
import axios from 'axios'
const path = 'http://localhost:5000/vessels/';
export default {
  name: 'HomeView',
  data() {
    return {
      vessels: [],
      addVesselForm: {
        name: '',
        lat: '',
        long: ''
      },
      editForm: {
        id: '',
        name: '',
        lat: '',
        long: ''
      },
    };
  },
  methods: {
    getVessels() {
      axios.get(path)
        .then((res) => {
          this.vessels = res.data.vessels;
          console.log(this.vessels)
        })
        .catch((error) => {
          console.error(error);
        });
    },
    onSuccess(){
      this.getVessels();
    },
    onError(error){
      // eslint-disable-next-line
      console.log(error);
      this.getVessels();
    },
    addVessel(payload) {
      axios.post(path, payload)
        .then(this.onSuccess)
        .catch(this.onError);
    },
    deleteVessel(bookId){
      axios.delete(path + `${bookId}`)
        .then(this.onSuccess)
        .catch(this.onError);
    },
    editVessel(payload, bookId){
      axios.put(path + `${bookId}`, payload)
      .then(this.onSuccess)
      .catch(this.onError)
    },
    initForm() {
      this.addVesselForm.name = '';
      this.addVesselForm.lat = '';
      this.addVesselForm.long = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addVesselModal.hide();
      const payload = {
        name: this.addVesselForm.name,
        lat: this.addVesselForm.lat,
        long: this.addVesselForm.long
      };
      this.addVessel(payload);
      this.initForm();
    },
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addVesselModal.hide();
      this.initForm();
    },
  },
     
  created() {
    this.getVessels();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}

</style>
