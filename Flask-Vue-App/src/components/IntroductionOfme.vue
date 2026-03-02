<script>
  import ScrollAnimation from './ScrollAnimation.vue';
  import axios from 'axios';
  export default {
    components: {
    ScrollAnimation
  },
      data() {
        return{
      user_id: '',
      userData:'',
      userPhoto:'',
      userISI:''
      }
    },
    mounted() {
      this.FetchSite();
    },
    methods: {
    async FetchSite() {
      const user_id = localStorage.getItem('user_id');
      try {
        const response = await axios.get(`http://localhost:5000/data-user/${user_id}`);
        this.userPhoto = response.data.user_foto;
        this.userISI = response.data.user_isi;
        console.log('Foto:', this.userPhoto);
        console.log('Isi:', this.userISI);
        console.log(this.userISI)
      } catch (error) {
        console.error('Gagal mengambil data:', error);
      }
    }
    }
  }
</script>
<template>
  <div class="container mx-auto px-4">
    <div class="flex p-4 justify-end-safe bg-[#8C8C8C] text-[#D8C9AE]">
      <div class="flex gap-3">
        <RouterLink to="/" class="px-3 py-1 rounded transition-colors duration-200"
        active-class="bg-[#D8C9AE] text-[#8C8C8C] font-semibold shadow-md">login</RouterLink>
          <RouterLink to="/home" class="px-3 py-1 rounded transition-colors duration-200"
        active-class="bg-[#D8C9AE] text-[#8C8C8C] font-semibold shadow-md">Home</RouterLink>
          <RouterLink to="/about" class="px-3 py-1 rounded transition-colors duration-200"
        active-class="bg-[#D8C9AE] text-[#8C8C8C] font-semibold shadow-md">About</RouterLink>
      </div>
    </div>
    <!-- Picture element -->
    <ScrollAnimation
        animationClass="opacity-100 translate-y-0"
        initialClass="-opacity-100 -translate-y-10">
        <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6 justify-items-center m-10">
          <div v-for="(item) in userPhoto" :key="item[0]" class=" w-54 h-70 flex justify-center items-center rounded-3xl overflow-hidden shadow-lg p-4 bg-[#575757]">
            <img :src="`./images/${item[2]}`" class="w-full h-full object-cover rounded-3xl">
          </div>
        </div>
    </ScrollAnimation>
  
    <!-- welcoming Element -->
    <ScrollAnimation 
        animationClass="opacity-100 translate-y-0"
        initialClass="opacity-0 translate-y-20">
      <div class="w-auto bg-[#D8C9AE] flex justify-center items-center h-auto p-8 mx-8 rounded-md shadow-xl">
          <h1 class="font-serif italic text-[#575757] text-3xl font-bold">Helloo!!! Welcome to my Site</h1>
      </div>
    </ScrollAnimation>
  
    <div class="space-y-10 p-10"> 
      <ScrollAnimation
        animationClass="opacity-100 scale-100"
        initialClass="opacity-0 scale-75"
      >
  
        <!-- Section Header -->
        <div class="relative mb-6">
            <div class="flex items-center">
                <div class="bg-[#575757] text-white px-4 py-2 rounded-l-lg font-semibold text-lg shadow-md">
                    Techincal Skill
                </div>
                <div class="flex-1 h-0.5 bg-[#575757] ml-2"></div>
            </div>
        </div>
        <div class="grid grid-cols-2 sm:grid-cols-3 md:grid-cols-4 lg:grid-cols-5 gap-4 justify-items-center m-8">
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/python.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/Drupal.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/SQL.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/Vue.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/Tailwind.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/AWS.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/HTML.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/CSS.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/Js.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
          <div class="w-25 h-25 flex items-center justify-center text-2xl rounded-full shadow border-[#575757] border-2">
            <img src="../../public/images/flasklogo.jpeg" alt="python" class="w-full h-full rounded-full object-cover">
          </div>
        </div>
      </ScrollAnimation>
  
      <div v-for="(section, index) in userISI" :key="index" class="mb-12">
              <!-- Section Header -->
          <ScrollAnimation
            animationClass="opacity-100 translate-x-0"
            initialClass="opacity-0 -translate-x-20"
          >
              <div class="relative mb-6">
                  <div class="flex items-center">
                      <div class="bg-[#575757] text-white px-4 py-2 rounded-l-lg font-semibold text-lg shadow-md">
                          {{ section[1] }}
                      </div>
                      <div class="flex-1 h-0.5 bg-[#575757] ml-2"></div>
                  </div>
              </div>
          </ScrollAnimation>
  
              <!-- Content Card -->
              <div class="bg-[#575757] rounded-2xl shadow-xl border-l-8 border-[#D8C9AE] overflow-hidden">
  
                <ScrollAnimation
                  animationClass="opacity-100 translate-x-0"
                  initialClass="opacity-0 -translate-x-20"
                >
                  <div class="p-8">
                      <div v-for="(isi, isiIndex) in section[2]" :key="isiIndex" class="mb-4 last:mb-0">
  
                        
                      <!-- Perkenalan Style -->
                                          <div v-if="section[1] === 'Perkenalan'" 
                          class="p-6 rounded-xl border-l-4"
                          style="background: linear-gradient(90deg, #D8C9AE, #B59F7B); border-color: #575757;">
                        <div class="text-lg leading-relaxed" style="color: #575757;">
                          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                            <div v-for="info in isi.split(', ')" :key="info" class="flex items-center">
                              <div class="w-2 h-2 rounded-full mr-3" style="background-color: #575757;"></div>
                              <span class="font-medium">{{ info }}</span>
                            </div>
                          </div>
                        </div>
                      </div>
  
                      <!-- KerjaOrganisasi Style -->
                      <div v-else-if="section[1] === 'KerjaOrganisasi'" 
                          class="pl-6 py-4 rounded-r-xl"
                          style="background-color: #D8C9AE; border-left: 4px solid #575757;">
                        <div class="text-base leading-relaxed" style="color: #575757;">
                          <div v-for="kerja in isi.split(', ')" :key="kerja" class="mb-3 flex items-start">
                            <div class="w-3 h-3 rounded-full mt-2 mr-4 flex-shrink-0" style="background-color: #575757;"></div>
                            <p class="font-semibold" style="color: #575757;">{{ kerja }}</p>
                          </div>
                        </div>
                      </div>
  
                      <!-- Proyek Style -->
                      <div v-else-if="section[1] === 'Proyek'" 
                          class="p-6 rounded-xl border"
                          style="background: linear-gradient(135deg, #D8C9AE, #B59F7B); border-color: #575757;">
                        <div class="text-base leading-relaxed" style="color: #575757;">
                          <div v-for="proyek in isi.split(', ')" :key="proyek" class="mb-3 flex items-start">
                            <div class="w-3 h-3 rounded-full mt-2 mr-4 flex-shrink-0" style="background-color: #575757;"></div>
                            <p class="font-semibold" style="color: #575757;">{{ proyek }}</p>
                          </div>
                        </div>
                      </div>
  
                      <div v-else-if="section[1] === 'Lainnya'" 
                          class="pl-6 py-4 rounded-r-xl"
                          style="background-color: #D8C9AE; border-left: 4px solid #575757;">
                        <div class="text-base leading-relaxed" style="color: #575757;">
                            <div v-for="lainnya in isi.split(', ')" :key="lainnya" class="mb-3 flex items-start">
                            <div class="w-3 h-3 rounded-full mt-2 mr-4 flex-shrink-0" style="background-color: #575757;"></div>
                            <p class="font-semibold" style="color: #575757;">{{ lainnya }}</p>
                          </div>
                        </div>
                      </div>
                    </div>
  
                      </div>
                  </ScrollAnimation>
              </div>
            </div>
  
        
    </div>
  <ScrollAnimation
    animationClass="opacity-100 scale-100"
    initialClass="opacity-0 scale-75"
  >
    <footer class="bg-[#6d6d6d] m-4 p-6 rounded-3xl shadow-xl">
      <div class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        
        <!-- Telegram -->
        <div class="flex flex-col items-center bg-[#D8C9AE] rounded-3xl p-6 text-center shadow-md">
          <div class="w-20 h-20 rounded-full shadow border-2 border-[#575757] overflow-hidden mb-3">
            <img src="../../public/images/Telegram.jpeg" alt="Telegram" class="w-full h-full object-cover" />
          </div>
          <p class="text-xl font-semibold">Telegram</p>
          <p class="text-base break-all">@Keanrich</p>
        </div>
  
        <!-- Email -->
        <div class="flex flex-col items-center bg-[#D8C9AE] rounded-3xl p-6 text-center shadow-md">
          <div class="w-20 h-20 rounded-full shadow border-2 border-[#575757] overflow-hidden mb-3">
            <img src="../../public/images/Email.jpeg" alt="Email" class="w-full h-full object-cover" />
          </div>
          <p class="text-xl font-semibold">Email</p>
          <p class="text-base break-all">kcordana26@students.calvin.ac.id</p>
        </div>
  
        <!-- Instagram -->
        <div class="flex flex-col items-center bg-[#D8C9AE] rounded-3xl p-6 text-center shadow-md">
          <div class="w-20 h-20 rounded-full shadow border-2 border-[#575757] overflow-hidden mb-3">
            <img src="../../public/images/Instagram.jpeg" alt="Instagram" class="w-full h-full object-cover" />
          </div>
          <p class="text-xl font-semibold">Instagram</p>
          <p class="text-base break-all">@keanrich_cr</p>
        </div>
  
      </div>
    </footer>
  </ScrollAnimation>
  </div>


