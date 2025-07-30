from flask import Flask, request, jsonify, render_template
from chatbot import ChatBot

app = Flask(__name__)
bot = ChatBot()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_question = request.json.get('question', '')
    if not user_question:
        return jsonify({'error': 'No question provided'}), 400
    answer = bot.get_answer(user_question)
    return jsonify({'answer': answer})

if __name__ == '__main__':
    app.run(debug=True)
