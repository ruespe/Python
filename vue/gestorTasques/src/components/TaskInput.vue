<script setup>
import { ref } from "vue";

const emit = defineEmits(["add-task"]);

const text = ref("");

function submit() {
  const trimmed = text.value.trim();
  if (!trimmed) return;
  emit("add-task", trimmed);
  text.value = "";
}
</script>

<template>
  <div class="task-input">
    <input
      v-model="text"
      type="text"
      placeholder="Escribe una tarea..."
      @keyup.enter="submit"
    />
    <button @click="submit">Añadir</button>
  </div>
</template>

<style scoped>
.task-input {
  display: flex;
  gap: 0.5rem;
  margin-bottom: 1.5rem;
}

input {
  flex: 1;
  padding: 0.5rem 0.75rem;
  font-size: 1rem;
  border: 2px solid #ccc;
  border-radius: 6px;
  outline: none;
  transition: border-color 0.2s;
}

input:focus {
  border-color: #42b883;
}

button {
  padding: 0.5rem 1.2rem;
  font-size: 1rem;
  background-color: #42b883;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #369870;
}
</style>
