<script setup lang="ts">
import axios from 'axios'
import { ref } from 'vue'

let userName = ref<string>("")

function getUser() {
  axios
    .get("/users")
    .then((res) => {
      userName.value = res.data
    })
    .catch((e) => {
      console.log('e:', e);
    })
}
</script>

<template>
  <div class="text-center">
    <p class="text-rose-500 text-3xl">Hello World</p>
    <button class="border p-1" @click="getUser" type="button">DBからユーザー情報取得</button>
    <div>{{ `ユーザー名：${userName}` }}</div>
  </div>
</template>

<style scoped>
</style>
