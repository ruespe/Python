<script setup>
import { ref, computed, onMounted, onUnmounted } from 'vue'

// --- Dades del joc ---
const personatges = ref([])
const armes = ref([])
const habitacions = ref([])

// --- Estat de la partida ---
const solucioId = ref(null)
const numIntents = ref(0)

// --- Seleccions de l'usuari ---
const personatgeSeleccionat = ref(null)
const armaSeleccionada = ref(null)
const habitacioSeleccionada = ref(null)

// --- Resultat de l'acusació ---
const resultat = ref(null)
const guanyat = ref(false)
const carregant = ref(false)
const missatgeError = ref('')

// --- Cronòmetre ---
const tempsSegons = ref(0)
let intervalId = null

const tempsFormatat = computed(() => {
  const m = Math.floor(tempsSegons.value / 60)
  const s = tempsSegons.value % 60
  return `${String(m).padStart(2, '0')}:${String(s).padStart(2, '0')}`
})

function iniciarCronòmetre() {
  if (intervalId) return
  intervalId = setInterval(() => { tempsSegons.value++ }, 1000)
}

function aturarCronòmetre() {
  clearInterval(intervalId)
  intervalId = null
}

onUnmounted(() => aturarCronòmetre())

// --- Carrega dades i partida ---
async function carregarDades() {
  const [resP, resA, resH] = await Promise.all([
    fetch('/api/personatges/'),
    fetch('/api/armes/'),
    fetch('/api/habitacions/'),
  ])
  personatges.value = await resP.json()
  armes.value = await resA.json()
  habitacions.value = await resH.json()
}

async function iniciarOContinuarPartida() {
  // Comprova si hi ha una partida activa
  const res = await fetch('/api/partida-activa/', { credentials: 'same-origin' })
  const data = await res.json()

  if (data.activa) {
    // Continuem la partida existent
    solucioId.value = data.solucio_id
    numIntents.value = data.num_intents
  } else {
    // Iniciem una nova partida
    const res2 = await fetch('/api/nova-partida/', {
      method: 'POST',
      credentials: 'same-origin',
    })
    const data2 = await res2.json()
    solucioId.value = data2.solucio_id
    numIntents.value = 0
  }

  iniciarCronòmetre()
}

// --- Acusació ---
async function acusar() {
  missatgeError.value = ''

  if (!personatgeSeleccionat.value || !armaSeleccionada.value || !habitacioSeleccionada.value) {
    missatgeError.value = 'Has de seleccionar un personatge, una arma i una habitació!'
    return
  }

  carregant.value = true
  resultat.value = null

  try {
    const res = await fetch('/api/acusar/', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      credentials: 'same-origin',
      body: JSON.stringify({
        solucio_id: solucioId.value,
        personatge_id: personatgeSeleccionat.value,
        arma_id: armaSeleccionada.value,
        habitacio_id: habitacioSeleccionada.value,
        temps: tempsSegons.value,
      }),
    })

    const data = await res.json()
    resultat.value = data
    numIntents.value = data.num_intent

    if (data.correcte) {
      guanyat.value = true
      aturarCronòmetre()
    }
  } catch {
    missatgeError.value = 'Error de connexió amb el servidor'
  } finally {
    carregant.value = false
  }
}

// --- Nova partida ---
async function novaPartida() {
  aturarCronòmetre()
  tempsSegons.value = 0
  resultat.value = null
  guanyat.value = false
  numIntents.value = 0
  personatgeSeleccionat.value = null
  armaSeleccionada.value = null
  habitacioSeleccionada.value = null
  missatgeError.value = ''

  const res = await fetch('/api/nova-partida/', {
    method: 'POST',
    credentials: 'same-origin',
  })
  const data = await res.json()
  solucioId.value = data.solucio_id
  iniciarCronòmetre()
}

onMounted(async () => {
  await carregarDades()
  await iniciarOContinuarPartida()
})
</script>

