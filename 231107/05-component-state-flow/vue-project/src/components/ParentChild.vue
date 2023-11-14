<template>
    <div>
        <p>{{ myMsg }}</p>
        <p>{{ dynamicProps }}</p>
        <ParentGrandChild 
        my-msg = '1'
        @update-name = 'updateName'
         />
        <button @click="buttonClick">클릭</button>
        <button @click="emitArgs">추가 인자 전달</button>
    </div>
</template>

<script setup>

    import ParentGrandChild from '@/components/ParentGrandChild.vue'

    // defineProps(['myMsg'])

    // defineProps({
    //     myMsg : String,
    // })

    // const props = defineProps ({
    //     myMsg : String,
    //     dynamicProps : String,
    // })

    // console.log(props)

    defineProps({
        myMsg:{
            type:String,
            required:true,
        }
    })

    const emit = defineEmits(['someEvent','emitArgs','updateName'])

    const buttonClick = function () {
        emit('someEvent')
    }

    const emitArgs = function(){
        emit('emitArgs',1,2,3)
    }

    const updateName = function() {
        emit('updateName')
    }

</script>

<style scoped>

</style>