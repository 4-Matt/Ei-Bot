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

# Import load_dotenv function from dotenv module
from dotenv import load_dotenv
# Import commands from the discord.ext module
from discord.ext import commands
# Import commands from Commands.py
from Commands import Commands

# Loads the .env file
load_dotenv()
# Grab the token from the .env file
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
    elif count % 2 == 0 and next_line.strip("\n") != "":
        command_description = next_line.strip("\n")
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

# Creates a new bot object with a specified prefix.
client = commands.Bot(command_prefix = "!", help_command = CustomHelpCommand())
# Add the Commands cog
client.add_cog(Commands(client))

# Event listener - runs when the bot goes online.
@client.event
async def on_ready():
    # Initializes a server counter
    guild_count = 0
    # Loops through every server the bot is in
    for guild in client.guilds:
        # Print the server's id and name.
        print(f"- {guild.id} (name: {guild.name})")
        # Increments the server counter
        guild_count = guild_count + 1
    # Prints the number of servers the bot is in
    print("Ei is granting " + str(guild_count) + " electro visions.")

# Executes the bot
if __name__ == "__main__":
    client.run(DISCORD_TOKEN)
