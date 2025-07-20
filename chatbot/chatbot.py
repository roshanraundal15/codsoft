from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

# Ensure the templates folder is correctly referenced
app = Flask(__name__, template_folder='templates')

# Gemini API key
GEMINI_API_KEY = "AIzaSyCm-WQQEG9df3hg0f6hqDhKrfqxVcIud-Y"
genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel('gemini-2.0flash')

def get_response(user_input):
    user_input_clean = user_input.lower().strip()
    if "hello" in user_input_clean or "hi" in user_input_clean:
        return "Hello! How can I help you today?"
    elif "your name" in user_input_clean:
        return "I'm CodSoftBot, your virtual assistant."
    elif "help" in user_input_clean:
        return "Sure! Ask me anything about the internship or tasks."
    elif "bye" in user_input_clean or "exit" in user_input_clean or "quit" in user_input_clean:
        return "Goodbye! Have a great day."
    else:
        try:
            response = model.generate_content(user_input)
            return response.text.strip()
        except Exception as e:
            return f"Sorry, I couldn't fetch an answer right now. ({e})"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = get_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True) 