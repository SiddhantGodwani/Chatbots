const chatlog = document.getElementById("chatlog");
const userInput = document.getElementById("userInput");
const sendButton = document.getElementById("sendButton");

function appendMessage(sender, message) {
    const messageDiv = document.createElement("div");
    messageDiv.className = sender;
    messageDiv.innerText = message;
    chatlog.appendChild(messageDiv);
    chatlog.scrollTop = chatlog.scrollHeight;
}

function sendUserMessage() {
    const message = userInput.value;
    if (message.trim() === "") return;

    appendMessage("user", message);
    userInput.value = "";

    fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message }),
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("bot", data.message);
    });
}

userInput.addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        sendUserMessage();
    }
});

sendButton.addEventListener("click", sendUserMessage);

appendMessage("bot", "Hello! I'm your Chatbot LOKI. How can I assist you today?");
