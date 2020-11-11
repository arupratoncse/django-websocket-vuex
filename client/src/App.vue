<template>
  <div class="kanban mt-1">
    <button class="btn btn-primary" @click="showPipelineModal">Add new PipeLine</button>
    <div class="kanban-base">
        <pipe-line :pipeLine="pipeLine" v-for="(pipeLine, index) in pipeLineList"
           v-bind:key="index"
           @update-pipeline="showUpdatePipeline"
        >
        </pipe-line>
    </div>
    <!--Add new pipeline modal-->
    <b-modal
      :title="pipeline_head"
      ref="pipelineModal"
      header-class="bg-info text-light"
      body-class="text-info"
      no-close-on-esc
      no-close-on-backdrop
      @ok="addOrUpdatePipeLine">
      <div>
        <div>
          PipeLine Name:
        </div>
        <form @submit.prevent="addOrUpdatePipeLine">
          <b-form-input
            name="pipeline-name"
            type="text"
            ref="focusInput"
            v-model="pipeline.title"
            :state="pipeline.title.length > 0"
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
              pipeline: {
                title: '',
                id: null
              },
              pipeline_head: ''
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
            this.pipeline_head = 'Add new pipeline'
            this.pipeline = {
              title: '',
              id: null
            }
            this.$refs.pipelineModal.show()
          },
          addOrUpdatePipeLine(){
            if(!this.pipeline.title){
                return;
            }
            if(!this.pipeline.id) {
              this.$store.dispatch('add_pipeline', {
                'kanbanId': this.kanbanId,
                'title': this.pipeline.title,
                'order': this.pipeLineList.length
              })
            }
            else {
              this.$store.dispatch('update_pipeline', {
                'title': this.pipeline.title,
                'pipeline_id': this.pipeline.id
              })
            }
          },
          showUpdatePipeline(item){
            this.pipeline_head = 'Update pipeline'
            this.pipeline = item
            this.$refs.pipelineModal.show()
          }
        }
    }
</script>
<style scoped>
    .kanban-base {
        display: flex;
    }

</style>
