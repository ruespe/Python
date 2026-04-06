<script setup>
import MovieItem from './MovieItem.vue'

defineProps({
  movies: {
    type: Array,
    required: true,
  },
})

const emit = defineEmits(['delete-movie'])
</script>

<template>
  <div v-if="movies.length === 0" class="empty-state">
    <h3>No hay películas en el catálogo</h3>
    <p>Usa el formulario de arriba para añadir tu primera película.</p>
  </div>

  <div v-else class="movie-grid">
    <MovieItem
      v-for="movie in movies"
      :key="movie.id"
      :movie="movie"
      @delete-movie="emit('delete-movie', $event)"
    />
  </div>
</template>

<style scoped>
.movie-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
  gap: 1rem;
}

.empty-state {
  text-align: center;
  padding: 3rem 1.5rem;
  background: #1e1e1e;
  border: 1px dashed #444;
  border-radius: 8px;
  color: #888;
}



.empty-state h3 {
  color: #e0e0e0;
  margin: 0 0 0.3rem 0;
  font-size: 1.1rem;
}

.empty-state p {
  margin: 0;
  font-size: 0.85rem;
}
</style>
