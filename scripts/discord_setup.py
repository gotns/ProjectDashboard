import discord
import asyncio
import os

# Configuration - These would typically come from environment variables
TOKEN = os.getenv('DISCORD_BOT_TOKEN')
GUILD_ID = os.getenv('DISCORD_GUILD_ID')

class emCeeSetupBot(discord.Client):
    async def on_ready(self):
        print(f'Logged in as {self.user}')
        
        if not GUILD_ID:
            print("Error: DISCORD_GUILD_ID environment variable not set.")
            await self.close()
            return

        guild = self.get_guild(int(GUILD_ID))
        if not guild:
            print("Error: Could not find guild. Check your GUILD_ID.")
            await self.close()
            return

        channels_to_create = [
            ("#general", "For direct text communication and manual task execution."),
            ("#daily-digest", "Where morning briefs and industry news updates are compiled."),
            ("#research-deep-dives", "For comprehensive analyses on specific topics."),
            ("#content-ideas", "A queue where you post high-scoring concepts requiring manual approval."),
            ("#system-alerts", "A protected logging channel for twice-daily automated health and security audits."),
        ]

        print(f"Setting up channels for {guild.name}...")

        for channel_name, description in channels_to_create:
            name = channel_name.replace("#", "")
            # Check if channel already exists
            existing_channel = discord.utils.get(guild.text_channels, name=name)
            
            if existing_channel:
                print(f"Channel {channel_name} already exists. Skipping.")
            else:
                # Create channel with specific permissions
                # In a real scenario, we'd set overwrite permissions here for @everyone and the user
                await guild.create_text_channel(name, topic=description)
                print(f"Created {channel_name}: {description}")

        print("Infrastructure setup complete.")
        await self.close()

if __name__ == "__main__":
    if not TOKEN:
        print("Error: DISCORD_BOT_TOKEN environment variable not set.")
    else:
        intents = discord.Intents.default()
        intents.guilds = True
        client = emCeeSetupBot(intents=intents)
        client.run(TOKEN)
