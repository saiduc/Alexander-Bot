from discord.ext import commands
import discord
from imdb import IMDb


class Film(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.bot.user:
            return

        if message.channel.id == 724623778356658256:
            message_channel = self.bot.get_channel(724623778356658256)
            if message.content[0] == "{" and message.content[-1] == "}":
                name = message.content[1:-1]
                embed_item = self.make_embed(name)
                await message_channel.send(embed=embed_item)
        else:
            return

    def make_embed(self, name):
        ia = IMDb()
        top_result = ia.search_movie(name)[0]
        movie = ia.get_movie(top_result.getID())

        title = movie["title"]
        year = movie["year"]
        kind = movie["kind"].title()
        genres = movie["genres"]
        cover = movie["full-size cover url"]
        outline = movie["plot outline"]
        cast = movie["cast"][:4]
        rating = movie["rating"]
        language = movie["languages"][0]
        runtimes = movie["runtimes"][0]

        embed = discord.Embed(title=title)
        embed.set_thumbnail(url=cover)
        embed.add_field(name="Synopsis", value=outline, inline=False)
        embed.add_field(name="Cast", value=f"{cast[0]}, {cast[1]}, {cast[2]}, {cast[3]}", inline=False)
        embed.add_field(name="General Details",
                        value=f"Type: {kind}\n"
                              f"Year: {year}\n"
                              f"Genre: {genres[0]}",
                        inline=True)
        embed.add_field(name="Other Details",
                        value=f"Score: {rating}\n"
                              f"Language: {language}\n"
                              f"Runtime: {runtimes} minutes",
                        inline=True)
        return embed


def setup(bot):
    bot.add_cog(Film(bot))
