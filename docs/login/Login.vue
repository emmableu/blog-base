<template>
  <div class="login-form">
    <div class="form-header">用户名</div>
    <div>
      <input type="text" class="form-control" v-model="username">
    </div>
    <div class="form-header">密码</div>
    <div>
      <input type="password" class="form-control" v-model="password">
    </div>

    <div class="btn-row">
      <button class="btn" @click="login">
        OK
      </button>
    </div>
  </div>
</template>

<script>
import {checkAuth, STORAGE_KEY} from './helper'

export default {
  data () {
    return {
      username: '',
      password: ''
    }
  },
  methods: {
    login () {
      if (this.username && this.password) {
        const data = JSON.stringify({
          name: this.username,
          password: this.password,
        })
        // 登录成功后的逻辑处理，这里将数据保存在 localStorage 中仅作为功能演示
        window.localStorage.setItem(STORAGE_KEY, data)
        if (checkAuth()) {
          this.$emit('close', true)
        }
        else {
          this.$dlg.alert('用户名密码错误！', {
            messageType: 'warning'
          })
        }
      } else {
        this.$dlg.alert('Please complete the content', {
          messageType: 'warning'
        })
      }
    }
  }
}
</script>

<style lang="stylus">
.v-dialog-overlay
  opacity: 1 !important
  background-color: darkgrey !important
.login-form
  padding: 1rem
  display flex
  flex-direction column
  box-sizing border-box
  .btn-row
    margin-top 1rem
  .btn
    padding 0.6rem 2rem
    outline none
    background-color #60C084
    color white
    border 0
  .form-header
    color #666
    margin-bottom 0.5rem
  .form-control
    padding 0.6rem
    border 2px solid #ddd
    width 100%
    margin-bottom 0.5rem
    box-sizing border-box
    outline none
    transition border 0.2s ease
    &:focus
      border 2px solid #aaa
</style>
