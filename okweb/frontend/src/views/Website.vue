<template>
  <div class="web-view">
    <SiteItem :site_list="site_list" />
  </div>
</template>

<script>
// @ is an alias to /src
import SiteItem from "@/components/SiteItem.vue";
import axios from "axios";

const url = "http://localhost:8000/webview/";

export default {
  name: "home",
  components: {
    SiteItem
  },
  data() {
    return {
      site_list: []
    };
  },
  methods: {
    fetchData(url, obj) {
      axios
        .get(url)
        .then(response => response.data)
        .then(data => {
          data.data.map(item => {
            obj.push(item);
          });
        })
        .catch(console.log());
    }
  },
  created() {
    this.fetchData(url, this.site_list);
  }
};
</script>
