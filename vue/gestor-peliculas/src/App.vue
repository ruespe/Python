<script setup>
import { ref, computed } from 'vue'
import MovieForm from './components/MovieForm.vue'
import MovieList from './components/MovieList.vue'

const movies = ref([
  {
    id: 1,
    name: 'Inception',
    year: 2010,
    genre: 'Ciencia Ficción',
    image: 'https://image.tmdb.org/t/p/w500/ljsZTbVsrQSqZgWeep2B1QiDKuh.jpg',
  },
  {
    id: 2,
    name: 'Spider-Man: Across the Spider-Verse',
    year: 2023,
    genre: 'Animación',
    image: 'https://image.tmdb.org/t/p/w500/8Vt6mWEReuy4Of61Lnj5Xj704m8.jpg',
  },
  {
    id: 3,
    name: 'The Dark Knight',
    year: 2008,
    genre: 'Acción',
    image: 'https://image.tmdb.org/t/p/w500/qJ2tW6WMUDux911Z7h1suhXSOB8.jpg',
  },
  {
    id: 4,
    name: 'Dune: Part Two',
    year: 2024,
    genre: 'Ciencia Ficción',
    image: 'https://image.tmdb.org/t/p/w500/czembW0Rk1Ke7lCJGahbOhdCuhV.jpg',
  },
  {
    id: 5,
    name: 'Pulp Fiction',
    year: 1994,
    genre: 'Drama',
    image: 'https://image.tmdb.org/t/p/w500/d5iIlFn5s0ImszYzBPb8JPIfbXD.jpg',
  },
])

const filter = ref('all')
const searchQuery = ref('')

const filteredMovies = computed(() => {
  let result = movies.value

  if (filter.value === 'modern') {
    result = result.filter((m) => m.year > 2015)
  } else if (filter.value === 'classic') {
    result = result.filter((m) => m.year <= 2015)
  }

  if (searchQuery.value.trim()) {
    const q = searchQuery.value.toLowerCase()
    result = result.filter(
      (m) =>
        m.name.toLowerCase().includes(q) ||
        m.genre.toLowerCase().includes(q) ||
        String(m.year).includes(q),
    )
  }

  return result
})

const totalCount = computed(() => movies.value.length)
const modernCount = computed(() => movies.value.filter((m) => m.year > 2015).length)
const classicCount = computed(() => movies.value.filter((m) => m.year <= 2015).length)

let nextId = 6

function addMovie(movieData) {
  movies.value.push({
    id: nextId++,
    ...movieData,
  })
}

function deleteMovie(id) {
  movies.value = movies.value.filter((m) => m.id !== id)
}
</script>

