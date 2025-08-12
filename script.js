function sendMessage() {
    const input = document.getElementById('userInput');
    const message = input.value.trim();
    if (!message) return;

    const chatArea = document.getElementById('chatArea');
    chatArea.innerHTML += `<p><b>You:</b> ${message}</p>`;
    input.value = '';
    input.disabled = true;

    fetch('/chat', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({message: message})
    })
    .then(response => response.json())
    .then(data => {
        chatArea.innerHTML += `<p><b>Bot:</b> ${data.response}</p>`;
        chatArea.scrollTop = chatArea.scrollHeight;
        input.disabled = false;
        input.focus();
    })
    .catch(err => {
        chatArea.innerHTML += `<p><b>Bot:</b> Error: ${err.message}</p>`;
        input.disabled = false;
    });
}

// Optional: send message on Enter key
document.getElementById('userInput').addEventListener('keypress', function (e) {
    if (e.key === 'Enter') {
        sendMessage();
    }
    });