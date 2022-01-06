import disnake as discord
import requests
from discord.ext import commands, tasks
import time
from datetime import datetime
import pyfiglet
import json
import colorama
from colorama import Fore, Back, Style
from os import system as os
import sys
colorama.init()
__lastRun__ = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
__starttime__ = time.time()
open("logs/info.log", "w").write(" ")
print(Fore.GREEN + "Resetting info log.")
open("logs/warning.log", "w").write(" ")
print(Fore.GREEN + "Resetting warning log.")
open("logs/error.log", "w").write(" ")
print(Fore.GREEN + "Resetting error log.")
open("logs/critical.log", "w").write(" ")
print(Fore.GREEN + "Resetting critical log.")
print(" ")
import logging
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='logs/discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
logging.basicConfig(filename="logs/error.log", level=logging.ERROR)
logging.basicConfig(filename="logs/warning.log", level=logging.WARNING)
logging.basicConfig(filename="logs/info.log", level=logging.INFO)
accountJson = json.load(open("data/account.json"))
accountFile = open("data/account.json", "r").read()
__token__ = accountJson["token"]
__cogs__ = accountJson["cogs"] #["name1.py", "start.py"]
__prefix__ = accountJson["prefix"] #+
__logsID__ = accountJson["logsID"] #channel ID
zzee=commands.zzee(command_prefix=__prefix__,help_command=None, selfzzee=True)
for filename in __cogs__:
  if filename.endswith('.py'):
    zzee.load_extension(f'cogs.{filename[:-3]}')
  else:
    print(f'failed load cog {filename[:-3]}')

@zzee.event
async def on_ready():
	await zzee.get_channel(int(__logsID__)).send('<ZzEE bot> zzee started!')
	open("zzee/runinfo.log", "w").write(f"last run: {__lastRun__}\n run time: %s seconds" % (time.time() - __starttime__))
	print(Fore.GREEN + "runinfo edited!")
	print(Fore.GREEN + "prefix: " + __prefix__)
	print("account name: " + zzee.user.name)
	print("bot started!")
	
@zzee.event
async def on_command_error(ctx, error):
    error_str = str(error)
    error = getattr(error, 'original', error)
    if isinstance(error, commands.CommandNotFound):
        return
    elif isinstance(error, commands.CheckFailure):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}You're missing permission to execute this command"+Fore.RESET)
    elif isinstance(error, commands.MissingRequiredArgument):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Missing arguments: {error}"+Fore.RESET)
        await zzee.get_channel(int(__logsID__)).send(f'<ZzEE bot> [error] missing arguments: {error}')
        await ctx.send(f"missing arguments: {error}")
    elif isinstance(error, numpy.AxisError):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Not a valid image"+Fore.RESET)
    elif isinstance(error, discord.errors.Forbidden):
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Discord error: {error}"+Fore.RESET)
        await zzee.get_channel(int(__logsID__)).send('<ZzEE bot> [error] discord error: \n```py\n{error}\n```')
    elif "Cannot send an empty message" in error_str:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Couldnt send a empty message"+Fore.RESET)               
    else:
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{error_str}"+Fore.RESET)
        await ctx.send(f"error! ```py\n{error_str}\n```")
        await zzee.get_channel(int(__logsID__)).send(f'<ZzEE bot> [error] error!:\n```py\n{error}\n```')
      

@zzee.command()
async def nitrosnipe(ctx, arg):
    global nitrosnipestatus
    thing = arg
    await ctx.message.delete()
    if thing == "on":
        nitrosnipestatus = True
    if thing == "off":
        nitrosnipestatus = False

@zzee.event
async def on_message(message):
    global donotdisturb
    global nitrosnipestatus
    global commanddict
    if nitrosnipestatus == True:
        if codeRegex.search(message.content):
            code = codeRegex.search(message.content).group(2)
            start_time = time.time()
            async with httpx.AsyncClient() as client:
                result = await client.post(
                'https://discordapp.com/api/v6/entitlements/gift-codes/' + code + '/redeem',
                json={'channel_id': str(message.channel.id)},
                headers={'authorization': TOKEN, 'user-agent': 'Mozilla/5.0'})
                delay = (time.time() - start_time)
                if 'This gift has been redeemed already' in str(result.content):
                    print(Fore.YELLOW+f"We found a code but it was redeemed already ({code}, delay of {delay})")
                elif 'nitro' in str(result.content):
                    print(Fore.GREEN+f"[>] We found a code and claimed it! ({code}, delay of {delay})")
                elif 'Unknown Gift Code' in str(result.content):
                    print(Fore.RED+f"[>] We found a code but it was invalid ({code}, delay of {delay})")
    for key in commanddict:
        if message.content == key:
            await message.delete()
            await message.channel.send(commanddict[key])
    if donotdisturb == True:
        global reply
        if message.author != zzee.user:
            if not message.guild:
                await message.channel.send(reply)
    await zzee.process_commands(message)
zzee.run(__token__, zzee=False)