<template>
  <div class="app">
    <header class="app-header">
      <h1>
        <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m15.75 10.5 4.72-4.72a.75.75 0 0 1 1.28.53v11.38a.75.75 0 0 1-1.28.53l-4.72-4.72M4.5 18.75h9a2.25 2.25 0 0 0 2.25-2.25v-9a2.25 2.25 0 0 0-2.25-2.25h-9A2.25 2.25 0 0 0 2.25 7.5v9a2.25 2.25 0 0 0 2.25 2.25Z" /></svg>
        Gestor de Catálogo de Películas
      </h1>
      <p class="subtitle">
        SPA Reactiva &mdash; Los datos mandan sobre la vista
      </p>
    </header>

    <MovieForm @add-movie="addMovie" />

    <section class="toolbar">
      <div class="filter-buttons">
        <button
          :class="['filter-btn', { active: filter === 'all' }]"
          @click="filter = 'all'"
        >
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M3.375 19.5h17.25m-17.25 0a1.125 1.125 0 0 1-1.125-1.125M3.375 19.5h1.5C5.496 19.5 6 18.996 6 18.375m-3.75.125H18m0 0a1.125 1.125 0 0 0 1.125-1.125M18 18.375V15m0 0H6.75v3.375M18 15V5.625M18 15H6.75m11.25 0h-11.25" /></svg>
          Todas ({{ totalCount }})
        </button>
        <button
          :class="['filter-btn', 'filter-btn--modern', { active: filter === 'modern' }]"
          @click="filter = 'modern'"
        >
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M11.48 3.499a.562.562 0 0 1 1.04 0l2.125 5.111a.563.563 0 0 0 .475.345l5.518.442c.499.04.701.663.321.988l-4.204 3.602a.563.563 0 0 0-.182.557l1.285 5.385a.562.562 0 0 1-.84.61l-4.725-2.885a.562.562 0 0 0-.586 0L6.982 20.54a.562.562 0 0 1-.84-.61l1.285-5.386a.562.562 0 0 0-.182-.557l-4.204-3.602a.562.562 0 0 1 .321-.988l5.518-.442a.563.563 0 0 0 .475-.345L11.48 3.5Z" /></svg>
          Modernas ({{ modernCount }})
        </button>
        <button
          :class="['filter-btn', 'filter-btn--classic', { active: filter === 'classic' }]"
          @click="filter = 'classic'"
        >
          <svg class="icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 6v6h4.5m4.5 0a9 9 0 1 1-18 0 9 9 0 0 1 18 0Z" /></svg>
          Clásicas ({{ classicCount }})
        </button>
      </div>

      <div class="search-box">
        <svg class="search-icon" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="m21 21-5.197-5.197m0 0A7.5 7.5 0 1 0 5.196 15.803a7.5 7.5 0 0 0 10.607 0Z" /></svg>
        <input
          v-model="searchQuery"
          type="text"
          placeholder="Buscar por nombre, género o año..."
        />
      </div>
    </section>

    <p class="results-count">
      Mostrando <strong>{{ filteredMovies.length }}</strong> de
      <strong>{{ totalCount }}</strong> películas
    </p>

    <MovieList :movies="filteredMovies" @delete-movie="deleteMovie" />
  </div>
</template>

<style>
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

:root {
  --bg: #121212;
  --bg-card: #1e1e1e;
  --border: #333;
  --accent: #e94560;
  --green: #4caf50;
  --text: #e0e0e0;
  --text-muted: #888;
}

.icon {
  width: 1em;
  height: 1em;
  display: inline-block;
  vertical-align: -0.15em;
  flex-shrink: 0;
}

body {
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: var(--bg);
  color: var(--text);
  min-height: 100vh;
  line-height: 1.5;
}

.app {
  max-width: 1000px;
  margin: 0 auto;
  padding: 2rem 1rem;
}

.app-header {
  text-align: center;
  margin-bottom: 1.5rem;
}

.app-header h1 {
  font-size: 1.8rem;
  color: var(--accent);
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 0.4rem;
}

.subtitle {
  color: var(--text-muted);
  font-size: 0.9rem;
}

.toolbar {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
  align-items: center;
  justify-content: space-between;
  margin-bottom: 1rem;
}

.filter-buttons {
  display: flex;
  gap: 0.4rem;
}

.filter-btn {
  padding: 0.4rem 0.9rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: transparent;
  color: var(--text-muted);
  font-size: 0.85rem;
  cursor: pointer;
  display: inline-flex;
  align-items: center;
  gap: 0.35rem;
}

.filter-btn:hover {
  border-color: var(--accent);
  color: var(--text);
}

.filter-btn.active {
  background: var(--accent);
  border-color: var(--accent);
  color: #fff;
}

.filter-btn--modern.active {
  background: var(--green);
  border-color: var(--green);
}

.search-box {
  position: relative;
  display: flex;
  align-items: center;
}

.search-icon {
  position: absolute;
  left: 0.65rem;
  width: 1rem;
  height: 1rem;
  color: #555;
  pointer-events: none;
}

.search-box input {
  padding: 0.45rem 0.8rem 0.45rem 2.2rem;
  border: 1px solid var(--border);
  border-radius: 6px;
  background: var(--bg-card);
  color: var(--text);
  font-size: 0.85rem;
  width: 260px;
  max-width: 100%;
}

.search-box input:focus {
  outline: none;
  border-color: var(--accent);
}

.search-box input::placeholder {
  color: #555;
}

.results-count {
  color: var(--text-muted);
  font-size: 0.8rem;
  margin-bottom: 1rem;
}

.results-count strong {
  color: var(--accent);
}
</style>
