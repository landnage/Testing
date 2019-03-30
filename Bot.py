import discord
from discord.ext import commands
import asyncio

bot = commands.Bot(command_prefix=".", status=discord.Status.idle, activity=discord.Game(name="Booting..."))
bot.remove_command("help")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(name="Active"))
    print("Your Bot is ready to use ")


@bot.event
async def on_message(message):
	author = message.author
	content = message.content
	print('{}: {}'.format(author, content))
	if message.content.startswith('.ping'):
		await message.channel.send("Pong!")
	elif message.content.startswith('.Hello'): 
		await message.channel.send('Hi, How are you today ? ')

@bot.command()
async def user(ctx, member:discord.User = None):
    if member == None:
        member = ctx.message.author
        pronoun = "Your"
    else:
        pronoun = "Their"
    name = """{member.name}#{member.discriminator}"""
    status = member.status
    joined = member.joined_at
    role = member.top_role
    await ctx.channel.send("{pronoun} name is {name}. {pronoun} status is {status}. They joined at {joined}. {pronoun} rank is {role}.")



bot.run("NTYxMDUxMDQ1NzUzNjUxMjMw.D3-m0w.4JGSFXNe5jxutaxo6DmmkaKa3ig") 
