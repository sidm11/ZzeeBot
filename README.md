# Zzee selfbot
Discord.py selfbot

## ATTENTION!
we are not responsible for your discord account!
this program violates the ToS discord rules!
your discord account may be blocked!

happy use! <3

# How do I get my token?
<img src="BigweldIndustries.gif" width="1000">

# about this bot
this bot is for discord account.
this program was written completely from scratch in disnake.py (discord.py)
this program is still in alpha testing, there may be bugs ...
good luck using it!

# How to install and run?
```py
# Linux
git clone https://github.com/KOTE-debug/zzeeBot
cd bot && python start.py
```
# How do I import my team into the bot?
there are 2 ways:
1.via cogs
2.addle to the main file

# Way 1

Open bot/data/account.json
change the parameter "cogs" and add to ["fun.py", "activity.py"]
your file to get it:
```py
["fun.py", "activity.py", "myfile.py"]
```
! Attention! don't forget about square brackets

now create a new file along the path: bot / cogs
let's call it as you indicated in the config!

and insert there:
```py
# imports
import discord, pyfiglet
from discord.ext import commands as zzee 
# class
class mass(zzee.Cog):
    def __init__(self, zzee):
        self.zzee = zzee
#commands
        
@zzee.command()
async def commandName(self, ctx):
    await ctx.send("hello world!") #you code

def setup(zzee):
    zzee.add_cog(mass(zzee))
```
# way 2
Open bot/start.py
