<template>
    <div class="pipeline">
      <div class="pipeline-title">
        {{pipeLine.title}} count: {{pipeLine.cards.length}}
        <span @click="showCardModal" class="close-button h4 text-success"
          v-b-tooltip.hover.top title="Add new card item">
          <b-icon icon="plus-square"></b-icon>
        </span>
        <span @click="deletePipeLine(pipeLine)" class="close-button h4 text-danger"
          v-b-tooltip.hover.top title="Delete PipeLine">
          <b-icon icon="trash"></b-icon>
        </span>
      </div>
      <div class="card-list">
          <draggable :options="options" v-model="cards" class="card-draggable-base">
              <card :card="card" v-for="(card, i) in cards" v-bind:key="i"></card>
          </draggable>
      </div>
      <b-modal
        title="Add new Card"
        ref="cardModal"
        header-class="bg-info text-light"
        body-class="text-info"
        no-close-on-esc
        no-close-on-backdrop
        @ok="addCard">
        <div>
          <form @submit.prevent="addCard">
            <div>
              Card Title:
            </div>
            <b-form-input
              name="card-title"
              type="text"
              v-model="card_title"
              :state="card_title.length > 0"
              maxlength="100">
            </b-form-input>
            <div>
              Card Content:
            </div>
            <b-form-textarea
              name="card-content"
              type="text"
              v-model="card_content"
              :state="card_content.length > 0"
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
            this.card_title = ''
            this.card_content = ''
            this.$refs.cardModal.show()
          },
          addCard(){
            if(! this.card_content || !this.card_title){
                return;
            }
            this.$store.dispatch('add_card', {
                'pipeLineId': this.pipeLine.id,
                'title': this.card_title,
                'content': this.card_content,
                'order': this.pipeLine.cards.length,
            });
          },
          deletePipeLine(item){
            const confirm = window.confirm("Are you sure to delete PipeLine: "+ item.title);
            if(confirm){
              console.log(item)
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
            card_title: '',
            card_content: ''
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
