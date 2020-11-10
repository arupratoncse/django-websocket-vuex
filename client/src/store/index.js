import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)
import createWebSocketPlugin from './WebSocketPlugin';

const socket = new WebSocket('ws://' + window.location.host + '/ws' + window.location.pathname);
const plugin = createWebSocketPlugin(socket);


export default new Vuex.Store({
  state: {
    pipeLineList: [],
    kanbanId: parseInt(window.location.pathname.split('kanban/')[1])
  },
  mutations: {
    set_data(state, payload){
        console.log('set_data', state, payload);
        this.state.pipeLineList = payload.kanban;
    },
  },
  actions: {
    add_pipeline(context, payload){
        console.log('action add_pipeline called', payload);
    },
    add_card(context, payload){
        console.log('action add_card called', payload);
    },
    update(context, payload){
        // The actual commit is on the plugin side
        // If you don't define it, you can't dispatch it ...
        console.log('action update called', payload);
        //context.commit('update', payload)
    }
  },
  plugins: [plugin],
  modules: {
  }
})
