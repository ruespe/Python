<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'

const router = useRouter()

// Estat del formulari
const username = ref('')
const password = ref('')
const error = ref('')
const carregant = ref(false)
const mode = ref('login') // 'login' o 'register'

async function enviar() {
  error.value = ''
  carregant.value = true

  const endpoint = mode.value === 'login' ? '/api/auth/login/' : '/api/auth/register/'

  try {
    const res = await fetch(endpoint, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ username: username.value, password: password.value }),
      credentials: 'same-origin',
    })
    const data = await res.json()

    if (data.ok) {
      router.push('/joc')
    } else {
      error.value = data.error || 'Error desconegut'
    }
  } catch {
    error.value = 'Error de connexió amb el servidor'
  } finally {
    carregant.value = false
  }
}

function canviarMode() {
  mode.value = mode.value === 'login' ? 'register' : 'login'
  error.value = ''
}
</script>

<template>
  <div class="login-container">
    <div class="login-card">
      <div class="logo">🕵️</div>
      <h1>Cluedo Web</h1>
      <h2>{{ mode === 'login' ? 'Iniciar Sessió' : 'Crear Compte' }}</h2>

      <form @submit.prevent="enviar">
        <div class="form-group">
          <label for="username">Nom d'usuari</label>
          <input
            id="username"
            v-model="username"
            type="text"
            placeholder="Introdueix el teu usuari"
            required
            autocomplete="username"
          />
        </div>

        <div class="form-group">
          <label for="password">Contrasenya</label>
          <input
            id="password"
            v-model="password"
            type="password"
            placeholder="Introdueix la contrasenya"
            required
            autocomplete="current-password"
          />
        </div>

        <p v-if="error" class="missatge-error">{{ error }}</p>

        <button type="submit" :disabled="carregant">
          {{ carregant ? 'Carregant...' : (mode === 'login' ? 'Entrar' : 'Registrar-se') }}
        </button>
      </form>

      <p class="canviar-mode">
        {{ mode === 'login' ? "No tens compte?" : "Ja tens compte?" }}
        <a href="#" @click.prevent="canviarMode">
          {{ mode === 'login' ? "Registra't" : 'Inicia sessió' }}
        </a>
      </p>
    </div>
  </div>
</template>

<style scoped>
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  min-height: 80vh;
}

.login-card {
  background: #2d1500;
  border: 2px solid #d4a853;
  border-radius: 12px;
  padding: 40px;
  width: 100%;
  max-width: 420px;
  box-shadow: 0 8px 32px rgba(0, 0, 0, 0.5);
}

.logo {
  font-size: 3rem;
  text-align: center;
  margin-bottom: 8px;
}

h1 {
  text-align: center;
  font-size: 1.8rem;
  color: #d4a853;
  margin-bottom: 4px;
}

h2 {
  text-align: center;
  font-size: 1rem;
  color: #a0856a;
  margin-bottom: 30px;
  font-weight: normal;
}

.form-group {
  margin-bottom: 20px;
}

label {
  display: block;
  margin-bottom: 6px;
  color: #d4a853;
  font-size: 0.9rem;
}

input {
  width: 100%;
  padding: 12px;
  border-radius: 6px;
  border: 1px solid #5a3a1a;
  background: #1a0a00;
  color: #f0e6d3;
  font-size: 1rem;
  transition: border-color 0.2s;
}

input:focus {
  outline: none;
  border-color: #d4a853;
}

button {
  width: 100%;
  padding: 13px;
  background: #8b1a1a;
  color: white;
  border: none;
  border-radius: 6px;
  font-size: 1rem;
  cursor: pointer;
  font-family: inherit;
  font-weight: bold;
  transition: background 0.2s;
}

button:hover:not(:disabled) {
  background: #a52020;
}

button:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

.missatge-error {
  color: #ff7b7b;
  margin-bottom: 15px;
  text-align: center;
  font-size: 0.9rem;
  padding: 8px;
  background: rgba(139, 26, 26, 0.3);
  border-radius: 4px;
}

.canviar-mode {
  text-align: center;
  margin-top: 20px;
  color: #a0856a;
  font-size: 0.9rem;
}

.canviar-mode a {
  color: #d4a853;
  text-decoration: none;
  font-weight: bold;
}

.canviar-mode a:hover {
  text-decoration: underline;
}
</style>
