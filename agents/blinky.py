from agents.base_agent import BaseAgent
import asyncio
import sqlite3
import json
from agents.base_agent import DB_PATH

class Blinky(BaseAgent):
    def __init__(self):
        super().__init__("Blinky")
        self.keywords = ["AI", "Agent", "LLM", "Autonomous", "Automation", "Open Source", "Machine Learning"]

    async def execute(self, **kwargs):
        """Defines the strategy: Blinky needs the top stories from HN and Reddit."""
        self.update_status("Requesting Trends...")
        # We return a 'Strategy' object that the PI Agent orchestrator will act upon
        return {
            "action": "web_search",
            "query": "top stories from Hacker News and Reddit today about AI agents and autonomous systems",
            "agent": self.name
        }

    async def process(self, data: str, **kwargs):
        """Processes the raw text data returned from the PI Agent's tools."""
        self.update_status("Scoring Trends...")
        self.log_task("Morning Scan", "Processing live web results and scoring topics.")
        
        # A real implementation would parse the data. 
        # Assuming 'data' is a list of search results or a summary.
        
        # Very basic scoring mechanism: search for keywords
        lines = data.split('\n')
        found_any = False
        
        with sqlite3.connect(DB_PATH) as conn:
            for line in lines:
                if any(kw.lower() in line.lower() for kw in self.keywords):
                    # Extract a simplified 'topic' from the line
                    topic = line.strip()[:100]
                    # Simple score based on keyword density
                    score = sum(20 for kw in self.keywords if kw.lower() in line.lower())
                    score = min(score, 100)
                    
                    conn.execute(
                        "INSERT INTO content_pipeline (topic, source, score, status) VALUES (?, ?, ?, ?)",
                        (topic, "PI Agent Search", score, "watchlist")
                    )
                    found_any = True
            conn.commit()
        
        self.update_status("Idle")
        return f"Blinky processed {len(lines)} lines and found {found_any} relevant topics."
