// import vue from 'vue/dist/vue.esm.browser'
export default ({
  Vue, // VuePress 正在使用的 Vue 构造函数
  options, // 附加到根实例的一些选项
  router, // 当前应用的路由实例
  siteData // 站点元数据
}) => {
  // window.Vue = vue // 使页面中可以使用Vue构造函数 （使页面中的vue demo生效）
}
// import { checkAuth } from '../login/helper'
// import Login from '../login/Login'

// export default ({
//   Vue,
//   options,
//   router,
//   siteData
// }) => {
//   Vue.mixin({
//     mounted() {
//       const doCheck = () => {
//         if (!checkAuth()) {
//           this.$dlg.modal(Login, {
//             width: 300,
//             height: 350,
//             title: 'Employee login',
//             singletonKey: 'employee-login',
//             maxButton: false,
//             closeButton: false,
//             callback: data => {
//               if (data === true) {
//                 // do some stuff after login
//               }
//             }
//           })
//         }
//       }

//       if (this.$dlg) {
//         doCheck()
//       } else {
//         import('v-dialogs').then(resp => {
//           Vue.use(resp.default)
//           this.$nextTick(() => {
//             doCheck()
//           })
//         })
//       }
//     }
//   })
// }