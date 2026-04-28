<script setup>
import { ref, onMounted } from "vue";

const historial = ref([]);
const carregant = ref(true);
const partidesDesplegades = ref(new Set());

function formatarTemps(segons) {
  if (!segons && segons !== 0) return "—";
  const m = Math.floor(segons / 60);
  const s = segons % 60;
  return `${String(m).padStart(2, "0")}:${String(s).padStart(2, "0")}`;
}

function formatarData(isoString) {
  return new Date(isoString).toLocaleString("ca-ES", {
    day: "2-digit",
    month: "2-digit",
    year: "numeric",
    hour: "2-digit",
    minute: "2-digit",
  });
}

function togglePartida(id) {
  if (partidesDesplegades.value.has(id)) {
    partidesDesplegades.value.delete(id);
  } else {
    partidesDesplegades.value.add(id);
  }
  // Forcem la reactivitat creant un nou Set
  partidesDesplegades.value = new Set(partidesDesplegades.value);
}

onMounted(async () => {
  try {
    const res = await fetch("/api/historial/", { credentials: "same-origin" });
    historial.value = await res.json();
  } catch {
    historial.value = [];
  } finally {
    carregant.value = false;
  }
});
</script>

<template>
  <div class="historial">
    <div class="capçalera">
      <h1>📜 Historial de Partides</h1>
      <p class="subtitol">Totes les teves investigacions anteriors</p>
    </div>

    <!-- Estat de càrrega -->
    <div v-if="carregant" class="carregant">Carregant historial...</div>

    <!-- Sense partides -->
    <div v-else-if="historial.length === 0" class="buit">
      <p>🔍 Encara no has jugat cap partida.</p>
      <router-link to="/joc" class="btn-jugar">Comença a Jugar</router-link>
    </div>

    <!-- Llista de partides -->
    <div v-else class="llista">
      <div
        v-for="partida in historial"
        :key="partida.id"
        class="partida-card"
        :class="{ resolta: partida.resolta, 'no-resolta': !partida.resolta }"
      >
        <!-- Capçalera de la partida -->
        <div class="partida-header" @click="togglePartida(partida.id)">
          <div class="partida-info">
            <span
              class="estat-badge"
              :class="partida.resolta ? 'resolt' : 'pendent'"
            >
              {{ partida.resolta ? "✅ Resolta" : "⏳ En curs" }}
            </span>
            <span class="partida-data">{{
              formatarData(partida.creada_en)
            }}</span>
          </div>
          <div class="partida-stats">
            <span>🔍 {{ partida.num_intents }} intents</span>
            <span v-if="partida.resolta"
              >⏱ {{ formatarTemps(partida.temps_resolucio) }}</span
            >
            <span class="toggle-icon">{{
              partidesDesplegades.has(partida.id) ? "▲" : "▼"
            }}</span>
          </div>
        </div>

        <!-- Detalls dels intents -->
        <div v-if="partidesDesplegades.has(partida.id)" class="intents">
          <div v-if="partida.intents.length === 0" class="sense-intents">
            Sense intents registrats.
          </div>
          <div
            v-for="(intent, idx) in partida.intents"
            :key="idx"
            class="intent-fila"
            :class="{ correcte: intent.correcte }"
          >
            <span class="intent-num">#{{ idx + 1 }}</span>
            <span
              :class="['element', intent.encert_personatge ? 'encert' : 'fail']"
            >
              {{ intent.encert_personatge ? "✅" : "❌" }}
              {{ intent.personatge }}
            </span>
            <span :class="['element', intent.encert_arma ? 'encert' : 'fail']">
              {{ intent.encert_arma ? "✅" : "❌" }} {{ intent.arma }}
            </span>
            <span
              :class="['element', intent.encert_habitacio ? 'encert' : 'fail']"
            >
              {{ intent.encert_habitacio ? "✅" : "❌" }} {{ intent.habitacio }}
            </span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.historial {
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

.carregant {
  text-align: center;
  color: #a0856a;
  padding: 40px;
  font-size: 1.1rem;
}

.buit {
  text-align: center;
  padding: 60px 20px;
  color: #a0856a;
}

.buit p {
  font-size: 1.2rem;
  margin-bottom: 20px;
}

.btn-jugar {
  display: inline-block;
  padding: 12px 30px;
  background: #8b1a1a;
  color: white;
  border-radius: 8px;
  text-decoration: none;
  font-weight: bold;
  transition: background 0.2s;
}

.btn-jugar:hover {
  background: #a52020;
}

.llista {
  display: flex;
  flex-direction: column;
  gap: 15px;
}

.partida-card {
  background: #2d1500;
  border-radius: 10px;
  overflow: hidden;
  border: 1px solid #5a3a1a;
}

.partida-card.resolta {
  border-color: #d4a853;
}

.partida-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 16px 20px;
  cursor: pointer;
  transition: background 0.2s;
  flex-wrap: wrap;
  gap: 10px;
}

.partida-header:hover {
  background: #3d1f00;
}

.partida-info {
  display: flex;
  align-items: center;
  gap: 12px;
}

.estat-badge {
  padding: 4px 12px;
  border-radius: 12px;
  font-size: 0.85rem;
  font-weight: bold;
}

.estat-badge.resolt {
  background: rgba(34, 139, 34, 0.2);
  border: 1px solid #228b22;
  color: #90ee90;
}

.estat-badge.pendent {
  background: rgba(212, 168, 83, 0.2);
  border: 1px solid #d4a853;
  color: #d4a853;
}

.partida-data {
  color: #a0856a;
  font-size: 0.9rem;
}

.partida-stats {
  display: flex;
  align-items: center;
  gap: 15px;
  color: #a0856a;
  font-size: 0.9rem;
}

.toggle-icon {
  color: #d4a853;
  font-size: 0.8rem;
}

/* Detalls dels intents */
.intents {
  border-top: 1px solid #5a3a1a;
  padding: 15px 20px;
  display: flex;
  flex-direction: column;
  gap: 8px;
}

.sense-intents {
  color: #a0856a;
  font-style: italic;
  text-align: center;
  padding: 10px;
}

.intent-fila {
  display: flex;
  align-items: center;
  gap: 15px;
  padding: 10px 14px;
  background: #1a0a00;
  border-radius: 6px;
  border: 1px solid #3d1f00;
  flex-wrap: wrap;
}

.intent-fila.correcte {
  border-color: #d4a853;
  background: rgba(212, 168, 83, 0.05);
}

.intent-num {
  color: #a0856a;
  font-weight: bold;
  min-width: 30px;
  font-size: 0.85rem;
}

.element {
  font-size: 0.9rem;
  flex: 1;
  min-width: 150px;
}

.element.encert {
  color: #90ee90;
}

.element.fail {
  color: #ff9999;
}
</style>
