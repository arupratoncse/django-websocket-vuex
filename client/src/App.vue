<template>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList" v-bind:key="index"></pipe-line>
        <button class="add-button" @click="addPipeLine">ADD</button>
    </div>
</template>

<script>
    import PipeLine from './components/PipeLine.vue';
    export default {
        name: 'App',
        components: {
            PipeLine,
        },
        data() {
            return {
            }
        },
        computed: {
            pipeLineList(){
                console.log(this.$store.state.pipeLineList);
                return this.$store.state.pipeLineList;
            },
            kanbanId(){
                return this.$store.state.kanbanId;
            }
        },
        methods: {
            addPipeLine(){
                let title = window.prompt('title');
                if(title === undefined || title === null){
                    return;
                }
                this.$store.dispatch('add_pipeline', {
                    'kanbanId': this.kanbanId,
                    'title': title,
                    'order': this.pipeLineList.length,
                });
            }
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }
    .add-button {
        font-size: 1.2em;
        height: 40px;
        border: solid;
        padding: 5px;
        margin: 5px;
        width: 100px;
        cursor: pointer;
    }
    .add-button:hover {
        background-color: #333333;
        color: #fffccf;
    }


</style>
