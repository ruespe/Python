<script setup>
import './App.css';
import { ref } from 'vue'
import ProfileCard from './components/ProfileCard.vue'

const name = ref('')
const city = ref('')
const tech = ref('')
</script>

<template>
  <div class="app">
    <div class="panel">
      <h1 class="title">Tarjeta de Perfil</h1>

      <div class="form">
        <div class="field">
          <label for="name">Nombre</label>
          <input id="name" v-model="name" type="text" placeholder="Ej: Rubén" />
        </div>
        <div class="field">
          <label for="city">Ciudad</label>
          <input id="city" v-model="city" type="text" placeholder="Ej: Mataró" />
        </div>
        <div class="field">
          <label for="tech">Tecnología preferida</label>
          <input id="tech" v-model="tech" type="text" placeholder="Ej: Vue" />
        </div>
      </div>
    </div>

    <div class="preview">
      <ProfileCard
        v-if="name"
        :name="name"
        :city="city"
        :tech="tech"
      />
      <p v-else class="hint">Introduce tu nombre para ver la tarjeta</p>
    </div>
  </div>
</template>

