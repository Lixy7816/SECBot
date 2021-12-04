<!-- 图片很少,直接静态加载 -->
<template>
  <div>
  <el-row :gutter="20">
    <el-col :span="6" :offset="3">
      <el-card :body-style="{ padding: '10px' }" shadow="hover">
        <img src="../assets/chat.jpeg" class="image" alt=""/>
        <div class="undpic">
          <div class="bottom clearfix">
            <el-button type="text" class="button" v-on:click="chooseABot(1)">闲聊</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card :body-style="{ padding: '10px' }" shadow="hover">
        <img src="../assets/poem.jpeg" class="image" alt=""/>
        <div class="undpic">
          <div class="bottom clearfix">
            <el-button type="text" class="button" v-on:click="chooseABot(2)">诗词</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card :body-style="{padding: '10px'}" shadow="hover">
        <img src="../assets/Q_A.jpeg" class="image" alt=""/>
        <div class="undpic">
          <div class="bottom clearfix">
            <el-button type="text" class="button" v-on:click="chooseABot(3)">问答</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
  </el-row>
    <el-row :gutter="20">
    <el-col :span="6" :offset="6">
      <el-card :body-style="{ padding: '10px' }" shadow="hover">
        <img src="../assets/film.jpeg" class="image" alt=""/>
        <div class="undpic">
          <div class="bottom clearfix">
            <el-button type="text" class="button" v-on:click="chooseABot(4)">影视</el-button>
          </div>
        </div>
      </el-card>
    </el-col>
    <el-col :span="6">
      <el-card :body-style="{ padding: '10px' }" shadow="hover">
        <img src="../assets/other.jpeg" class="image" alt=""/>
          <div class="bottom clearfix">
            <el-button type="text" class="button">更多功能等待开发</el-button>
          </div>
      </el-card>
    </el-col>
  </el-row>
  </div>
</template>

<script>
export default {
  name: 'ChooseBot',
  methods: {
    chooseABot(index) {
      console.log('chooseABot', index);
      this.$emit('choseABot', index);
    }
  }
};
</script>

<style>
.el-row {
  margin-bottom: 15px;
}
.el-col {
  border-radius: 4px;
}
.time {
  font-size: 13px;
  color: #999;
}

.undpic {
  padding: 5px;
}

.bottom {
  margin-top: 13px;
  line-height: 12px;
}

.button {
  padding: 0;
  float: center;
}

.image {
  width: 99%;
  display: block;
  border-style: solid;
  border-width: 1px;
}

.clearfix:before,
.clearfix:after {
  display: table;
  content: "";
}

.clearfix:after {
  clear: both;
}
</style>
