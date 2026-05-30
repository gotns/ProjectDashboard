from agents.base_agent import BaseAgent
import asyncio
import sqlite3
from agents.base_agent import DB_PATH

class Pinky(BaseAgent):
    def __init__(self):
        super().__init__("Pinky")

    async def execute(self, topic=None, **kwargs):
        """Strategy: Find the highest scoring 'watchlist' topic and request a deep dive."""
        self.update_status("Selecting Topic...")
        
        with sqlite3.connect(DB_PATH) as conn:
            conn.row_factory = sqlite3.Row
            row = conn.execute(
                "SELECT topic FROM content_pipeline WHERE status = 'watchlist' ORDER BY score DESC LIMIT 1"
            ).fetchone()
            
            if not row:
                self.update_status("Idle (No Topics)")
                return {"action": "idle", "message": "No topics in watchlist."}
            
            target_topic = row['topic']
            self.log_task("Deep Dive Selection", f"Selected topic for research: {target_topic}")
            
            return {
                "action": "web_search",
                "query": f"technical deep dive and detailed analysis of {target_topic}: current state, implementation challenges, and leading approaches",
                "agent": self.name,
                "topic": target_topic
            }

    async def process(self, data: str, topic=None, **kwargs):
        """Processes research data into a structured format."""
        self.update_status(f"Analyzing {topic}...")
        self.log_task("Deep Dive Complete", f"Finished researching {topic}.")
        
        # 1. Move the topic from watchlist to 'approved' (or a research state if we had one)
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "UPDATE content_pipeline SET status = 'approved' WHERE topic = ?",
                (topic,)
            )
            conn.commit()
        
        # In a real system, this data would be saved to a research.md file
        # For now, we log it as a success.
        self.update_status("Idle")
        return f"Pinky: Completed deep-dive on {topic}. Data processed and topic promoted to approved."
