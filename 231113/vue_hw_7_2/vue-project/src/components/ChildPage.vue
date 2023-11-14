<template>
    <div>
        <div v-bind:style = "{border : '0.3px solid lightgray', margin : '10px', padding : '10px', backgroundColor : 'white',textAlign : 'center'}">
        <h3>자식 페이지</h3>
        {{ child.name }}
        </div>
    </div>
</template>

<script setup>

const props = defineProps({
    child : Object
})

</script>

<style scoped>

</style>