<template>
    <div class="pipeline">
      <div class="pipeline-title">
        {{pipeLine.title}}<b-badge>{{pipeLine.cards.length}}</b-badge>&nbsp;
        <span @click="showCardModal" class="close-button h4 text-success"
          v-b-tooltip.hover.top title="Add new card item">
          <b-icon icon="plus-square"></b-icon>
        </span>&nbsp;
        <span @click="updatePipeline(pipeLine)" class="close-button h4 text-info"
          v-b-tooltip.hover.top title="Update PipeLine">
          <b-icon icon="pencil-fill"></b-icon>
        </span>&nbsp;
        <span @click="deletePipeLine(pipeLine)" class="close-button h4 text-danger"
          v-b-tooltip.hover.top title="Delete PipeLine">
          <b-icon icon="trash"></b-icon>
        </span>
      </div>
      <div class="card-list">
          <draggable :options="options" v-model="cards" class="card-draggable-base">
              <card :card="card" v-for="(card, i) in cards" v-bind:key="i" @update-card="showUpdateCard"></card>
          </draggable>
      </div>
      <b-modal
        :title="card_head"
        ref="cardModal"
        header-class="bg-info text-light"
        body-class="text-info"
        no-close-on-esc
        no-close-on-backdrop
        @ok="addOrUpdateCard">
        <div>
          <form @submit.prevent="addOrUpdateCard">
            <div>
              Card Title:
            </div>
            <b-form-input
              name="card-title"
              type="text"
              v-model="item_card.title"
              :state="item_card.title.length > 0"
              maxlength="100">
            </b-form-input>
            <div>
              Card Content:
            </div>
            <b-form-textarea
              name="card-content"
              type="text"
              v-model="item_card.content"
              :state="item_card.content.length > 0"
              rows="3"
              max-rows="6">
            </b-form-textarea>
          </form>
        </div>
      </b-modal>
    </div>
</template>
<script>
    import Card from './Card.vue';
    import draggable from 'vuedraggable';
    export default {
        name: 'PipeLine',
        props: [
            'pipeLine'
        ],
        components: {
            Card,
            draggable,
        },
        methods: {
          showCardModal(){
            this.card_head = "Add New Card"
            this.item_card = {
              card_id: null,
              title: '',
              content: ''
            }
            this.$refs.cardModal.show()
          },
          addOrUpdateCard(){
            if(!this.item_card.title || !this.item_card.content){
                return;
            }
            if(!this.item_card.card_id){
              this.$store.dispatch('add_card', {
                  'pipeLineId': this.pipeLine.id,
                  'title': this.item_card.title,
                  'content': this.item_card.content,
                  'order': this.pipeLine.cards.length,
              })
            }
            else{
              this.$store.dispatch('update_card', this.item_card)
            }
          },
          showUpdateCard(item){
            this.card_head = "Update Card"
            this.item_card = item
            this.$refs.cardModal.show()
          },
          updatePipeline(item){
            this.$emit('update-pipeline', {'title': item.title, 'id': item.id})
          },
          deletePipeLine(item){
            const confirm = window.confirm("Are you sure to delete PipeLine: "+ item.title);
            if(confirm){
              this.$store.dispatch('delete_pipeline', {
                'pipeline_id': item.id
              })
            }
          }
        },
        computed: {
            cards: {
                get(){
                    return this.pipeLine.cards;
                },
                set(value){
                    console.log('cards', value);
                    this.$store.dispatch('update', {
                        'pipeLineId': this.pipeLine.id,
                        'newCardList': value
                    });
                }
            }
        },
        data() {
          return {
            options: {
                group: "kanban",
                animation: 300,
            },
            item_card:{
              card_id: null,
              title: '',
              content: ''
            },
            card_head: ''
          };
        }
    }
</script>
<style scoped>
    .card-draggable-base {
        min-height: 100px;
    }
    .pipeline {
        margin: 5px;
        padding: 5px;
        width: 250px;
        border: solid;
    }
    .pipeline-title {
        text-align: center;
        padding: 5px;
        border: solid;
    }
    .close-button {
        cursor: pointer;
    }
</style>
