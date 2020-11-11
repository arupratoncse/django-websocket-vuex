<template>
  <div class="kanban mt-1">
    <button class="btn btn-primary" @click="showPipelineModal">Add new PipeLine</button>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList" v-bind:key="index"></pipe-line>
    </div>
    <!--Add new pipeline modal-->
    <b-modal
      title="Add new PipeLine"
      ref="pipelineModal"
      header-class="bg-info text-light"
      body-class="text-info"
      no-close-on-esc
      no-close-on-backdrop
      @ok="addPipeLine">
      <div>
        <div>
          PipeLine Name:
        </div>
        <form @submit.prevent="addPipeLine">
          <b-form-input
            name="pipeline-name"
            type="text"
            ref="focusInput"
            v-model="pipeline_title"
            :state="pipeline_title.length > 0"
            maxlength="100">
          </b-form-input>
        </form>
      </div>
    </b-modal>
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
              pipeline_title: ''
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
          showPipelineModal(){
            this.pipeline_title = ''
            this.$refs.pipelineModal.show()
          },
          addPipeLine(){
            this.pipeline_title=this.pipeline_title.trim()
            if(!this.pipeline_title){
                return;
            }
            this.$store.dispatch('add_pipeline', {
                'kanbanId': this.kanbanId,
                'title': this.pipeline_title,
                'order': this.pipeLineList.length
            })
          }
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }

</style>
