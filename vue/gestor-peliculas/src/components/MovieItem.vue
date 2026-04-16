<script setup>
defineProps({
  movie: {
    type: Object,
    required: true,
  },
})

const emit = defineEmits(['delete-movie'])

const currentYear = new Date().getFullYear()
</script>

<template>
  <div
    class="movie-card"
    :class="{ 'movie-card--modern': movie.year > 2015 }"
  >
    <div class="card-image">
      <img
        :src="movie.image"
        :alt="`Poster de ${movie.name}`"
        loading="lazy"
        @error="$event.target.src = `https://placehold.co/300x420/1a1a2e/e94560?text=${encodeURIComponent(movie.name)}`"
      />

      <span v-if="movie.year > 2015" class="badge badge--modern">
        Moderno
      </span>
      <span v-else class="badge badge--classic">
         Clásico
      </span>
    </div>

    <div class="card-body">
      <h3 class="card-title">{{ movie.name }}</h3>

      <div class="card-meta">
        <span class="meta-year">
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M6.75 3v2.25M17.25 3v2.25M3 18.75V7.5a2.25 2.25 0 0 1 2.25-2.25h13.5A2.25 2.25 0 0 1 21 7.5v11.25m-18 0A2.25 2.25 0 0 0 5.25 21h13.5A2.25 2.25 0 0 0 21 18.75m-18 0v-7.5A2.25 2.25 0 0 1 5.25 9h13.5A2.25 2.25 0 0 1 21 11.25v7.5" /></svg>
          {{ movie.year }}
        </span>
        <span class="meta-genre">
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9.568 3H5.25A2.25 2.25 0 0 0 3 5.25v4.318c0 .597.237 1.17.659 1.591l9.581 9.581c.699.699 1.78.872 2.607.33a18.095 18.095 0 0 0 5.223-5.223c.542-.827.369-1.908-.33-2.607L11.16 3.66A2.25 2.25 0 0 0 9.568 3Z" /><path stroke-linecap="round" stroke-linejoin="round" d="M6 6h.008v.008H6V6Z" /></svg>
          {{ movie.genre }}
        </span>
      </div>

      <div class="age-bar">
        <div
          class="age-bar-fill"
          :style="{
            width: Math.min(((currentYear - movie.year) / 50) * 100, 100) + '%',
          }"
          :title="`${currentYear - movie.year} años de antigüedad`"
        ></div>
      </div>
      <span class="age-label">{{ currentYear - movie.year }} años</span>
    </div>

    <button
      class="btn-delete"
      :title="`Eliminar ${movie.name}`"
      @click="emit('delete-movie', movie.id)"
    >
      <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m14.74 9-.346 9m-4.788 0L9.26 9m9.968-3.21c.342.052.682.107 1.022.166m-1.022-.165L18.16 19.673a2.25 2.25 0 0 1-2.244 2.077H8.084a2.25 2.25 0 0 1-2.244-2.077L4.772 5.79m14.456 0a48.108 48.108 0 0 0-3.478-.397m-12 .562c.34-.059.68-.114 1.022-.165m0 0a48.11 48.11 0 0 1 3.478-.397m7.5 0v-.916c0-1.18-.91-2.164-2.09-2.201a51.964 51.964 0 0 0-3.32 0c-1.18.037-2.09 1.022-2.09 2.201v.916m7.5 0a48.667 48.667 0 0 0-7.5 0" /></svg>
    </button>
  </div>
</template>

<style scoped>
.movie-card {
  position: relative;
  background: #1e1e1e;
  border: 1px solid #333;
  border-radius: 8px;
  overflow: hidden;
  display: flex;
  flex-direction: column;
}

.movie-card--modern {
  border-color: #4caf50;
}

.card-image {
  position: relative;
  width: 100%;
  aspect-ratio: 2 / 3;
  overflow: hidden;
  background: #121212;
}

.card-image img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.badge {
  position: absolute;
  top: 8px;
  right: 8px;
  padding: 0.2rem 0.5rem;
  border-radius: 4px;
  font-size: 0.7rem;
  font-weight: 600;
}

.badge--modern {
  background: #4caf50;
  color: #fff;
}

.badge--classic {
  background: #e94560;
  color: #fff;
}

.card-body {
  padding: 0.8rem;
  flex: 1;
  display: flex;
  flex-direction: column;
  gap: 0.4rem;
}

.card-title {
  margin: 0;
  font-size: 1rem;
  color: #e0e0e0;
}

.card-meta {
  display: flex;
  gap: 0.5rem;
  flex-wrap: wrap;
}

.meta-year,
.meta-genre {
  font-size: 0.75rem;
  color: #888;
  display: inline-flex;
  align-items: center;
  gap: 0.25rem;
}

.age-bar {
  height: 3px;
  background: #333;
  border-radius: 2px;
  overflow: hidden;
  margin-top: auto;
}

.age-bar-fill {
  height: 100%;
  background: #e94560;
  border-radius: 2px;
}

.age-label {
  font-size: 0.65rem;
  color: #666;
}

.btn-delete {
  position: absolute;
  top: 8px;
  left: 8px;
  width: 28px;
  height: 28px;
  border: none;
  border-radius: 4px;
  background: rgba(0, 0, 0, 0.7);
  font-size: 1rem;
  cursor: pointer;
  opacity: 0;
  transition: opacity 0.2s;
  display: flex;
  align-items: center;
  justify-content: center;
}

.movie-card:hover .btn-delete {
  opacity: 1;
}

.btn-delete:hover {
  background: #e94560;
}
</style>
