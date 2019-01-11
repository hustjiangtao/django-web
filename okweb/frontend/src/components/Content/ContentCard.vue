<template>
  <div class="xe-widget xe-conversations box2 label-info"
       v-on:click="handleClick"
       data-toggle="tooltip"
       data-placement="bottom"
       title=""
       :data-original-title="site.url"
  >
    <div class="xe-comment-entry">
      <a class="xe-user-img">
        <img :src="site.logo" class="img-circle" width="40">
        <!--<img :src="site.logo" class="img-circle" width="16">-->
      </a>
      <span class="label label-info" data-toggle="tooltip" data-placement="left" title="" data-original-title="Hello I am a Tooltip"></span>
      <div class="xe-comment">
        <a href="#" class="xe-user-name overflowClip_1">
          <strong>{{ site.name }}</strong>
        </a>
        <p class="overflowClip_2">{{ site.desc }}</p>
      </div>
    </div>
  </div>
</template>

<script>
export default {
  name: "ContentCard",
  props: {
    site: {
      name: String,
      url: String,
      logo: String,
      desc: String
    }
  },
  methods: {
    handleClick() {
      window.open(this.site.url, "_blank");
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "./nav.css";
</style>
