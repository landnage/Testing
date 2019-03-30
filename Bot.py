import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time

bot = commands.Bot(command_prefix = ".")

@bot.event
async def on_ready():
    print("Your Bot is ready to use ")
    print("Welcome Admin! ")

@bot.event
async def on_message(message):
	author = message.author
	content = message.content
	print('{}: {}'.format(author, content))
	if message.content.startswith('.ping'):
		await message.channel.send("Pong!")
	elif message.content.startswith('.Hello'): 
		await message.channel.send('Hi, How are you today ? ')

@bot.event
async def on_message_join(member):
	for channel in member.server.channels:
		if str(channel) == "join-and-leave":
			await bot.message.send("""Welcome to the Server {member.mention} Hope you have a Great time here""")


bot.run("NTYxMDUxMDQ1NzUzNjUxMjMw.D3-m0w.4JGSFXNe5jxutaxo6DmmkaKa3ig") 
