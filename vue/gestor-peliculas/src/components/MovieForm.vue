<script setup>
import { ref } from 'vue'

const emit = defineEmits(['add-movie'])

const name = ref('')
const year = ref('')
const genre = ref('')
const image = ref('')

const genres = [
  'Acción',
  'Aventura',
  'Ciencia Ficción',
  'Comedia',
  'Drama',
  'Terror',
  'Animación',
  'Fantasía',
]

function handleSubmit() {
  if (!name.value.trim() || !year.value) return

  emit('add-movie', {
    name: name.value.trim(),
    year: Number(year.value),
    genre: genre.value || 'Sin género',
    image:
      image.value.trim() ||
      `https://placehold.co/300x420/1a1a2e/e94560?text=${encodeURIComponent(name.value.trim())}`,
  })

  name.value = ''
  year.value = ''
  genre.value = ''
  image.value = ''
}
</script>

<template>
  <form class="movie-form" @submit.prevent="handleSubmit">
    <h2>Añadir Película</h2>

    <div class="form-grid">
      <div class="form-group">
        <label for="movie-name">Nombre *</label>
        <input
          id="movie-name"
          v-model="name"
          type="text"
          placeholder="Ej: Inception"
          required
        />
      </div>

      <div class="form-group">
        <label for="movie-year">Año *</label>
        <input
          id="movie-year"
          v-model="year"
          type="number"
          min="1900"
          max="2030"
          placeholder="Ej: 2020"
          required
        />
      </div>

      <div class="form-group">
        <label for="movie-genre">Género</label>
        <select id="movie-genre" v-model="genre">
          <option value="">Selecciona un género</option>
          <option v-for="g in genres" :key="g" :value="g">{{ g }}</option>
        </select>
      </div>

      <div class="form-group">
        <label for="movie-image">URL Imagen</label>
        <input
          id="movie-image"
          v-model="image"
          type="url"
          placeholder="https://... (opcional)"
        />
      </div>
    </div>

    <button type="submit" class="btn-add" :disabled="!name.trim() || !year">
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v6m3-3H9m12 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" /></svg>
      Añadir a la lista
    </button>
  </form>
</template>

<style scoped>
.movie-form {
  background: #1e1e1e;
  border: 1px solid #333;
  border-radius: 8px;
  padding: 1.5rem;
  margin-bottom: 1.5rem;
}

.movie-form h2 {
  margin: 0 0 1rem 0;
  color: #e94560;
  font-size: 1.2rem;
}

.form-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 0.8rem;
}

@media (max-width: 600px) {
  .form-grid {
    grid-template-columns: 1fr;
  }
}

.form-group {
  display: flex;
  flex-direction: column;
  gap: 0.3rem;
}

.form-group label {
  color: #888;
  font-size: 0.8rem;
  font-weight: 600;
}

.form-group input,
.form-group select {
  padding: 0.5rem 0.7rem;
  border: 1px solid #333;
  border-radius: 6px;
  background: #121212;
  color: #e0e0e0;
  font-size: 0.9rem;
}

.form-group input:focus,
.form-group select:focus {
  outline: none;
  border-color: #e94560;
}

.form-group input::placeholder {
  color: #555;
}

.btn-add {
  margin-top: 1rem;
  width: 100%;
  padding: 0.6rem;
  border: none;
  border-radius: 6px;
  background: #e94560;
  color: white;
  font-size: 0.95rem;
  font-weight: 600;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.btn-add:hover:not(:disabled) {
  background: #d13a54;
}

.btn-add:disabled {
  opacity: 0.4;
  cursor: not-allowed;
}
</style>
