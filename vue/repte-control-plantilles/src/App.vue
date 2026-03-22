<script setup>
import { ref } from 'vue'

const filtroActivo = ref(false)

const juegos = [
  {
    nombre: 'The Legend of Zelda: Breath of the Wild',
    año: 2017,
    genero: 'Aventura',
    imagen: '/images/the-legend-of-zelda-breath-of-the-wild-view-i111060.jpg',
  },
  {
    nombre: 'Minecraft',
    año: 2011,
    genero: 'Sandbox',
    imagen: '/images/yp0ad5n6swia1.jpg',
  },
  {
    nombre: 'Cyberpunk 2077',
    año: 2020,
    genero: 'RPG',
    imagen: '/images/artur-tarnowski-malemain.jpg',
  },
  {
    nombre: 'Red Dead Redemption 2',
    año: 2018,
    genero: 'Disparos en tercera persona',
    imagen: '/images/images.jfif',
  },
  {
    nombre: 'Max Payne',
    año: 2001,
    genero: 'Shooter',
    imagen: '/images/Maxpaynebox.jpg',
  },
  {
    nombre: 'Elden Ring',
    año: 2022,
    genero: 'RPG',
    imagen: '/images/614Y4NA6CVL._UF1000,1000_QL80_.jpg',
  },
]

const juegosMostrados = () => filtroActivo.value ? juegos.filter(j => j.año > 2015) : juegos
</script>

<template>
  <div class="app">
    <header>
      <h1>Catálogo de Videojuegos</h1>
      <p>Descubre los mejores títulos de la historia</p>
      <button
        :class="['btn', filtroActivo ? 'btn--actiu' : '']"
        @click="filtroActivo = !filtroActivo"
      >
        {{ filtroActivo ? '✅ Juegos modernos (> 2015)' : 'Mostrar solo juegos modernos' }}
      </button>
    </header>

    <main>
      <article v-for="juego in juegosMostrados()" :key="juego.nombre" class="targeta">
        <img :src="juego.imagen" :alt="juego.nombre" />
        <div class="targeta__info">
          <div class="targeta__cap">
            <h2>{{ juego.nombre }}</h2>
            <span v-if="juego.año > 2015" class="badge">⭐ Moderno</span>
          </div>
          <p class="targeta__meta">{{ juego.genero }} · {{ juego.año }}</p>
        </div>
      </article>
    </main>
  </div>
</template>

<style scoped>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

.app {
  font-family: 'Segoe UI', system-ui, sans-serif;
  background: #0d1117;
  color: #e6edf3;
  min-height: 100vh;
}

header {
  text-align: center;
  padding: 3rem 1.5rem 2.5rem;
  background: linear-gradient(160deg, #161b22, #0d1117);
  border-bottom: 1px solid #30363d;
}

header h1 {
  font-size: clamp(1.8rem, 4vw, 2.8rem);
  font-weight: 800;
  color: #58a6ff;
  margin-bottom: 0.4rem;
}

header p {
  color: #8b949e;
  margin-bottom: 1.5rem;
}

.btn {
  background: #21262d;
  color: #e6edf3;
  border: 1px solid #30363d;
  border-radius: 8px;
  padding: 0.6rem 1.4rem;
  font-size: 0.95rem;
  cursor: pointer;
  transition: border-color 0.2s, background 0.2s;
}
.btn:hover { border-color: #58a6ff; }
.btn--actiu {
  background: #1f3354;
  border-color: #58a6ff;
  color: #79c0ff;
  font-weight: 600;
}

main {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
  gap: 1.5rem;
  max-width: 1100px;
  margin: 0 auto;
  padding: 2.5rem 1.5rem;
}

.targeta {
  background: #161b22;
  border: 1px solid #30363d;
  border-radius: 12px;
  overflow: hidden;
  transition: transform 0.2s, box-shadow 0.2s, border-color 0.2s;
}
.targeta:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 28px rgba(88, 166, 255, 0.18);
  border-color: #58a6ff;
}
.targeta img {
  width: 100%;
  height: 170px;
  object-fit: cover;
  display: block;
}
.targeta__info { padding: 1rem 1.1rem 1.2rem; }
.targeta__cap {
  display: flex;
  align-items: flex-start;
  justify-content: space-between;
  gap: 0.5rem;
  margin-bottom: 0.35rem;
}
.targeta__cap h2 {
  font-size: 0.95rem;
  font-weight: 700;
  line-height: 1.3;
}
.badge {
  flex-shrink: 0;
  background: #3d2c00;
  color: #d29922;
  border: 1px solid #d29922;
  border-radius: 999px;
  font-size: 0.7rem;
  font-weight: 700;
  padding: 0.2rem 0.55rem;
  white-space: nowrap;
}
.targeta__meta { font-size: 0.82rem; color: #8b949e; }
</style>
