<template>
  <div class="main-content">
    <nav class="navbar user-info-navbar" role="navigation">
      <!-- User Info, Notifications and Menu Bar -->
      <!-- Left links for user info navbar -->
      <ul class="user-info-menu left-links list-inline list-unstyled">
        <li class="hidden-sm hidden-xs">
          <a href="#" data-toggle="sidebar">
            <i class="fa-bars"></i>
          </a>
        </li>
        <!--<li class="dropdown hover-line language-switcher">
          <a href="../cn/index.html" class="dropdown-toggle" data-toggle="dropdown">
            <img src="../../assets/images/flags/flag-cn.png" alt="flag-cn" /> Chinese
          </a>
          <ul class="dropdown-menu languages">
            <li>
              <a href="../en/index.html">
                <img src="../../assets/images/flags/flag-us.png" alt="flag-us" /> English
              </a>
            </li>
            <li class="active">
              <a href="../cn/index.html">
                <img src="../../assets/images/flags/flag-cn.png" alt="flag-cn" /> Chinese
              </a>
            </li>
          </ul>
        </li>-->
      </ul>
      <!--<a href="https://github.com/WebStackPage/WebStackPage.github.io" target="_blank"><img style="position: absolute; top: 0; right: 0; border: 0;" src="https://s3.amazonaws.com/github/ribbons/forkme_right_darkblue_121621.png" alt="Fork me on GitHub"></a>-->
    </nav>

    <div class="content-detail">
      <!-- 关于本站 -->
      <!--<ContentAbout v-if="show_about" />-->
      <ContentAbout v-show="show_about" />
      <!-- END 关于本站 -->

      <!-- 常用推荐 -->
      <!--<div v-else>
        <ContentCard v-for="group in groups" :key="group.id" :group="group" />
      </div>-->
      <ContentCardGroup v-for="group in groups" :key="group.id" :group="group" v-show="!show_about" />
      <!-- END 常用推荐 -->
    </div>

    <!-- Main Footer -->
    <ContentFooter />
  </div>
</template>

<script>
import ContentCardGroup from "./ContentCardGroup.vue";
import ContentFooter from "./ContentFooter.vue";
import ContentAbout from "./ContentAbout.vue";

export default {
  name: "Content",
  components: {
    ContentCardGroup,
    ContentFooter,
    ContentAbout
  },
  props: {
    groups: Array
  },
  data() {
    return {
      show_about: this.compute_show_about()
    };
  },
  methods: {
    compute_show_about() {
      return window.location.hash == "#about" ? true : false;
    }
  },
  watch: {
    $route() {
      this.show_about = this.compute_show_about();
    }
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "./nav.css";
.main-content {
  height: 100%;
  display: flex;
  flex-direction: column;
}
.content-detail {
  flex: 1;
}
</style>
