import discord
from discord.ext import commands
# Import Inspirobot
import inspirobot
# Import datetime
import datetime
# Import calendar
import calendar
# Import asyncio
import asyncio
# Import random
import random

# Initialize the 8ball responses
EIGHTBAAL_RESPONSES = []
newfile = open("8ball_responses.txt")
for line in newfile:
    EIGHTBAAL_RESPONSES.append(line.strip('\n'))

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client
    # When a command is given starting with the command prefix and "dango", return "milk" and a cute emoji.
    @commands.command()
    async def dango(self, ctx):
        em = discord.Embed(title = "milk :bubble_tea:", description = "(" + str(self.client.latency)[0:5] + "ms) :ping_pong:", color = discord.Colour.purple())
        await ctx.send(embed = em)

    # Generates a quote with the inspirobot API and sends it to the channel.
    @commands.command()
    async def blessing(self, ctx):
        quote = inspirobot.generate()
        print(quote)
        message = "When thou asketh the Almighty Narukami Ogosho for a blessing, thou shalt receive. :purple_heart:"
        await ctx.send(message)
        await ctx.send(quote)

    @commands.command(aliases = ['8ball'])
    async def eightball(self, ctx, *args):
        # Get Message Content
        msg = ''
        for item in args:
            item += " "
            msg += item
        if msg == '':
            em = discord.Embed(title = msg, description = "Insolent! At least ask a question...:pensive:", color = discord.Colour.purple())
            await ctx.send(embed = em)
        else:
            index = random.randint(0, 19)
            em = discord.Embed(title = msg, description = EIGHTBAAL_RESPONSES[index], color = discord.Colour.purple())
            await ctx.send(embed = em)

    @commands.command()
    async def schedulemessage(self, ctx, days: int, hours: int, minutes: int, *args):
        # Get Message Content
        msg = ''
        for item in args:
            item += " "
            msg += item
        wait_time = ((days * 86400) + (hours * 3600) + (minutes * 60))
        await ctx.send(f'\"{msg}\" will be sent {days} days, {hours} hours, and {minutes} minutes from now!~')
        # wait x amount of timex
        await asyncio.sleep(wait_time)
        await ctx.send(msg)

