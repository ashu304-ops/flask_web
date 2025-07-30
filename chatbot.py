import sqlite3
from sentence_transformers import SentenceTransformer, util

class ChatBot:
    def __init__(self, db_path='mechanical.db'):
        self.conn = sqlite3.connect(db_path, check_same_thread=False)
        self.cursor = self.conn.cursor()
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.load_data()

    def load_data(self):
        self.cursor.execute("SELECT id, question, answer FROM qa_pairs")
        rows = self.cursor.fetchall()
        self.qa_pairs = [{'id': row[0], 'question': row[1], 'answer': row[2]} for row in rows]
        self.embeddings = self.model.encode([q['question'] for q in self.qa_pairs], convert_to_tensor=True)

    def get_answer(self, user_question):
        user_embedding = self.model.encode(user_question, convert_to_tensor=True)
        scores = util.cos_sim(user_embedding, self.embeddings)[0]
        best_idx = scores.argmax().item()
        best_score = scores[best_idx].item()
        
        if best_score > 0.6:
            return self.qa_pairs[best_idx]['answer']
        else:
            return "Sorry, I couldn't find an answer. Please rephrase your question."
