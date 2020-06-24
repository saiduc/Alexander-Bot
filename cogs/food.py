from discord.ext import commands
import validators


class Food(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        recipes = "./data/recipes.dat"
        isRecipe = False

        if message.author == self.bot.user:
            return
        if message.channel.id == 719512855984210011:
            item = message.content

            if validators.url(item):
                isRecipe = True

            elif item[:7] != "http://":
                item = "http://" + item
                if validators.url(item):
                    isRecipe = True

            if isRecipe:
                response = f"Adding item to recipe book! Please select the type of food:"

                msg = await message.channel.send(response)
                await msg.add_reaction("\U0001F96F")
                await msg.add_reaction("\U0001F9C1")
                await msg.add_reaction("\U0001F9C6")
                await msg.add_reaction("\U0001F35B")
                await msg.add_reaction("\U0001F9C9")
                with open(recipes, "a") as myfile:
                    myfile.write(item+"\n")


def setup(bot):
    bot.add_cog(Food(bot))

