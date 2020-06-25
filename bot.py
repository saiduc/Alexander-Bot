import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

bot = commands.Bot(command_prefix="!")

bot.load_extension("cogs.misc")
bot.load_extension("cogs.food")
bot.load_extension("cogs.exercise")


@bot.event
async def on_ready():
    print("AlexanderBot is running...")

bot.run(TOKEN)
