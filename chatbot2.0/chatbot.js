const responses = {
    "what is e-waste": "E-waste, or electronic waste, refers to discarded electronic devices, such as old computers, smartphones, and TVs.",
    "why is e-waste harmful": "E-waste contains toxic materials that can harm the environment and human health when not properly disposed of.",
    // Add more responses as needed
};

function userMessage() {
    const input = document.getElementById("userInput");
    const message = input.value.trim();
    if (message === "") return;
    const chatlog = document.getElementById("chatlog");
    chatlog.innerHTML += `<div class="user">${message}</div>`;
    input.value = "";

    if (responses[message.toLowerCase()]) {
        botMessage(responses[message.toLowerCase()]);
    } else {
        botMessage("I'm sorry, I don't know the answer to that question. Please ask something else.");
    }
}

function botMessage(message) {
    const chatlog = document.getElementById("chatlog");
    chatlog.innerHTML += `<div class="bot">${message}</div>`;
}

document.getElementById("userInput").addEventListener("keydown", function (e) {
    if (e.key === "Enter") {
        userMessage();
    }
});

botMessage("Hello! I'm your E-Waste chatbot. How can I help you today?");
