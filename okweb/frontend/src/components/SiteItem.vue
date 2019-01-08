<template>
  <div class="hello">
    <ul v-for="site in site_list" :key="site.id">
      <li class="site-outer-box">
        <div class="site-inner-box">
          <img :src="site.favicon" alt="favicon" class="site-favicon" />
          <a :href="site.url" target="_blank" rel="noopener">{{ site.name }}</a>
          <p>{{ site.desc }}</p>
        </div>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  props: {
    msg: String,
    site_list: Array
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
.site-outer-box {
  float: left;
}
.site-inner-box {
  cursor: pointer;
  height: 1rem;
  border: 1px solid #e4ecf3;
  border-radius: 4px;
  margin: 20px 0 0 0;
  padding: 1rem;
  transition: all 0.3s ease;
  position: relative;
  background: #fff;
}
.site-favicon {
  margin-right: 0.5rem;
}
</style>
