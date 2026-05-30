import asyncio
import json
import subprocess

# This script is a "Helper" for the PI Agent.
# It handles the CLI calls to the agent bridge.

async def call_agent(agent, action, data=None, topic=None):
    cmd = ["python3", "main.py", "--agent", agent, "--action", action]
    if data:
        cmd.extend(["--data", data])
    if topic:
        cmd.extend(["--topic", topic])
    
    process = await asyncio.create_subprocess_exec(
        *cmd,
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.PIPE
    )
    stdout, stderr = await process.communicate()
    
    if stderr:
        print(f"Error from {agent}: {stderr.decode().strip()}")
    
    output = stdout.decode().strip()
    try:
        return json.loads(output)
    except json.JSONDecodeError:
        return output

async def main():
    print("Ready for real-time cycle. Please provide tool outputs as requested.")
    # This script just demonstrates the API. The actual cycle is driven 
    # by the PI Agent (LLM) because the LLM holds the search tool.

if __name__ == "__main__":
    asyncio.run(main())
