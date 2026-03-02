<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'

const props = defineProps({
    animationClass: {
        type: String,
        default: 'opacity-100 translate-y-0'
    },
    initialClass: {
        type: String,
        default: 'opacity-0 translate-y-10'
    },
    threshold: {
        type: Number,
        default: 0.1
    },
    repeat: {
        type: Boolean,
        default: true
    },
    exitDelay: {
        type: Number,
        default: 200 // ms sebelum apply exit (untuk animasi keluar)
    }
})

const element = ref(null)
const isVisible = ref(false)
const currentClass = ref(props.initialClass)
let timeoutId = null

onMounted(() => {
    const observer = new IntersectionObserver(
        ([entry]) => {
        if (entry.isIntersecting) {
            // Masuk layar: langsung apply animasi masuk
            clearTimeout(timeoutId)
            isVisible.value = true
            currentClass.value = props.animationClass
        } else if (props.repeat) {
            // Keluar layar: delay sebelum keluar
            timeoutId = setTimeout(() => {
            isVisible.value = false
            currentClass.value = props.initialClass
            }, props.exitDelay)
        }
        },
        { threshold: props.threshold }
    )

    if (element.value) {
        observer.observe(element.value)
    }

    // Clean up observer
    onBeforeUnmount(() => {
        if (element.value) {
        observer.unobserve(element.value)
        }
    })
    })
</script>

<template>
    <div
        ref="element"
        :class="[
        'transition-all duration-700 ease-out',
        currentClass
        ]"
    >
        <slot />
    </div>
</template>



