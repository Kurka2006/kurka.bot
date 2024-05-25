import discord
from discord.ext import commands
from discord import FFmpegPCMAudio


client = commands.Bot(command_prefix='!', intents=discord.Intents.all())


queues = {}

def check_queue(ctx, id):
    if queues[id]  != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)
    else:
        print("queue is empty")






@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle, activity=discord.Activity(type = discord.ActivityType.listening, name='Music'))
    print('Ready')
    print("------------------")
    
    
    


@client.command()
async def hello(ctx):
    await ctx.send("Hello, I am the Kurka Bot")


@client.command()
async def bye(ctx):
    await ctx.send("Good Bye")
    
    
@client.event
async def on_member_join(member):
    channel = client.get_channel(989150833012776962)
    await channel.send("hello zango")
    
@client.command(pass_context = True)  
async def join(ctx):
    if (ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        
    
    else:
        await ctx.send("You are not in a voice channel, you must be in a voice channel to run this command!")
        
@client.command(pass_context = True)
async def play(ctx, arg):              
     voice = ctx.guild.voice_client
     if (ctx.author.voice):
        source = FFmpegPCMAudio(arg)
        player = voice.play(source, after=lambda x=None: check_queue(ctx, ctx.message.guild.id)) 

    
    
    
@client.command(pass_context = True)
async def leave(ctx):
    if (ctx.voice_client):
        await ctx.guild.voice_client.disconnect()   
        await ctx.send("I left the voice channel")  
    else:
        await ctx.send("I am not in the voice channel")
                
@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Currently, no audio is playing.")
    
@client.command(pass_context = True)
async def resume(ctx):              
     voice = discord.utils.get(client.voice_clients, guild=ctx.guild)               
     if voice.is_paused():
         voice.resume()
     else:
        await ctx.send("at the moment, song isn't paused ")           
 
 
 
@client.command(pass_context = True)
async def stop(ctx):              
     voice = discord.utils.get(client.voice_clients, guild=ctx.guild) 
     voice.stop()             
 
 
@client.command(pass_context = True)
async def queue(ctx, arg):
    voice = ctx.guild.voice_client
    source = FFmpegPCMAudio(arg)
    
    guild_id = ctx.message.guild.id
   
    if guild_id in queues:
        queues[guild_id].append(source)
       
    else:
        queues[guild_id] = [source]
    
    await ctx.send('added to queue')   
    
@client.command(pass_context = True)
async def commands(ctx): 
    await ctx.send("!join, !leave, !queue, !play, !stop, !pause")   
    
client.run('MTIzMzg3NjI5NjM1MDgyNjU2Nw.GygiLN.CwPikZ2SJC4sJvyK9VmqV9L8zn6miRBWfQCfrQ')






