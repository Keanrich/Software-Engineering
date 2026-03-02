<script>
    import axios from 'axios';
    export default {
    data() {
        return {
        form: {
            username: '',
            password: ''
        }
        };
    },
    methods: {
        async login() {
        try {
            const response = await axios.post("http://localhost:5000/login", this.form);
            console.log(response.user_id)
            localStorage.setItem("user_id", response.data.user_id);
            this.$router.push("/home");
        } catch (error) {
            alert(error.response?.data?.message || "Login failed");
            this.form = {
            username: '',
            password: ''
            }
        }
    }
    } 
    };
</script>

<template>
    <div class="flex justify-center items-center h-screen bg-[#17a6ee]">
        <div class="w-80 p-8 rounded-xl shadow-lg bg-[#cddbe9]">
        <h2 class="text-center text-lg font-semibold text-[#36454F] mb-8">LOGIN</h2>

        <form @submit.prevent="login">
            <div class="mb-6">
            <label class="block text-[#36454F] font-semibold mb-2">Username</label>
            <input
                type="text"
                v-model="form.username"
                required @keyup.enter="login"
                class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F]"
            />
            </div>

            <div class="mb-6">
            <label class="block text-[#36454F] font-semibold mb-2">Password</label>
            <input
                type="password"
                v-model="form.password"
                required @keyup.enter="login"
                class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F]"
            />
            </div>

            <div class="text-center">
            <button
                type="submit"
                class="bg-[#36454F] text-white px-6 py-2 rounded hover:bg-[#2a363e] transition"
            >
                Submit
            </button>
            </div>
        </form>
        </div>
    </div>
</template>


