// Get chatbot elements
const chatbot = document.getElementById('chatbot');
const conversation = document.getElementById('conversation');
const inputForm = document.getElementById('input-form');
const inputField = document.getElementById('input-field');

// Add event listener to input form
inputForm.addEventListener('submit', function(event) {
  // Prevent form submission
    event.preventDefault();

  // Get user input
        const input = inputField.value;

  // Clear input field
        inputField.value = '';
        const currentTime = new Date().toLocaleTimeString([], { hour: '2-digit', minute: '2-digit' });

  // Add user input to conversation
    let message = document.createElement('div');
    message.classList.add('chatbot-message', 'user-message');
    message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${input}</p>`;
    conversation.appendChild(message);

    // Generate chatbot response
    const response = generateResponse(input);

    // Add chatbot response to conversation
    message = document.createElement('div');
    message.classList.add('chatbot-message', 'chatbot');
    message.innerHTML = `<p class="chatbot-text" sentTime="${currentTime}">${response}</p>`;
    conversation.appendChild(message);
    message.scrollIntoView({ behavior: 'smooth' });
});

// Generate chatbot response function
function generateResponse(input) {
  // Define options and responses
    const options = [
    {
        option: '1. Tell me a joke',
        response: 'Why did the chicken cross the road? To get to the other side!'
    },
    {
        option: '2. Whats the weather like today?',
        response: 'I am sorry, I dont have access to real-time weather information.'
    },
    {
        option: '3. Who won the World Series in 2021?',
        response: 'The Atlanta Braves won the World Series in 2021.'
    },
    {
        option: '4. Help me with C++ programming',
        response: 'Sure, I can help you with C++ programming. What do you need assistance with?'
    },
    ];

    // Check if user input matches an option
    for (const item of options) {
        if (input.toLowerCase().includes(item.option.toLowerCase())) {
        return item.response;
    }
    }

    // If no option matches, provide a generic response
    const genericResponse = 'I'm here to assist you with any questions or concerns you may have.';
    return genericResponse;
}
