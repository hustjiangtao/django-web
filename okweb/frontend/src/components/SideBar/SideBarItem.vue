<template>
  <li>
    <a :href="'#' + group" class="smooth">
      <i class="linecons-star"></i>
      <span class="title">{{ group }}</span>
    </a>
  </li>
</template>

<script>
export default {
  name: "SideBar",
  props: {
    group: String
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
