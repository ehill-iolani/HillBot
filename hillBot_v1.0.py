# Original code (and idea) by Liam Pearson, c/o 25
# V1.0 finalised 1/16/25 
# discord.py refrence: https://discordpy.readthedocs.io/en/stable/api.html 
# good luck, you poor soul. May the Hill smile upon you for completing this project. 
# to execute as a continuous process: "nohup python3 -u hillBot_v1.0.py" 

# import all needed libraries 
import os
import discord
import datetime
import time
import random

# Import needed commands
from dotenv import load_dotenv
from discord.ext import commands
from asyncio import sleep as s

# get variebles from .env file
#   note: token and guild IDs should be kept in a .env file. Harcoding them into this current file is a security risk for your discord account.
#   Bot may only work witha specific token. Ask Mr. Hill for details. he'll prob figure it out.
load_dotenv()
TOKEN = os.getenv('TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
YUH = os.getenv("YUH")

# Specify the bot's intents
intents = discord.Intents.all()
intents.message_content = True

# define the bot object (only works with the name 'client')
# also scpecify intents here
client = discord.Client(intents=intents)

# This is where you can specify the command prefix.
client = commands.Bot(command_prefix='hill.', intents=intents)
client.remove_command('help')
# the default help command needs to be removed to make the one below work. this could be something to improve on, but it is not currently necissary


# This function is called only once (essentially Void setup() if you know what that means) on the bot's startup
@client.event
async def on_ready():
    await client.change_presence(activity=discord. Activity(type=discord.ActivityType.listening, name='hill.help'))

    # idk what this stuff does. the bot needs it to work
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )

# Format for commands:
    # @client.command() Specifies that a command will follow
    # async def command_name_here(arguments): 
            # await ctx.send("message for bot to send")

#some common arguements:
    # ctx - the command name itself. even if you wont use this in the following code, this arguement must be included first
    # variable_name:discord.User - use only if this variable will contain the name of a discord user. note: this must be the name that pops up when you click on thier profile. not the display name.
    # variable_name any other variable name can be used to store strings, intergers, etc. just like a normal variable. you can specify a variable type by writing variable_name: int/float/string/etc
    # there are other arguemants too. check the refrence if needed


# Fun fact: multiple commands can be run at one time. no need to wory about accidentally bricking the bot if you add too many wait comamnds. 

# help commamnd
@client.command()
async def help(ctx):
    await ctx.send("List of commands: \nhill.help \nhill.yuh \nhill.remind [target] [time (in mins)] [message] \nhill.annoy [target] \n")

# yuh command
@client.command()
async def yuh(ctx):
    print("yuh")
    await ctx.send("yuh")

# remind command
@client.command()
async def remind(ctx, user:discord.User, time: int, *, msg):
    await ctx.send("ok lol")
    await s(60*time)
    await ctx.send(user.mention + " you are being reminded to " + msg)

# annoy command
@client.command()
async def annoy(ctx, user:discord.User):
    await ctx.send("lol bet")

    def check(m):
        return m.author == user

    msg = await client.wait_for('message',check = check)
    print("yuh")
    annoys = ["Bro thinks hes him :skull::skull::skull:",
              "Good luck on that, buddy",
              "Bro's cooked:skull::skull:",
              "is that even a question??????",
              "LMAOOOOOOOOO",
              "yuh",
              "Bro's done",
              ":skull:"]
    await ctx.send(user.mention + " " + random.choice(annoys))
    
# PredictGrade command
@client.command()
async def predictGrade(ctx):
    rand = random.randint(0,101)
    await ctx.send("you will get a " + str(rand))
    if rand < 70:
        time.sleep(1)
        await ctx.send("you're cooked lol")


# This should be placed at the very last line of the code. no code after this will be exicuted
client.run(TOKEN)
