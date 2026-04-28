<script setup>
import TaskItem from "./TaskItem.vue";

defineProps({
  tasks: {
    type: Array,
    required: true,
  },
});

const emit = defineEmits(["delete-task"]);
</script>

<template>
  <ul class="task-list">
    <TaskItem
      v-for="task in tasks"
      :key="task.id"
      :task="task"
      @delete-task="emit('delete-task', $event)"
    />
    <li v-if="tasks.length === 0" class="empty">No hay tareas pendientes.</li>
  </ul>
</template>

<style scoped>
.task-list {
  list-style: none;
  padding: 0;
  margin: 0;
}

.empty {
  text-align: center;
  color: #aaa;
  font-style: italic;
  padding: 1rem 0;
}
</style>
