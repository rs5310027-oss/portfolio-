import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello! I am your bot 🤖")

bot.run("YOUR_BOT_TOKEN")
