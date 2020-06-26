document.addEventListener('DOMContentLoaded', () => {

      // Connect to websocket
      var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

      // When connected, configure buttons
      socket.on('connect', () => {
        button = document.getElementById('messagebutton');
        button.onclick = () => {
                  const selection = document.getElementById('message').value;
                  socket.emit('submit message', {'selection': selection});
              };
          });

      socket.on('announce message', data => {
          const li = document.createElement('li');
          li.innerHTML = `${data.selection}`;
          document.querySelector('#allmessages').append(li);
      });
  });
