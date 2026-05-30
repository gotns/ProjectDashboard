import asyncio
import sys
import json
import argparse
from agents.blinky import Blinky
from agents.pinky import Pinky
from agents.dinky import Dinky
from agents.linky import Linky
from agents.winky import Winky

# Agent Map
AGENTS = {
    "blinky": Blinky,
    "pinky": Pinky,
    "dinky": Dinky,
    "linky": Linky,
    "winky": Winky
}

async def main():
    parser = argparse.ArgumentParser(description="emCee Agent Bridge")
    parser.add_argument("--agent", required=True, help="Agent name (e.g., blinky)")
    parser.add_argument("--action", required=True, choices=["execute", "process"], help="Action to perform")
    parser.add_argument("--data", help="Input data for the process action")
    parser.add_argument("--topic", help="Topic for the process action")
    
    args = parser.parse_args()
    
    agent_class = AGENTS.get(args.agent.lower())
    if not agent_class:
        print(f"Error: Agent {args.agent} not found.")
        sys.exit(1)
    
    agent = agent_class()
    
    if args.action == "execute":
        # Returns the strategy for the PI Agent to execute
        result = await agent.execute()
        print(json.dumps(result))
    
    elif args.action == "process":
        if not args.data:
            print("Error: --data is required for process action.")
            sys.exit(1)
        result = await agent.process(args.data, topic=args.topic)
        print(result)

if __name__ == "__main__":
    asyncio.run(main())
