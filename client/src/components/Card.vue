<template>
    <div class="card">
        <div class="card-title">
          {{card.title}}
          <span @click="deleteCard(card)" class="pointer-cursor h4 text-white float-right"
          v-b-tooltip.hover.top title="Delete Card">
          <b-icon icon="trash"></b-icon>
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
          deleteCard(item){
            const confirm = window.confirm("Are you sure to delete card: "+ item.title);
            if(confirm){
              console.log(item)
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