<template>
  <div class="joc">
    <!-- Capçalera de la partida -->
    <div class="capçalera">
      <div class="info-partida">
        <span class="badge">⏱ {{ tempsFormatat }}</span>
        <span class="badge">🔍 Intent #{{ numIntents }}</span>
      </div>
      <h1>🔎 La Mansió del Misteri</h1>
      <p class="subtitol">Descobreix qui va ser, amb quina arma i on va cometre el crim!</p>
    </div>

    <!-- Pantalla de victòria -->
    <div v-if="guanyat" class="victoria">
      <div class="victoria-card">
        <div class="victoria-emoji">🏆</div>
        <h2>¡Cas resolt!</h2>
        <p>Has resolt el misteri en <strong>{{ numIntents }} intent{{ numIntents !== 1 ? 's' : '' }}</strong>
        i <strong>{{ tempsFormatat }}</strong>.</p>
        <div v-if="resultat" class="solucio-final">
          <p>🧑 <strong>{{ personatges.find(p => p.id === personatgeSeleccionat)?.nom }}</strong></p>
          <p>🔪 <strong>{{ armes.find(a => a.id === armaSeleccionada)?.nom }}</strong></p>
          <p>🚪 <strong>{{ habitacions.find(h => h.id === habitacioSeleccionada)?.nom }}</strong></p>
        </div>
        <button class="btn-nova" @click="novaPartida">Nova Partida</button>
      </div>
    </div>

    <!-- Formulari d'acusació -->
    <div v-else class="formulari">
      <!-- Selector de Personatge -->
      <div class="selector-grup">
        <h3>🧑 Sospitós</h3>
        <div class="opcions">
          <button
            v-for="p in personatges"
            :key="p.id"
            class="opcio"
            :class="{ seleccionat: personatgeSeleccionat === p.id }"
            @click="personatgeSeleccionat = p.id"
            :title="p.descripcio"
          >
            {{ p.nom }}
          </button>
        </div>
      </div>

      <!-- Selector d'Arma -->
      <div class="selector-grup">
        <h3>🔪 Arma del Crim</h3>
        <div class="opcions">
          <button
            v-for="a in armes"
            :key="a.id"
            class="opcio"
            :class="{ seleccionat: armaSeleccionada === a.id }"
            @click="armaSeleccionada = a.id"
            :title="a.descripcio"
          >
            {{ a.nom }}
          </button>
        </div>
      </div>

      <!-- Selector d'Habitació -->
      <div class="selector-grup">
        <h3>🚪 Lloc del Crim</h3>
        <div class="opcions">
          <button
            v-for="h in habitacions"
            :key="h.id"
            class="opcio"
            :class="{ seleccionat: habitacioSeleccionada === h.id }"
            @click="habitacioSeleccionada = h.id"
            :title="h.descripcio"
          >
            {{ h.nom }}
          </button>
        </div>
      </div>

      <!-- Error de validació -->
      <p v-if="missatgeError" class="missatge-error">{{ missatgeError }}</p>

      <!-- Resultat de l'intent anterior -->
      <div v-if="resultat && !guanyat" class="feedback">
        <h3>Resultat de l'acusació anterior:</h3>
        <div class="feedback-items">
          <span :class="['feedback-item', resultat.encert_personatge ? 'encert' : 'error']">
            {{ resultat.encert_personatge ? '✅' : '❌' }} Sospitós
          </span>
          <span :class="['feedback-item', resultat.encert_arma ? 'encert' : 'error']">
            {{ resultat.encert_arma ? '✅' : '❌' }} Arma
          </span>
          <span :class="['feedback-item', resultat.encert_habitacio ? 'encert' : 'error']">
            {{ resultat.encert_habitacio ? '✅' : '❌' }} Habitació
          </span>
        </div>
        <p class="pista">Torna-ho a intentar! Alguns elements poden ser correctes.</p>
      </div>

      <!-- Botó d'acusació -->
      <button class="btn-acusar" :disabled="carregant" @click="acusar">
        {{ carregant ? 'Comprovant...' : '⚖️ Fer Acusació' }}
      </button>
    </div>
  </div>
</template>

<style scoped>
.joc {
  max-width: 800px;
  margin: 0 auto;
}

.capçalera {
  text-align: center;
  margin-bottom: 30px;
}

.capçalera h1 {
  font-size: 2rem;
  color: #d4a853;
  margin-bottom: 8px;
}

