import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")

bot = commands.Bot(command_prefix="!")

bot.load_extension("cogs.misc")


@bot.event
async def on_ready():
    print("AlexanderBot is running...")

bot.run(TOKEN)