</template>


<!-- <ScrollAnimation
animationClass="opacity-100 translate-x-0"
initialClass="opacity-0 translate-x-20"
>
<div class="bg-amber-50 h-128 flex items-center 
justify-center text-black text-2xl 
rounded-xl shadow-xl border-8 border-[]">
    Slide from Right
  </div>
</ScrollAnimation> -->
    
    <!-- Fade Up -->
    <!-- <ScrollAnimation
      animationClass="opacity-100 translate-y-0"
      initialClass="opacity-0 translate-y-20"
    >
      <div class="bg-blue-400 h-32 flex items-center justify-center text-white text-2xl rounded shadow">
        Fade Up
      </div>
    </ScrollAnimation> -->

    <!-- Slide from Left -->
    <!-- <ScrollAnimation
      animationClass="opacity-100 translate-x-0"
      initialClass="opacity-0 -translate-x-20"
    >
      <div class="bg-green-400 h-32 flex items-center justify-center text-white text-2xl rounded shadow">
        Slide from Left
      </div>
    </ScrollAnimation> -->

    <!-- Slide from Right -->
    <!-- <ScrollAnimation
      animationClass="opacity-100 translate-x-0"
      initialClass="opacity-0 translate-x-20"
    >
      <div class="bg-purple-400 h-32 flex items-center justify-center text-white text-2xl rounded shadow">
        Slide from Right
      </div>
    </ScrollAnimation> -->
    
    <!-- Zoom In -->
    <!-- <ScrollAnimation
    animationClass="opacity-100 scale-200"
    initialClass="opacity-0 scale-75"
    >
    <div class="bg-red-400 h-32 flex items-center justify-center text-white text-2xl rounded shadow">
      Zoom In
    </div>
  </ScrollAnimation> -->
  
  <!-- <ScrollAnimation
    animationClass="opacity-100 rotate-0"
    initialClass="opacity-0 -rotate-90"
  >
    <div class="bg-red-400 h-32 flex items-center justify-center text-white text-2xl rounded shadow">
      Rotate
    </div>
  </ScrollAnimation> -->

