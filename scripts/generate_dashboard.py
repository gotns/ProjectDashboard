import sqlite3
import json
import os

DB_PATH = "dashboard/mission_control.db"
TEMPLATE_PATH = "dashboard/templates/index.html"
OUTPUT_PATH = "dashboard/dashboard_snapshot.html"

def get_data():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    data = {
        "agents": [dict(r) for r in cursor.execute("SELECT * FROM agent_status").fetchall()],
        "tasks": [dict(r) for r in cursor.execute("SELECT * FROM tasks").fetchall()],
        "pipeline": [dict(r) for r in cursor.execute("SELECT * FROM content_pipeline").fetchall()],
        "memories": [dict(r) for r in cursor.execute("SELECT * FROM memories ORDER BY created_at DESC").fetchall()],
    }
    conn.close()
    return data

def generate():
    print("Generating dashboard snapshot...")
    data = get_data()
    
    with open(TEMPLATE_PATH, "r") as f:
        html = f.read()
    
    # Inject the data as a global JS variable
    json_data = json.dumps(data, indent=4)
    injection = f"\n    const EMCEE_DATA = {json_data};\n"
    
    # Modify the Alpine.js init function to use local data instead of fetch
    old_init = """
                async init() {
                    await this.refreshData();
                    setInterval(() => this.refreshData(), 5000);
                },
                async refreshData() {
                    this.agents = await (await fetch('/api/agents')).json();
                    this.tasks = await (await fetch('/api/tasks')).json();
                    this.pipeline = await (await fetch('/api/pipeline')).json();
                    this.memories = await (await fetch('/api/memories')).json();
                },"""
    
    new_init = """
                init() {
                    this.refreshData();
                },
                refreshData() {
                    this.agents = EMCEE_DATA.agents;
                    this.tasks = EMCEE_DATA.tasks;
                    this.pipeline = EMCEE_DATA.pipeline;
                    this.memories = EMCEE_DATA.memories;
                },"""
    
    html = html.replace(old_init, new_init)
    
    # Place the data variable inside the script tag
    html = html.replace("<script>", f"<script>{injection}")
    
    with open(OUTPUT_PATH, "w") as f:
        f.write(html)
    
    print(f"Successfully generated snapshot at: {OUTPUT_PATH}")

if __name__ == "__main__":
    generate()
