import Vue from "vue";
import App from "./App.vue";
import VueCookies from "vue-cookies";
import axios from "axios";
import { BootstrapVue, IconsPlugin } from "bootstrap-vue";

Vue.config.productionTip = false;
Vue.use(VueCookies);
Vue.use(BootstrapVue);
Vue.use(IconsPlugin);

export const axiosInstance = axios.create({
    baseURL: "http://localhost:8000/api/",
    timeout: 1000,
    headers: {
        "x-csrftoken": Vue.$cookies.get("csrftoken"),
    },
    xsrfCookieName: "csrftoken",
    xsrfHeaderName: "x-csrftoken",
    withCredentials: true,
});

new Vue({
    render: (h) => h(App),
}).$mount("#app");
