<template>
  <div class="sidebar-menu toggle-others fixed">
    <div class="sidebar-menu-inner">
      <header class="logo-env">
        <!-- logo -->
        <div class="logo">
          <a href="/" class="logo-expanded">
            <img src="../../assets/images/logo@2x.png" width="100%" alt="" />
          </a>
          <a href="/" class="logo-collapsed">
            <img src="../../assets/images/logo-collapsed@2x.png" width="40" alt="" />
          </a>
        </div>
        <div class="mobile-menu-toggle visible-xs">
          <!--<a href="#" data-toggle="user-info-menu">
            <i class="linecons-cog"></i>
          </a>-->
          <a href="#" data-toggle="mobile-menu">
            <i class="fa-bars"></i>
          </a>
        </div>
      </header>
      <ul id="main-menu" class="main-menu">
        <SideBarItem v-for="group in groups" :key="group.id" :group="group" />
      </ul>
      <ul class="main-menu">
        <li>
          <a href="#about">
            <i class="linecons-heart"></i>
            <span class="tooltip-blue">关于本站</span>
            <!--<span class="label label-Primary pull-right hidden-collapsed">♥︎</span>-->
          </a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
import SideBarItem from "./SideBarItem.vue";

export default {
  name: "SideBar",
  components: {
    SideBarItem
  },
  props: {
    groups: Array
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
@import "../Content/nav.css";
.sidebar-menu-inner {
  height: 100%;
  display: flex;
  flex-direction: column;
}
#main-menu {
  flex: 1;
}
</style>
