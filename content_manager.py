import sqlite3

def initialize_database():
    conn = sqlite3.connect("content_calendar.db")
    cursor = conn.cursor()
    
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS content(
        id INTEGER PRIMARY KEY,
        date TEXT,
        content_type TEXT,
        description TEXT,
        platform TEXT,
        status TEXT,
        notes TEXT,
        link TEXT,
        views INTEGER,
        likes INTEGER,
        shares INTEGER,
        comments INTEGER
    )
    """)
    
    conn.commit()
    conn.close()

def add_content(date, content_type, description, platform, status, notes, link):
    conn = sqlite3.connect("content_calendar.db")
    cursor = conn.cursor()
    
    cursor.execute("INSERT INTO content (date, content_type, description, platform, status, notes, link) VALUES (?, ?, ?, ?, ?, ?, ?)", (date, content_type, description, platform, status, notes, link))
    
    conn.commit()
    conn.close()

# First, run initialize_database() to set up your database
initialize_database()

# Then, you can add content using the add_content function
add_content("2023-09-12", "Video", "Intro to Quitclaim Deeds", "YouTube", "Idea", "First in the series", "link_to_video")

from flask import Flask, request, render_template, jsonify
import sqlite3

app = Flask(__name__)

# Existing functions for the database...

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_content', methods=['POST'])
def add_entry():
    data = request.json
    date = data.get('date')
    content_type = data.get('content_type')
    description = data.get('description')
    platform = data.get('platform')
    status = data.get('status')
    notes = data.get('notes')
    link = data.get('link')
    
    add_content(date, content_type, description, platform, status, notes, link)
    
    return jsonify({"message": "Content added successfully!"})

if __name__ == '__main__':
    app.run(debug=True)
