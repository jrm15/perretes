<template>
  <vue-cal
      active-view="week"
      :disable-views="['years', 'year', 'month', 'day']"
      locale="es"
      show-time-in-cells
      :time-step="timeStep"
      :time-from="7 * 60"
      :time-to="20 * 60"
      :events="events"
      :special-hours="specialHours"
      :on-event-click="onEventClick"
      style="width: 100vh;"
  />
</template>


<script setup>
import { ref } from 'vue'
import VueCal from 'vue-cal'
import 'vue-cal/dist/vuecal.css'
import {specialHours, events, timeStep} from '../data.js'

const showDialog = ref(false)
let selectedEvent = ref({})

function onEventClick(event, e){
  this.selectedEvent = event
  this.showDialog = true
  console.log('event', event.free)

  // Prevent navigating to narrower view (default vue-cal behavior).
  e.stopPropagation()
}

</script>


<style>

.vuecal__special-hours {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4px;

  em {font-size: 0.9em;color: #999;}
}

.ocupado {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 4px;

  em {font-size: 0.9em;color: #999;}
}
.ocupado .vuecal__event-time {display: none}

.vuecal__menu, .vuecal__cell-events-count {display: none}
.vuecal__no-event {display: none}

.closed {
  background:
      #fff7f0
      repeating-linear-gradient(
          -45deg,
          rgba(255, 162, 87, 0.25),
          rgba(255, 162, 87, 0.25) 5px,
          rgba(255, 255, 255, 0) 5px,
          rgba(255, 255, 255, 0) 15px
      );
  color: #f6984c;
}
.free {background-color: rgba(100, 220, 102, 0.9);border: 1px solid rgb(235, 82, 82);color: #fff;}




</style>