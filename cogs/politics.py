import asyncio
from discord.ext import commands
import discord
from discord.utils import get
import validators
from functions import summarise


class Politics(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return
        if message.channel.id == 719836420801298472:
            item = message.content

            if validators.url(item):
                isURL = True

            elif item[:7] != "http://":
                item = "http://" + item
                if validators.url(item):
                    isURL = True

            if isURL:
                title, summary, reduced = summarise.get_summary(item)
                if summary is not None:
                    if len(summary) > 2040:
                        summary = summary[:2040] + "..."

                if title is not None and summary is not None:
                    embed = discord.Embed(title=title, description=summary)

                if reduced is not None:
                    footer = "This was the best TLDR I could make. I have shortened the article by " + str(reduced) + "."
                    embed.set_footer(text=footer)

                if title is not None and summary is not None:
                    await message.channel.send(embed=embed)


def setup(bot):
    bot.add_cog(Politics(bot))
