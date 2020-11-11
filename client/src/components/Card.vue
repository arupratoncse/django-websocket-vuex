<template>
    <div class="card">
        <div class="card-title">
          {{card.title}}
          <span @click="updateCard(card)" class="pointer-cursor text-white"
            v-b-tooltip.hover.top title="Update Card">
            <b-icon icon="pencil-fill"></b-icon>
          </span>
          <span @click="deleteCard(card)" class="pointer-cursor text-danger float-right"
          v-b-tooltip.hover.top title="Delete Card">
          <b-icon icon="trash-fill"></b-icon>
        </span>
        </div>
        <div>
            {{card.content}}
        </div>
    </div>
</template>
<script>
    export default {
        name: 'Card',
        props: [
            'card',
        ],
      methods: {
          updateCard(item){
            this.$emit('update-card', {'card_id': item.id, 'title': item.title, 'content': item.content})
          },
          deleteCard(item){
            const confirm = window.confirm("Are you sure to delete card: "+ item.title);
            if(confirm){
              this.$store.dispatch('delete_card', {
                'card_id': item.id
              })
            }
          }
      }
    }
</script>
<style scoped>
    .card {
        margin: 5px;
        border: solid;
        cursor: move;
    }
    .card-title {
        background-color: #333333;
        color: #fffccf;
    }
    .pointer-cursor{
      cursor: pointer;
    }
</style>
