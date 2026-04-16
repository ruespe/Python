<script setup>
import './ProfileCard.css';
defineProps({
  name: String,
  city: String,
  tech: String,
});
</script>

<template>
  <div class="card">
    <div class="card-header">
      <span class="avatar">
        <img src="/images/avatar-svgrepo-com.svg" alt="Avatar" class="icon-img" />
      </span>
      <h2 class="card-name">{{ name }}</h2>
    </div>
    <div class="card-body">
      <p class="card-line">
        <span class="icon">
          <img src="/images/location-pin-svgrepo-com.svg" alt="Ubicación" class="icon-img" />
        </span>
        <span>{{ city || "—" }}</span>
      </p>
      <p class="card-line">
        <span class="icon">
          <img src="/images/laptop-svgrepo-com.svg" alt="Tecnología" class="icon-img" />
        </span>
        <span>Le gusta <strong>{{ tech || "—" }}</strong></span>
      </p>
    </div>
  </div>
</template>

