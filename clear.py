from discord.ext import commands

client = commands.Bot(command_prefix='-')

@client.command(name='clear', help='this command will clear msgs')
async def clear(ctx, amount = 18):
    await ctx.channel.purge(limit=amount)
   
    
client.run('OTMyNjg3MTczNDE5OTU0MjI2.YeWmng.A83I-NQMT7evqi6D5vkx6-He9Vs')