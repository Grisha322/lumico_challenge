import BootstrapVue from 'bootstrap-vue';
import Vue from 'vue';
import App from './App.vue';
import router from './router';
import * as VueGoogleMaps from 'vue2-google-maps'
import 'bootstrap/dist/css/bootstrap.css';

Vue.use(BootstrapVue).use(
  VueGoogleMaps, {
  load: {
      key: 'AIzaSyCm4jNrMTGR6qXAF1cV_32dF9nf7I8lHfY',
  },
});

Vue.config.productionTip = false;

new Vue({
  router,
  render: (h) => h(App),
}).$mount('#app');
