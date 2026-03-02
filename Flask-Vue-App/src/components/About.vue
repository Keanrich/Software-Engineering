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
      userISI:'',
      id_item:'', 
      show_form_add:false,
      activeFormSection: null,
      activeFormSection_delete: null,
      form_add: {
        kategori:'',
        isi:'',
      },
      form_update: {
        kategori_lama:'',
        isi_lama:'',
        kategori:'',
        isi:'',
      },
      form_delete: {
        kategori:'',
        isi:''
      }
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
      } catch (error) {
        console.error('Gagal mengambil data:', error);
      }
    },
    async submitform_add() {
      const user_id = localStorage.getItem('user_id');
      try {
        const res = await axios.post(`http://localhost:5000/add-item/${user_id}`, this.form_add)
        console.log('Berhasil Membuat Item Baru', res.data)
      } catch (error) {
        console.error('Gagal Membuat Item Baru', error)
      }

      this.form_add = {
        kategori:'',
        isi:'',
      }

      this.show_form_add = false
      this.FetchSite()
    }, 

    async submitform_update() {
      const user_id = localStorage.getItem('user_id');   
      try {
        const res = await axios.put(`http://localhost:5000/update-item/${user_id}`, this.form_update)
        console.log(`Berhasil mengubah section index`, res.data)
      } catch (error) {
        console.error(error)
      }

      this.form_update = {
        kategori:'',
        isi:'',
      }

      this.activeFormSection = null
      this.FetchSite()
    },

    async submitform_delete() {
      const user_id = localStorage.getItem('user_id');   
      try {
        const res = await axios.delete(`http://localhost:5000/delete-item/${user_id}`, {
        data: this.form_delete
        })
        console.log(`Berhasil menghapus section ${this.form_delete.kategori} dengan isi ${this.form_delete.isi}`, res.data)
        } catch (error) {
          console.error(error)
        }

      this.form_delete = {
        kategori:'',
        isi:'',
      }

      this.activeFormSection_delete = null
      this.FetchSite()
      },

    cancel_form_delete() {
      this.form_delete = {
        kategori:'',
        isi:'',
      }
      this.activeFormSection_delete = null
      this.FetchSite()
    },

    toggleForm(sectionIndex, kategori_lama, isi_lama) {
      this.activeFormSection = this.activeFormSection === sectionIndex ? null : sectionIndex;
      this.form_update = {    
        kategori:'',
        isi:'',      
        kategori_lama: kategori_lama,      // default sama dengan lama
        isi_lama: isi_lama                  // default sama dengan lama
        }
        console.log(this.form_update)
    },
    toggleForm_delete(sectionIndex, kategori_lama, isi_lama) {
      this.activeFormSection_delete = this.activeFormSection_delete === sectionIndex ? null : sectionIndex;
      this.form_delete = {      
        kategori: kategori_lama,      // default sama dengan lama
        isi: isi_lama                  // default sama dengan lama
        }
        console.log(this.form_delete)
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
  
                      <div class="flex justify-end">
                        <button @click="toggleForm(index,section[1], section[2])" 
                                class="bg-[#e0d9cb] text-[#575757] m-4 px-4 py-2 rounded-lg 
                                font-semibold text-l shadow-md w-20 h-10 transition delay-150 duration-300 
                                ease-in-out hover:-translate-y-1 hover:scale-105 hover:bg-[#575757] hover:text-[#D8C9AE]">
                          {{ activeFormSection === index ? 'Tutup' : 'Update' }}
                        </button>
                        <button @click="toggleForm_delete(index, section[1], section[2])" 
                                class="bg-[#da1327] text-[#D8C9AE] my-4 px-4 py-2 rounded-lg 
                                font-semibold text-l shadow-md w-20 h-10 transition delay-150 duration-300 
                                ease-in-out hover:-translate-y-1 hover:scale-105 hover:bg-[#9c0b23] hover:text-[#D8C9AE]">
                          {{ activeFormSection_delete === index ? 'Tutup' : 'Delete' }}
                        </button>
                      </div>
  
                      <div v-if="activeFormSection_delete === index">
                        <div class="flex justify-center items-center h-auto p-4">
                              <div class="w-160 p-8 rounded-xl shadow-lg bg-[#f6eee0]">
                              <h2 class="text-center text-lg font-semibold text-[#36454F] mb-8">Are You Sure Want to Delete this Item</h2>
                              <div class="text-center">
                                  <button
                                      type="submit"
                                      @click="submitform_delete"
                                      class="bg-[#da2424] text-white px-6 py-2 rounded hover:bg-[#2a363e] transition m-2"
                                  >
                                      Delete
                                  </button>
                                  <button
                                      type="submit"
                                      @click="cancel_form_delete"
                                      class="bg-[#36454F] text-white px-6 py-2 rounded hover:bg-[#2a363e] transition m-2"
                                  >
                                      Cancel
                                  </button>
                              </div>
                            </div>
                          </div>
                      </div>
  
                        <div  v-if="activeFormSection === index">
                          <div class="flex justify-center items-center h-auto p-4">
                              <div class="w-160 p-8 rounded-xl shadow-lg bg-[#f6eee0]">
                              <h2 class="text-center text-lg font-semibold text-[#36454F] mb-8">Update Item</h2>
                              
                              <form @submit.prevent="submitform_update()">
                                <div class="mb-6">
                                  <label class="block text-[#36454F] font-semibold mb-2">Kategori</label>
                                  <select
                                      v-model="form_update.kategori"
                                      required
                                      class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F]"
                                  >
                                      <option value="" disabled>Pilih kategori...</option>
                                      <option value="Proyek">Proyek</option>
                                      <option value="KerjaOrganisasi">Kerja Organisasi</option>
                                      <option value="Perkenalan">Perkenalan</option>
                                      <option value="Lainnya">Lainnya</option>
                                  </select>
                                </div>
  
                                <div class="mb-6">
                                  <label class="block text-[#36454F] font-semibold mb-2">Isi Block</label>
                                  <textarea
                                      v-model="form_update.isi"
                                      rows="6"
                                      required
                                      class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F] resize-y"
                                      placeholder="Masukkan deskripsi lengkap di sini..."
                                  ></textarea>
                                </div>
  <!-- 
                                <div class="mb-6">
                                  <label class="block text-[#36454F] font-semibold mb-2">Kategori lama</label>
                                    <select
                                      v-model="form_update.kategori_lama"
                                      disabled
                                      class="w-full px-4 py-2 border border-[#ccc] rounded bg-gray-200 cursor-not-allowed"
                                    >
                                      <option value="Proyek">Proyek</option>
                                      <option value="KerjaOrganisasi">Kerja Organisasi</option>
                                      <option value="Perkenalan">Perkenalan</option>
                                      <option value="Lainnya">Lainnya</option>
                                    </select>
                                </div>
  
                                <div class="mb-6">
                                  <label class="block text-[#36454F] font-semibold mb-2">Isi Block yang lama</label>
                                    <textarea
                                      v-model="form_update.isi_lama"
                                      rows="6"
                                      readonly
                                      class="w-full px-4 py-2 border border-[#ccc] rounded bg-gray-200 resize-y cursor-not-allowed"
                                    ></textarea>
                                </div> -->
  
                                <div class="text-center">
                                  <button
                                      type="submit"
                                      class="bg-[#36454F] text-white px-6 py-2 rounded hover:bg-[#2a363e] transition m-2"
                                  >
                                      Update
                                  </button>
                                </div>
                              </form>
                              </div>
                          </div>
                        </div>
                  </div>
              </ScrollAnimation>
              </div>
            </div>
  
  
      <div class="flex justify-center items-center">
        <button @click="show_form_add = !show_form_add" class="bg-[#575757] text-[#D8C9AE] px-4 py-2 rounded-lg font-semibold text-xl shadow-md w-40 h-20
        transition delay-150 duration-300 ease-in-out hover:-translate-y-1 hover:scale-105 hover:bg-[#D8C9AE] hover:text-[#575757]"> + Add Block</button>
      </div>
  
      <div v-if="show_form_add == true">
        <div class="flex justify-center items-center h-auto p-4">
            <div class="w-160 p-8 rounded-xl shadow-lg bg-[#f6eee0]">
            <h2 class="text-center text-lg font-semibold text-[#36454F] mb-8">Add Item</h2>
            
            <form @submit.prevent="submitform_add">
              <div class="mb-6">
                <label class="block text-[#36454F] font-semibold mb-2">Kategori</label>
                <select
                    v-model="form_add.kategori"
                    required
                    class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F]"
                >
                    <option value="" disabled>Pilih kategori...</option>
                    <option value="Proyek">Proyek</option>
                    <option value="KerjaOrganisasi">Kerja Organisasi</option>
                    <option value="Perkenalan">Perkenalan</option>
                    <option value="Lainnya">Lainnya</option>
                </select>
              </div>
  
              <div class="mb-6">
                <label class="block text-[#36454F] font-semibold mb-2">Isi Block</label>
                <textarea
                    v-model="form_add.isi"
                    rows="6"
                    required
                    class="w-full px-4 py-2 border border-[#ccc] rounded focus:outline-none focus:ring-2 focus:ring-[#36454F] resize-y"
                    placeholder="Masukkan deskripsi lengkap di sini..."
                ></textarea>
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

<!-- buat tampilan yang sama tapi bisa edit pagenya, jadi ada tombol tambah, delete, update -->