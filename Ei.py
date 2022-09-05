# Import the os module.
import os
# Import discord.py
import discord
# Import Inspirobot
import inspirobot
# Import datetime
import datetime
# Import asyncio
import asyncio
# Import random
import random

# IMPORT LOAD_DOTENV FUNCTION FROM DOTENV MODULE.
from dotenv import load_dotenv
# IMPORT COMMANDS FROM THE DISCORD.EXT MODULE.
from discord.ext import commands
# IMPORT COMMANDS FROM Commands.py
from Commands import Commands

# LOADS THE .ENV FILE THAT RESIDES ON THE SAME LEVEL AS THE SCRIPT.
load_dotenv()
# GRAB THE API TOKEN FROM THE .ENV FILE.
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# Initialize the list of commands
COMMAND_LIST = {}
# Read all the commands and descriptions from the "CommandDescriptions.txt" file.
myfile = open("CommandDescriptions.txt")
next_line = myfile.readline()
count = 0
command_name = next_line.strip("\n")
command_description = ""
while next_line != "":
    count += 1
    if count % 2 != 0 and next_line.strip("\n") != "":
        command_name = next_line.strip("\n")
        # print(command_name + str(count))
    elif count % 2 == 0 and next_line.strip("\n") != "":
        command_description = next_line.strip("\n")
        # print(command_description)
    next_line = myfile.readline()
    COMMAND_LIST[command_name] = command_description

# Class for custom help command
class CustomHelpCommand(commands.HelpCommand):

    def __init__(self):
        super().__init__()

    # Called when !help is called
    async def send_bot_help(self, mapping):
        em = discord.Embed(title = "Help", description = "Use !help and a command name for more info on each command :dango:~", color = discord.Colour.purple())
        em.add_field(name = "Utility", value = "dango, schedulemessage")
        em.add_field(name = "Fun", value =  "8ball, blessing")
        await self.get_destination().send(embed = em)

    # Called when !help [command name] is called.
    async def send_command_help(self, command):
        em = discord.Embed(title = command.name, description = COMMAND_LIST[command.name], color = discord.Colour.purple())
        await self.get_destination().send(embed = em)

# CREATES A NEW BOT OBJECT WITH A SPECIFIED PREFIX. IT CAN BE WHATEVER YOU WANT IT TO BE.
client = commands.Bot(command_prefix = "!", help_command = CustomHelpCommand(), intents = discord.Intents.all())
# Add the Commands cog
client.add_cog(Commands(client))

# EVENT LISTENER FOR WHEN THE BOT HAS SWITCHED FROM OFFLINE TO ONLINE.
@client.event
async def on_ready():
    # CREATES A COUNTER TO KEEP TRACK OF HOW MANY GUILDS / SERVERS THE BOT IS CONNECTED TO.
    guild_count = 0
    # LOOPS THROUGH ALL THE GUILD / SERVERS THAT THE BOT IS ASSOCIATED WITH.
    for guild in client.guilds:
        # PRINT THE SERVER'S ID AND NAME.
        print(f"- {guild.id} (name: {guild.name})")
        # INCREMENTS THE GUILD COUNTER.
        guild_count = guild_count + 1
    # PRINTS HOW MANY GUILDS / SERVERS THE BOT IS IN.
    print("Ei is granting " + str(guild_count) + " electro visions.")

# EXECUTES THE BOT WITH THE SPECIFIED TOKEN.
if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
