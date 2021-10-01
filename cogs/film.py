from discord.ext import commands
import discord
from discord.utils import get
from imdb import IMDb
import numpy as np
import time


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

        if user != self.bot.user:
            reactions_yes = get(message.reactions, emoji="\U0001F44D")
            reactions_no = get(message.reactions, emoji="\U0001F44E")
            count = reactions_yes.count + reactions_no.count
            if count > 3:
                return
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

    @commands.command(name="watchlist", help="Lists the watchlist")
    async def list_watchlist(self, ctx, item):
        watchlist = "./data/watchlist.dat"
        completed = "./data/completed.dat"
        title, kind, year, genre, rating = np.loadtxt(watchlist, unpack=True, delimiter=",", dtype="str")
        counter = 0

        if type(title) != np.ndarray:
            title = [title]
            kind = [kind]
            year = [year]
            genre = [genre]
            rating = [rating]

        if str(item) == "all":
            embed = discord.Embed(title="Watchlist")

            for i in range(len(title)):
                counter += 1
                string1 = title[i]
                string2 = "**Type:** " + kind[i] + " **Year:** " + year[i] + " **Genre:** " + genre[i] + " **Score:** " + rating[i]

                embed.add_field(name=string1, value=string2, inline=False)

            await ctx.send(embed=embed)

        if str(item) == "completed":
            title, kind, year, genre, rating = np.loadtxt(completed, unpack=True, delimiter=",", dtype="str")
            embed = discord.Embed(title="Watchlist: Completed")

            for i in range(len(title)):
                counter += 1
                string1 = title[i]
                string2 = "**Type:** " + kind[i] + " **Year:** " + year[i] + " **Genre:** " + genre[i] + " **Score:** " + rating[i]

                embed.add_field(name=string1, value=string2, inline=False)

            await ctx.send(embed=embed)

        if str(item) == "films":
            embed = discord.Embed(title="Watchlist: Films")

            for i in range(len(title)):
                if kind[i] == "Movie":
                    counter += 1
                    string1 = title[i]
                    string2 = "**Year:** " + year[i] + " **Genre:** " + genre[i] + " **Score:** " + rating[i]

                    embed.add_field(name=string1, value=string2, inline=False)

            if counter != 0:
                await ctx.send(embed=embed)

        if str(item) == "tv" or str(item) == "TV":
            embed = discord.Embed(title="Watchlist: TV Shows")

            for i in range(len(title)):
                if "Tv" in kind[i] or "TV" in kind[i] or "tv" in kind[i]:
                    counter += 1
                    string1 = title[i]
                    string2 = "**Type:** " + kind[i] + " **Year:** " + year[i] + " **Genre:** " + genre[i] + " **Score:** " + rating[i]

                    embed.add_field(name=string1, value=string2, inline=False)

            if counter != 0:
                await ctx.send(embed=embed)

        if counter == 0:
            await ctx.send("No items found!")

    def get_info(self, name):
        ia = IMDb()
        try:
            top_result = ia.search_movie(name)[0]
            movie = ia.get_movie(top_result.getID())
            title = movie["title"]
            year = movie["year"]
            kind = movie["kind"].title()
            genres = movie["genres"][0]
            try:
                cover = movie["full-size cover url"]
            except:
                cover = None
            try:
                outline = movie["plot outline"]
                if len(outline) > 500:
                    outline = outline[:500] + "..."
            except:
                try:
                    outline = movie["plot"]
                    if type(outline) == list:
                        outline = outline[0]
                    if len(outline) > 500:
                        outline = outline[:500] + "..."
                except:
                    outline = "No synopsis found!"
            cast = movie["cast"][:4]
            rating = movie["rating"]
            language = movie["languages"][0]
            runtimes = movie["runtimes"][0]
        except:
            pass

        return title, year, kind, genres, cover, outline, cast, rating, language, runtimes

    def make_embed(self, name):
        watchlist = "./data/watchlist.dat"

        title, year, kind, genres, cover, outline, cast, rating, language, runtimes = self.get_info(name)

        embed = discord.Embed(title=title)

        try:
            if cover != None:
                embed.set_thumbnail(url=cover)
            embed.add_field(name="Synopsis", value=outline, inline=False)
            embed.add_field(name="Cast", value=f"{cast[0]}, {cast[1]}, {cast[2]}, {cast[3]}", inline=False)
            embed.add_field(name="General Details",
                            value=f"Type: {kind}\n"
                                  f"Year: {year}\n"
                                  f"Genre: {genres}",
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
            myFile.write(title + "," + kind + "," + str(year) + "," + genres + "," + str(rating) + "\n")

        return embed

    @commands.command(name="complete", help="Marks an item on watchlist as completed")
    async def complete(self, ctx, item):
        user_input = str(item)
        title, *rest = self.get_info(user_input)
        watchlist = "./data/watchlist.dat"
        completed = "./data/completed.dat"

        with open(watchlist, "r") as readFile:
            lines = readFile.readlines()

        with open(watchlist, "w") as writeFile:
            writeFile.writelines([item for item in lines if title not in item])

        with open(completed, "a") as myFile:
            myFile.writelines([item for item in lines if title in item])

        with open(watchlist, "r") as readFile:
            new_lines = readFile.readlines()

        if len(new_lines) < len(lines):
            message = "Removed " + title + " from Watchlist!"
            await ctx.send(message)
        else:
            message = "Could not find " + title + " in Watchlist."
            await ctx.send(message)


def setup(bot):
    bot.add_cog(Film(bot))
