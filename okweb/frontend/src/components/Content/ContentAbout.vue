<template>
  <!-- Main Footer -->
  <!-- Choose between footer styles: "footer-type-1" or "footer-type-2" -->
  <!-- Add class "sticky" to  always stick the footer to the end of page (if page contents is small) -->
  <!-- Or class "fixed" to  always fix the footer to the end of page -->
  <div class="row" id="about">
    <div class="col-md-12">
      <div class="panel panel-default">
        <!-- 关于网站 -->
        <h4 class="text-gray">关于网站</h4>
        <div class="panel-body">
          <div class="row">
            <div class="col-sm-12">
              <blockquote>
                <!--<p>有一段时间我发现我的收藏夹越来越多，很难找到某个不常用的网站。所以就有了这个网站，这里收集的基本都是我自己浏览器收藏夹里的网站，我平时用的相对比较多的一些都在这里。</p>
                </br>
                <p>如果你也是设计师，如果你也正好喜欢设计，那希望这个网站能给你带来一些作用。</p>
                <p>闲聊或者有任何建议都可以加QQ群交流：304584722</p>-->
                <p>
                  一直以来我都使用Chrome的收藏夹来整理网站，
                  直到收藏的网站越来越多，收藏夹也越来越多，
                  当想要回头需要参考的时候找的时候就比较麻烦了，
                  所以一直想做一个网址导航，贴上自己比较常用的一些网站
                </p>
                <br />
                <p>
                  某些工具或者现成的网站虽然也能满足自己的部分需求，但是可定制性又不强，
                  自己刚好翻到一个设计师 <a href="https://github.com/WebStackPage/WebStackPage.github.io" target="_blank"> Designer. Viggo. </a>
                  写的设计师导航网站，感觉和自己的设想、思路都比较契合，
                  经过三天的改造，于是就有了本站。
                </p>
                <br />
                <p>
                  如果你对本站有任何的疑问或者建议，欢迎随时邮件与我交流：<a href="mailto:jiangtao.work@gmail.com"><img src="../../assets/images/logos/baseline-email-24px.svg" width="24" alt="email"></a>
                </p>
              </blockquote>
            </div>
          </div>
          <!-- 关于站长 -->
          <h4 class="text-gray">关于站长</h4>
          <div class="row">
            <div class="col-sm-4">
              <ContentCard :site="site" />
            </div>
            <div class="col-md-8">
              <div class="row">
                <div class="col-sm-12">
                  <br />
                  <blockquote>
                    <p>
                      <!--这是一个公益项目，而且是<a href="https://github.com/WebStackPage/WebStackPage.github.io"> 开源 </a>的。你也可以拿来制作自己的网址导航。如果你有更好的想法，可以通过个人网站<a href="http://www.viggoz.com"><span class="label label-info" data-toggle="tooltip" data-placement="left" title="" data-original-title="Hello I am a Tooltip">viggoz.com</span></a>中的联系方式找到我，欢迎与我交流分享。-->
                      站长长期专职写后台，主要语言为 <i>Python</i>，
                      建立本站的目的就是提高自己的效率，
                      如果刚好有幸能够帮到你，也会给我带来一份成就，
                      技术无止境，期待与你交流。
                    </p>
                  </blockquote>
                </div>
              </div>
              <!--<br>-->
            </div>
          </div>
          <!-- <h4 class="text-gray">反馈交流</h4>
          <div>
              <img src="../assets/images/WechatGroup.jpg" alt=""  style="width: 200px">
          </div> -->
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import ContentCard from "./ContentCard.vue";

export default {
  name: "ContentAbout",
  components: {
    ContentCard
  },
  data() {
    return {
      site: {
        name: "木先生",
        url: "https://www.hujiangtao.cn/",
        logo: require("../../assets/images/logos/hujiangtao_logo.jpg"),
        desc: "Full-time UI designer with an enduring interest in Coding."
      }
    };
  }
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
</style>
