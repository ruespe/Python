<script setup>
defineProps({
  task: {
    type: Object,
    required: true,
  },
});

const emit = defineEmits(["delete-task"]);
</script>

<template>
  <li class="task-item">
    <span>{{ task.text }}</span>
    <button @click="emit('delete-task', task.id)">Eliminar</button>
  </li>
</template>

<style scoped>
.task-item {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 0.6rem 1rem;
  background: #f9f9f9;
  border: 1px solid #e0e0e0;
  border-radius: 6px;
  margin-bottom: 0.5rem;
}

span {
  font-size: 1rem;
}

button {
  padding: 0.3rem 0.8rem;
  font-size: 0.85rem;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background-color 0.2s;
}

button:hover {
  background-color: #c0392b;
}
</style>
