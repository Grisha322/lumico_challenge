<template>
    <GMapMap
        :center="center"
        :zoom="7"
        map-type-id="terrain"
        style="width: 500px; height: 300px"
    >
      <GMapCluster>
        <GMapMarker
            :key="index"
            v-for="(m, index) in markers"
            :position="m.position"
            :clickable="true"
            :draggable="true"
            @click="center=m.position"
        />
      </GMapCluster>
    </GMapMap>
  </template>
  <script>
  export default {
    name: 'Map',
    props: ['vessels'],
    data() {
      return {
        center: {},
        markers: []
      }
    },
    created(){
        for (var vessel in this.vessels){
            this.markers.push({
                "position": {
                    "lat": vessel.lat,
                    "lng": vessel.long
                }
            })
        }
        center = markers[0]
    }
  }
  </script>
  