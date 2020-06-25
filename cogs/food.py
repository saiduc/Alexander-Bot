from discord.ext import commands
import numpy as np
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
                    myfile.write(item+",")

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        channel = await self.bot.fetch_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)
        user = await self.bot.fetch_user(payload.user_id)
        emoji = payload.emoji
        recipes = "./data/recipes.dat"

        if user != self.bot.user:
            # need to add check to make sure it's first emoji added
            # perhaps check that total number of reactions == 6
            if "Adding item to recipe book! Please select the type of food:" in str(message.content):
                r = str(str(emoji).encode("unicode-escape").decode("ASCII"))
                if r == r"\U0001f96f":
                    await channel.send("You chose breakfast!")
                    with open(recipes, "a") as myfile:
                        myfile.write("breakfast\n")
                if r == r"\U0001f9c1":
                    await channel.send("You chose dessert!")
                    with open(recipes, "a") as myfile:
                        myfile.write("dessert\n")
                if r == r"\U0001f9c6":
                    await channel.send("You chose snack!")
                    with open(recipes, "a") as myfile:
                        myfile.write("snack\n")
                if r == r"\U0001f35b":
                    await channel.send("You chose main course!")
                    with open(recipes, "a") as myfile:
                        myfile.write("main\n")
                if r == r"\U0001f9c9":
                    await channel.send("You chose drink!")
                    with open(recipes, "a") as myfile:
                        myfile.write("drink\n")

    @commands.command(name="food", help="Lists foods in recipe book")
    async def listFoods(self, ctx, food):
        recipes = "./data/recipes.dat"
        links, foodTypes = np.loadtxt(recipes, unpack=True, delimiter=",", dtype="str")
        counter = 0

        if str(food) == "all":
            for i in range(len(links)):
                counter += 1
                await ctx.send(links[i])
        else:
            for i in range(len(links)):
                if foodTypes[i] == str(food):
                    counter += 1
                    await ctx.send(links[i])
        if counter == 0:
            await ctx.send("No items found!")


def setup(bot):
    bot.add_cog(Food(bot))
