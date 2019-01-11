<template>
  <!-- Main Footer -->
  <!-- Choose between footer styles: "footer-type-1" or "footer-type-2" -->
  <!-- Add class "sticky" to  always stick the footer to the end of page (if page contents is small) -->
  <!-- Or class "fixed" to  always fix the footer to the end of page -->
  <footer class="main-footer sticky footer-type-1">
    <div class="footer-inner">
      <!-- Add your copyright text here -->
      <div class="footer-text">
        &copy; {{ new Date().getFullYear() }}
        <a href="#about"><strong>WebStack</strong></a> build by <a href="https://www.hujiangtao.cn" target="_blank"><strong>木先生</strong></a>
      </div>
      <!-- Go to Top Link, just add rel="go-top" to any link to add this functionality -->
      <div class="go-up">
        <a href="#" rel="go-top">
          <i class="fa-angle-up"></i>
        </a>
      </div>
    </div>
  </footer>
</template>

<script>
export default {
  name: "ContentFooter"
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
footer {
  margin-top: 1rem !important;
}
</style>
