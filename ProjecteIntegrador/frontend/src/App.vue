<script setup>
import { ref, onMounted } from "vue";
import { useRouter, useRoute } from "vue-router";

const router = useRouter();
const route = useRoute();
const username = ref("");
const carregantLogout = ref(false);

async function comprovarSessio() {
  const res = await fetch("/api/auth/me/", { credentials: "same-origin" });
  const data = await res.json();
  username.value = data.authenticated ? data.username : "";
}

async function logout() {
  carregantLogout.value = true;
  await fetch("/api/auth/logout/", {
    method: "POST",
    credentials: "same-origin",
  });
  username.value = "";
  carregantLogout.value = false;
  router.push("/login");
}

// Actualitza el nom d'usuari quan canvia la ruta
router.afterEach(() => comprovarSessio());

onMounted(() => comprovarSessio());
</script>

<template>
  <div id="app">
    <nav v-if="username && route.path !== '/login'">
      <span class="nav-brand">🕵️ Cluedo Web</span>
      <div class="nav-links">
        <router-link to="/joc">🎮 Joc</router-link>
        <router-link to="/historial">📜 Historial</router-link>
      </div>
      <div class="nav-user">
        <span class="nav-username">👤 {{ username }}</span>
        <button @click="logout" :disabled="carregantLogout">
          {{ carregantLogout ? "..." : "Sortir" }}
        </button>
      </div>
    </nav>

    <main>
      <router-view />
    </main>
  </div>
</template>

<style>
/* Reset i base global */
*,
*::before,
*::after {
  box-sizing: border-box;
  margin: 0;
  padding: 0;
}

body {
  font-family: "Georgia", serif;
  background: #1a0a00;
  color: #f0e6d3;
  min-height: 100vh;
}

#app {
  min-height: 100vh;
  display: flex;
  flex-direction: column;
}

/* Barra de navegació */
nav {
  display: flex;
  align-items: center;
  gap: 20px;
  padding: 14px 24px;
  background: #2d1500;
  border-bottom: 2px solid #d4a853;
  flex-wrap: wrap;
}

.nav-brand {
  font-size: 1.2rem;
  font-weight: bold;
  color: #d4a853;
  margin-right: auto;
}

.nav-links {
  display: flex;
  gap: 15px;
}

.nav-links a {
  color: #f0e6d3;
  text-decoration: none;
  padding: 6px 14px;
  border-radius: 6px;
  transition: background 0.2s;
  font-size: 0.95rem;
}

.nav-links a:hover,
.nav-links a.router-link-active {
  background: #4a2500;
  color: #d4a853;
}

.nav-user {
  display: flex;
  align-items: center;
  gap: 12px;
}

.nav-username {
  color: #a0856a;
  font-size: 0.9rem;
}

nav button {
  background: #8b1a1a;
  color: white;
  border: none;
  padding: 7px 16px;
  border-radius: 6px;
  cursor: pointer;
  font-family: inherit;
  font-size: 0.9rem;
  transition: background 0.2s;
}

nav button:hover:not(:disabled) {
  background: #a52020;
}

nav button:disabled {
  opacity: 0.6;
}

main {
  flex: 1;
  padding: 30px 20px;
  max-width: 900px;
  width: 100%;
  margin: 0 auto;
}
</style>
