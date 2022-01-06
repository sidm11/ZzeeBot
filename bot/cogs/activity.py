import discord, requests, pyfiglet
from discord.ext import commands as zzee

class Activity(zzee.Cog):
    def __init__(self, zzee):
        self.zzee = zzee


    @zzee.command()
    async def streaming(self, ctx, *, message):
        await ctx.message.delete()
        stream = discord.Streaming(
            name = message
        )
        await self.zzee.change_presence(activity=stream)    

        
    @zzee.command()
    async def playing(self, ctx, *, message):
        await ctx.message.delete()
        game = discord.Game(
            name=message
        )
        await self.zzee.change_presence(activity=game)
    
    
    @zzee.command()
    async def listening(self, ctx, *, message):
        await ctx.message.delete()
        await self.zzee.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.listening, 
                name=message, 
            ))
           
            
    @zzee.command()
    async def watching(self, ctx, *, message):
        await ctx.message.delete()
        await self.zzee.change_presence(
            activity=discord.Activity(
                type=discord.ActivityType.watching, 
                name=message
            ))


    @zzee.command(aliases=["stopstreaming", "stopstatus", "stoplistening", "stopplaying", "stopwatching"])
    async def stopactivity(self, ctx):
        await ctx.message.delete()
        await self.zzee.change_presence(activity=None, status=discord.Status.dnd)


def setup(zzee):
    zzee.add_cog(Activity(zzee))