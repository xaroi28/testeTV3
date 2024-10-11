const socket = io();

document.getElementById('textInput').addEventListener('input', function() {
    const text = this.value;
    socket.emit('send_text', { text: text });
});

socket.on('receive_text', function(data) {
    document.getElementById('textOutput').innerText = data.text;
});
