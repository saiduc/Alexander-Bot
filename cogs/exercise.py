from discord.ext import commands
from datetime import date


class Exercise(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="checkin", help="Check in for the day")
    async def check_in(self, ctx):
        response = str(ctx.author)[:-5] + " has checked in for the day!"
        await ctx.send(response)

        log = "./data/log.dat"
        with open(log, "a") as myfile:
            item = str(ctx.author)[:-5] + "," + str(date.today()) + "\n"
            myfile.write(item)

    @commands.command(name="zrobione", help="Check in for the day")
    async def check_in(self, ctx):
        if str(ctx.author) == "SaiDuc#4556":
            response = str(ctx.author)[:-5] + " ukończył ćwiczenia na dzisiaj!"
        else:
            response = str(ctx.author)[:-5] + " ukończyła ćwiczenia na dzisiaj!"
        await ctx.send(response)

        log = "./data/log.dat"
        with open(log, "a") as myfile:
            item = str(ctx.author)[:-5] + "," + str(date.today()) + "\n"
            myfile.write(item)


def setup(bot):
    bot.add_cog(Exercise(bot))
