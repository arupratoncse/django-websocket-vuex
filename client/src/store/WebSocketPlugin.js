export default function createWebSocketPlugin (socket) {
  return store => {
    console.log(store, socket);
    // Mutate with the response from the server
    socket.onmessage = e => {
      const data = JSON.parse(e.data);
      store.commit(data.type, data)

    };
    // Hook Action on the Plugin side and throw it to websocket
    store.subscribeAction((action) => {
      console.log(action);
      switch(action.type){
        case 'update':
          socket.send(JSON.stringify({
              type: 'update',
              payload: action.payload
          }));
          break;

        case 'add_card':
          socket.send(JSON.stringify({
              type: 'add_card',
              payload: action.payload
          }));
          break;

        case 'update_card':
          socket.send(JSON.stringify({
              type: 'update_card',
              payload: action.payload
          }));
          break;

        case 'delete_card':
          socket.send(JSON.stringify({
              type: 'delete_card',
              payload: action.payload
          }));
          break;

        case 'add_pipeline':
          socket.send(JSON.stringify({
              type: 'add_pipeline',
              payload: action.payload
          }));
          break;

        case 'update_pipeline':
          socket.send(JSON.stringify({
              type: 'update_pipeline',
              payload: action.payload
          }));
          break;

        case 'delete_pipeline':
          socket.send(JSON.stringify({
              type: 'delete_pipeline',
              payload: action.payload
          }));
          break;
      }
    })
  }
}
