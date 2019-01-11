<template>
  <div class="page-container">
    <SideBar :groups="group_names" />
    <Content :groups="groups" />
  </div>
</template>

<script>
// @ is an alias to /src
import Content from "@/components/Content/Content.vue";
import SideBar from "@/components/SideBar/SideBar.vue";
import axios from "axios";

// const url = "http://localhost:8000/webview/";
const url = "/webview/";

export default {
  name: "home",
  components: {
    Content,
    SideBar
  },
  data() {
    return {
      group_names: [],
      groups: []
    };
  },
  methods: {
    fetchData(url, obj, obj_names) {
      axios
        .get(url)
        .then(response => response.data)
        .then(data => {
          data.data.map(item => {
            obj.push(item);
            obj_names.push(item.name);
          });
        })
        .catch(console.log());
    }
  },
  created() {
    this.fetchData(url, this.groups, this.group_names);
  }
};
</script>
