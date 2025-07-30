import json
import sqlite3

def init_db(json_path='mechanical_data.json', db_path='mechanical.db'):
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create table if it doesn't exist
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS qa_pairs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            question TEXT,
            answer TEXT
        )
    ''')

    # Load JSON and extract the 'questions' list
    with open(json_path, 'r') as f:
        data = json.load(f)
        questions = data.get("questions", [])

        for entry in questions:
            cursor.execute('''
                INSERT INTO qa_pairs (question, answer) VALUES (?, ?)
            ''', (entry['question'], entry['answer']))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    init_db()
