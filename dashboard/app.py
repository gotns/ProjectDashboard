from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import sqlite3
from datetime import datetime
import uvicorn

app = FastAPI()

# Setup templates and static files
templates = Jinja2Templates(directory="dashboard/templates")
app.mount("/static", StaticFiles(directory="dashboard/static"), name="static")

DB_PATH = "dashboard/mission_control.db"

def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    with get_db_connection() as conn:
        # Agents Table
        conn.execute('''CREATE TABLE IF NOT EXISTS agent_status (
            agent_name TEXT PRIMARY KEY, 
            current_status TEXT, 
            last_update TEXT
        )''')
        
        # Tasks Table
        conn.execute('''CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            task_name TEXT, 
            owner TEXT, 
            status TEXT, 
            activity_log TEXT, 
            updated_at TEXT
        )''')
        
        # Content Pipeline Table
        conn.execute('''CREATE TABLE IF NOT EXISTS content_pipeline (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            topic TEXT, 
            source TEXT, 
            score INTEGER, 
            status TEXT, 
            content_link TEXT
        )''')
        
        # Memories Table
        conn.execute('''CREATE TABLE IF NOT EXISTS memories (
            id INTEGER PRIMARY KEY AUTOINCREMENT, 
            content TEXT, 
            type TEXT, 
            created_at TEXT
        )''')
        
        # Seed some initial data for agents
        agents = [
            ('Blinky', 'Idle', datetime.now().isoformat()),
            ('Pinky', 'Idle', datetime.now().isoformat()),
            ('Dinky', 'Idle', datetime.now().isoformat()),
            ('Linky', 'Idle', datetime.now().isoformat()),
            ('Winky', 'Idle', datetime.now().isoformat()),
        ]
        conn.executemany('INSERT OR IGNORE INTO agent_status VALUES (?, ?, ?)', agents)
        conn.commit()

@app.on_event("startup")
async def startup_event():
    init_db()

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/api/agents")
async def get_agents():
    with get_db_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM agent_status").fetchall()]

@app.get("/api/tasks")
async def get_tasks():
    with get_db_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM tasks").fetchall()]

@app.get("/api/pipeline")
async def get_pipeline():
    with get_db_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM content_pipeline").fetchall()]

@app.get("/api/memories")
async def get_memories():
    with get_db_connection() as conn:
        return [dict(row) for row in conn.execute("SELECT * FROM memories ORDER BY created_at DESC").fetchall()]

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
