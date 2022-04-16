<template>
    <div>
        <form>
            <input class="mr-2" v-model="number" type="text" />
            <b-button
                class="mr-1"
                lg="4"
                size="sm"
                variant="success"
                type="button"
                @click="submitFormGet()"
                >Submit</b-button
            >
            <b-button
                variant="success"
                size="sm"
                :disabled="loading"
                type="button"
                @click="clearAll()"
            >
                Clear
            </b-button>
        </form>
        <div class="mt-3">
            <p>{{ getResponse }}</p>
        </div>
        <div>
            <b-spinner v-if="loading" variant="info"></b-spinner>
        </div>
        <div>
            <p>{{ postResponse }}</p>
        </div>
    </div>
</template>

<script>
import { axiosInstance } from "../main";

export default {
    name: "NumToEnglish",
    data: () => {
        return {
            number: "",
            getResponse: "",
            postResponse: "",
            loading: false,
        };
    },
    methods: {
        submitFormGet() {
            this.loading = true;
            this.getResponse = "";
            axiosInstance
                .get(
                    "http://127.0.0.1:8000/api/num_to_english/?number=" +
                        this.number
                )
                .then((response) => {
                    this.loading = false;

                    if (this.handleResponse(response.data)) {
                        this.getResponse = response.data.num_in_english;
                        this.submitFormPost();
                    }
                });
        },
        async submitFormPost() {
            this.loading = true;
            this.postResponse = "";
            await new Promise((resolve) => setTimeout(resolve, 5000));
            await axiosInstance
                .post("num_to_english/", {
                    number: this.number,
                })
                .then((response) => {
                    this.postResponse = response.data.num_in_english;
                    this.loading = false;
                })
                .catch(() => {
                    this.showErrorToast();
                });
        },
        handleResponse(data) {
            if (data.status == "ok") {
                return true;
            } else {
                this.showErrorToast(data.num_in_english);
                return false;
            }
        },
        showErrorToast(message = "An unexpected error has occurred.") {
            this.$bvToast.toast(message, {
                title: "Error: ",
                appendToast: true,
                toaster: "b-toaster-bottom-center",
                variant: "warning",
            });
        },
        clearAll() {
            this.number = "";
            this.postResponse = "";
            this.getResponse = "";
        },
    },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped></style>
