from discord.ext import commands


class Miscellaneous(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="bob", help="Calls the other person a bobas")
    async def call_bob(self, ctx):
        if str(ctx.author) == "SaiDuc#4556":
            response = "Kasia is a bobas!"
        elif str(ctx.author) == "Kasiakoo#4933":
            response = "Sai is a bobas!"
        await ctx.send(response)

    @commands.command(name="hello", help="Says hello")
    async def say_hello(self, ctx):
        response = "Hello!"
        await ctx.send(response)


def setup(bot):
    bot.add_cog(Miscellaneous(bot))
