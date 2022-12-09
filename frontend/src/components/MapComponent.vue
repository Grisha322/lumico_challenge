<template>
  <gmap-map
        :zoom="14"  
        :center="center"
        map-type-id="terrain"
        style="width: 500px; height: 300px"
      >
      <gmap-marker
        :key="index"
        v-for="(v, index) in vessels"
        :position="parsePosition(v)"
        :clickable="true"
        :draggable="true"
        @click="center=parsePosition(v)"
      ></gmap-marker>
    </gmap-map>
  </template>
  <script>

  export default {
    name: 'MapComponent',
    props: ['vessels'],
    data() {
      return {
        center:  {
          lat: 50.851452,
          lng: -1.179021
        },
      }
    },
    methods: {
      parsePosition(vessel){
        return {
          lat: parseFloat(vessel.lat),
          lng: parseFloat(vessel.long)
        }
      }
    },
  }
  </script>
  