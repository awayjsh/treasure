<template>
    <div>
        <div v-bind:style = "{border : '0.3px solid lightgray', margin : '3px', padding : '10px', backgroundColor : 'whitesmoke',textAlign : 'center'}">
        <h2>부모 컴포넌트</h2>
        <p>{{ family.father }}</p>
        <p>{{ family.mother }}</p>
        <ChildPage v-for="(child,index) in family.children" :key = 'index' :child = 'child' />
        </div>
    </div>
</template>

<script setup>

import ChildPage from './ChildPage.vue'
import { useFamilyStore } from '../stores/family'

const store = useFamilyStore()

const props = defineProps({
    family : Object
})

</script>

<style scoped>

</style>