from discord.ext import tasks, commands
import discord
import os
from dotenv.main import load_dotenv
load_dotenv()
client = discord.Client(intents=discord.Intents.all())
@client.event
async def on_message(message):
    if message.author.id == 223914382248116235 or message.author.id == 964060064698736680 or message.author.id == 964079432090390558 or message.author.id == 651455341426376726 or message.author.id == 964361615111770163:
        await message.delete()
        await message.channel.send(message.content)
client.run(os.getenv('DISCORD_TOKEN'))