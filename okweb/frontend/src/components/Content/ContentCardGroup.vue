<template>
  <div>
    <!-- 常用推荐 -->
    <h4 class="text-gray"><i class="linecons-tag" style="margin-right: 7px;" :id="group.name"></i>{{ group.name }}</h4>
    <div class="row">
      <div class="col-sm-3" v-for="site in group.sites" :key="site.id">
        <ContentCard :site="site" />
      </div>
    </div>
    <br />
    <!-- END 常用推荐 -->
  </div>
</template>

<script>
import ContentCard from "./ContentCard.vue";

export default {
  name: "ContentCardGroup",
  components: {
    ContentCard
  },
  props: {
    group: {
      name: String,
      sites: Array
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "./nav.css";
</style>
