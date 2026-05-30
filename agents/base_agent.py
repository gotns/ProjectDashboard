from abc import ABC, abstractmethod
from datetime import datetime
import sqlite3
import os

DB_PATH = "dashboard/mission_control.db"

class BaseAgent(ABC):
    def __init__(self, name):
        self.name = name

    def update_status(self, status):
        """Updates the agent's current status in the Mission Control database."""
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "UPDATE agent_status SET current_status = ?, last_update = ? WHERE agent_name = ?",
                (status, datetime.now().isoformat(), self.name)
            )
            conn.commit()

    def log_task(self, task_name, activity):
        """Logs a task's progress in the Mission Control database."""
        with sqlite3.connect(DB_PATH) as conn:
            conn.execute(
                "INSERT INTO tasks (task_name, owner, status, activity_log, updated_at) VALUES (?, ?, ?, ?, ?)",
                (task_name, self.name, "Active", activity, datetime.now().isoformat())
            )
            conn.commit()

    @abstractmethod
    async def process(self, data: str, **kwargs):
        """Processes external data (from web/tools) and performs agent-specific logic."""
        pass

    @abstractmethod
    async def execute(self, **kwargs):
        """Defines the strategy for what data the agent needs from the orchestrator."""
        pass
