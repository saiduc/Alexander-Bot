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
                # the movie is already added to list, but will be deleted if user answers no
                msg = await message_channel.send("Add to Watch List?")
                await msg.add_reaction("\U0001F44D")
                await msg.add_reaction("\U0001F44E")
        else:
            return

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        emoji = payload.emoji
        watchlist = "./data/watchlist.dat"

        if user != self.bot.user:
            if "Add to Watch List?" in str(message.content):
                r = str(str(emoji).encode("unicode-escape").decode("ASCII"))
                if r == r"\U0001f44d":
                    await channel.send("Adding to Watch List!")
                elif r == r"\U0001f44e":
                    await channel.send("Not adding to Watch List!")
                    with open(watchlist) as readFile:
                        lines = readFile.readlines()
                    with open(watchlist, "w") as writeFile:
                        writeFile.writelines([item for item in lines[:-1]])


    def make_embed(self, name):
        watchlist = "./data/watchlist.dat"
        ia = IMDb()
        try:
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
        except:
            pass

        embed = discord.Embed(title=title)

        try:
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
        except:
            msg = "Unfortunately, I couldn't find the necessary information. Sorry!"
            embed.add_field(name="Error", value=msg, inline=False)

        with open(watchlist, "a") as myFile:
            myFile.write(title + "\n")

        return embed


def setup(bot):
    bot.add_cog(Film(bot))
