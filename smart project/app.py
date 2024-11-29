from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Chatbot responses
def get_response(user_input):
    """
    Generate a response based on predefined keywords.
    """
    # Normalize input
    user_input = user_input.lower().strip()

    # Predefined keywords and responses
    keywords = {
        "hello": "hello I am amrit Assistant. How can i'm help you.",
        "symptom": "Please describe your symptoms so I can assist you better.",
        "doctor": "I can help you find a doctor. Please tell me your specialty or location.",
        "appointment": "You can schedule an appointment by specifying the doctor and time slot.",
        "medication": "For medication, could you tell me the medicine you are looking for?",
        "emergency": "In case of an emergency, I recommend calling your local emergency services immediately.",
        "hospital": "I can help you find nearby hospitals. Could you share your location?",
        "advice": "It's always a good idea to consult with a healthcare professional for personalized advice.",
        "health tips": "Stay hydrated, eat a balanced diet, and exercise regularly to maintain good health.",
        "covid": "For COVID-19 updates, I recommend checking with the official health authorities in your region.",
        "fever": "If you have a fever, I recommend checking your temperature regularly and consulting a healthcare provider.",
        "headache": "A headache can have many causes. It's best to take a rest, stay hydrated, and consult a doctor if the symptoms persist."
    }

    # Check if the user input matches any predefined keyword
    for keyword, response in keywords.items():
        if keyword in user_input:
            return response

    # Default response if no keyword matches
    return "I'm sorry, I didn't quite understand that. Can you please provide more details?"

# Route to render the chatbot page
@app.route('/')
def home():
    """
    Render the chatbot interface.
    """
    return render_template('index.html')  # Ensure 'index.html' is in the 'templates' folder

# Route to handle user input and generate chatbot response
@app.route('/get_response', methods=['POST'])
def get_chat_response():
    """
    Handle user input and return chatbot response.
    """
    try:
        # Get user input from the request
        user_input = request.form.get('user_input')
        if not user_input:
            return jsonify({'response': "Invalid input. Please type a message."}), 400

        # Generate response
        bot_response = get_response(user_input)
        return jsonify({'response': bot_response})
    except Exception as e:
        # Handle unexpected errors
        return jsonify({'response': f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
