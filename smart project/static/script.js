// This script connects the frontend with the Flask backend for chat interaction

document.getElementById('chat-form').addEventListener('submit', function(event) {
    event.preventDefault();  // Prevent form from submitting

    const userInput = document.getElementById('user-input').value.trim();
    if (userInput) {
        // Display user's message
        displayMessage(userInput, 'user');
        document.getElementById('user-input').value = ''; // Clear input field

        // Send the message to the server
        fetch('/get_response', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            },
            body: new URLSearchParams({
                'user_input': userInput
            })
        })
        .then(response => response.json())
        .then(data => {
            // Display bot's response
            displayMessage(data.response, 'bot');
        })
        .catch(error => {
            // In case of error, show an error message
            displayMessage("Sorry, I couldn't reach the server.", 'bot');
        });
    }
});

// Function to display messages
function displayMessage(message, sender) {
    const messageContainer = document.createElement('div');
    messageContainer.classList.add('message', `${sender}-message`);
    messageContainer.textContent = message;
    document.getElementById('chat-output').appendChild(messageContainer);

    // Auto scroll to the bottom of the chat box
    document.getElementById('chatbox').scrollTop = document.getElementById('chatbox').scrollHeight;
}
