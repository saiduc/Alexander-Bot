from discord.ext import commands, tasks
from datetime import date, datetime
import numpy as np


class Exercise(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reminder.start()

    def cog_unload(self):
        self.reminder.cancel()

    @commands.command(name="checkin", help="Check in for the day")
    async def check_in(self, ctx):
        response = str(ctx.author)[:-5] + " has checked in for the day!"
        await ctx.send(response)

        log = "./data/log.dat"
        with open(log, "a") as myfile:
            item = str(ctx.author)[:-5] + "," + str(date.today()) + "\n"
            myfile.write(item)

    @commands.command(name="zrobione", help="Check in for the day")
    async def zrobione(self, ctx):
        if str(ctx.author) == "SaiDuc#4556" or str(ctx.author) == "zztop66#0863":
            response = str(ctx.author)[:-5] + " ukończył ćwiczenia na dzisiaj!"
        else:
            response = str(ctx.author)[:-5] + " ukończyła ćwiczenia na dzisiaj!"
        await ctx.send(response)

        log = "./data/log.dat"
        with open(log, "a") as myfile:
            item = str(ctx.author)[:-5] + "," + str(date.today()) + "\n"
            myfile.write(item)

    @tasks.loop(seconds=60.0)
    async def reminder(self):
        message_channel = self.bot.get_channel(725329702985662505)
        current_time = datetime.now().strftime("%H:%M:%S")
        if current_time[:2] == "19" and current_time[3:5] == "00":
            log = "./data/log.dat"
            names, times = np.loadtxt(log, dtype="str", unpack=True, delimiter=",")
            members = ["Kasiakoo", "SaiDuc", "zuziek424", "zztop66"]
            people = []
            for i in range(len(times)):
                if times[i] == str(date.today()):
                    people.append(names[i])
            for i in members:
                if i not in people:
                    response = i + " has not checked in today!"
                    await message_channel.send(response)
        else:
            return


def setup(bot):
    bot.add_cog(Exercise(bot))