.subtitol {
  color: #a0856a;
  font-style: italic;
}

.info-partida {
  display: flex;
  gap: 15px;
  justify-content: center;
  margin-bottom: 15px;
}

.badge {
  background: #2d1500;
  border: 1px solid #d4a853;
  color: #d4a853;
  padding: 6px 14px;
  border-radius: 20px;
  font-size: 0.9rem;
  font-weight: bold;
}

/* Formulari */
.formulari {
  display: flex;
  flex-direction: column;
  gap: 25px;
}

.selector-grup h3 {
  color: #d4a853;
  margin-bottom: 12px;
  font-size: 1.1rem;
  border-bottom: 1px solid #5a3a1a;
  padding-bottom: 6px;
}

.opcions {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}

.opcio {
  padding: 10px 18px;
  background: #1a0a00;
  border: 2px solid #5a3a1a;
  color: #f0e6d3;
  border-radius: 8px;
  cursor: pointer;
  font-family: inherit;
  font-size: 0.95rem;
  transition: all 0.2s;
}

.opcio:hover {
  border-color: #d4a853;
  background: #2d1500;
}

.opcio.seleccionat {
  border-color: #d4a853;
  background: #4a2500;
  color: #d4a853;
  font-weight: bold;
}

/* Feedback */
.feedback {
  background: #2d1500;
  border: 1px solid #5a3a1a;
  border-radius: 8px;
  padding: 20px;
}

.feedback h3 {
  color: #d4a853;
  margin-bottom: 12px;
}

.feedback-items {
  display: flex;
  gap: 15px;
  flex-wrap: wrap;
  margin-bottom: 10px;
}

.feedback-item {
  padding: 8px 16px;
  border-radius: 6px;
  font-weight: bold;
  font-size: 0.95rem;
}

.feedback-item.encert {
  background: rgba(34, 139, 34, 0.2);
  border: 1px solid #228b22;
  color: #90ee90;
}

.feedback-item.error {
  background: rgba(139, 26, 26, 0.3);
  border: 1px solid #8b1a1a;
  color: #ff9999;
}

.pista {
  color: #a0856a;
  font-style: italic;
  font-size: 0.9rem;
}

/* Errors i botons */
.missatge-error {
  color: #ff7b7b;
  text-align: center;
  padding: 10px;
  background: rgba(139, 26, 26, 0.3);
  border-radius: 6px;
}

.btn-acusar {
  padding: 15px;
  background: #8b1a1a;
  color: white;
  border: none;
  border-radius: 8px;
  font-size: 1.1rem;
  font-weight: bold;
  cursor: pointer;
  font-family: inherit;
  transition: background 0.2s;
}

.btn-acusar:hover:not(:disabled) {
  background: #a52020;
}

.btn-acusar:disabled {
  opacity: 0.6;
  cursor: not-allowed;
}

/* Victòria */
.victoria {
  display: flex;
  justify-content: center;
  align-items: center;
  padding: 30px 0;
}

.victoria-card {
  background: #2d1500;
  border: 3px solid #d4a853;
  border-radius: 16px;
  padding: 40px;
  text-align: center;
  max-width: 450px;
  box-shadow: 0 0 40px rgba(212, 168, 83, 0.3);
}

.victoria-emoji {
  font-size: 4rem;
  margin-bottom: 15px;
}

.victoria-card h2 {
  color: #d4a853;
  font-size: 2rem;
  margin-bottom: 15px;
}

.victoria-card p {
  color: #f0e6d3;
  margin-bottom: 10px;
  font-size: 1.05rem;
}

.solucio-final {
  background: #1a0a00;
  border-radius: 8px;
  padding: 15px;
  margin: 20px 0;
  text-align: left;
}

.solucio-final p {
  margin-bottom: 8px;
}

.btn-nova {
  padding: 12px 30px;
  background: #d4a853;
  color: #1a0a00;
  border: none;
  border-radius: 8px;
  font-size: 1rem;
  font-weight: bold;
  cursor: pointer;
  font-family: inherit;
  margin-top: 10px;
  transition: background 0.2s;
}

.btn-nova:hover {
  background: #f0c878;
}
</style>
