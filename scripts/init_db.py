import sqlite3
from datetime import datetime

DB_PATH = "dashboard/mission_control.db"

def init_db():
    with sqlite3.connect(DB_PATH) as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS agent_status (
            agent_name TEXT PRIMARY KEY, 
            current_status TEXT, 
            last_update TEXT
        )''')
        
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task_name TEXT, 
            owner TEXT, 
            status TEXT, 
            activity_log TEXT, 
            updated_at TEXT
        )''')
        
        conn.execute('''CREATE TABLE IF NOT EXISTS content_pipeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            topic TEXT, 
            source TEXT, 
            score INTEGER, 
            status TEXT, 
            content_link TEXT
        )''')
        
        conn.execute('''CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            content TEXT, 
            type TEXT, 
            created_at TEXT
        )''')
        
        agents = [
            ('Blinky', 'Idle', datetime.now().isoformat()),
            ('Pinky', 'Idle', datetime.now().isoformat()),
            ('Dinky', 'Idle', datetime.now().isoformat()),
            ('Linky', 'Idle', datetime.now().isoformat()),
            ('Winky', 'Idle', datetime.now().isoformat()),
        ]
        conn.executemany('INSERT OR IGNORE INTO agent_status VALUES (?, ?, ?)', agents)
        conn.commit()
    print("Database initialized successfully.")

if __name__ == "__main__":
    init_db()
