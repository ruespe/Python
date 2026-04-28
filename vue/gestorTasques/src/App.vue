<script setup>
import { ref } from "vue";
import TaskInput from "./components/TaskInput.vue";
import TaskList from "./components/TaskList.vue";

const tasks = ref([
  { id: 1, text: "Estudiar Vue" },
  { id: 2, text: "Hacer ejercicios" },
]);

let nextId = 3;

function addTask(text) {
  tasks.value.push({ id: nextId++, text });
}

function deleteTask(id) {
  tasks.value = tasks.value.filter((t) => t.id !== id);
}
</script>

<template>
  <main class="app">
    <h1>Gestor de Tareas</h1>
    <TaskInput @add-task="addTask" />
    <TaskList :tasks="tasks" @delete-task="deleteTask" />
  </main>
</template>

<style scoped>
.app {
  max-width: 600px;
  margin: 3rem auto;
  padding: 2rem;
  background: white;
  border-radius: 10px;
  box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
  font-family: Arial, sans-serif;
}

h1 {
  text-align: center;
  color: #2c3e50;
  margin-bottom: 1.5rem;
}
</style>
