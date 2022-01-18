from __future__ import unicode_literals
from youtubesearchpython.__future__ import VideosSearch
from nest_asyncio import apply
from time import time
from nextcord import ui, Interaction, Embed, Colour, FFmpegPCMAudio, SelectOption
from asyncio import get_event_loop, wait, ALL_COMPLETED, sleep
from datetime import timedelta
from yt_dlp import YoutubeDL
from concurrent.futures import ThreadPoolExecutor

apply()
  

global vc, data, q, p, info, audio, title, channel, optio, view, play, stdout, ydl, loop, executor, fr2, fr, linkqueue, linklist, rurl, channel, FFMPEG_OPTIONS, ydl_opts

FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5','options': '-vn'}
ydl_opts = {'format': 'bestaudio/best', 'extractaudio': True,'audioformat': 'mp3', 'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s','restrictfilenames': True,'noplaylist': True,'nocheckcertificate': True,'ignoreerrors': False,'logtostderr': False,'quiet': True,'no_warnings': True,'default_search': 'auto','cachedir': False,'source_address': '0.0.0.0'}

vc, data, q, p, info, audio, title, optio, linkqueue, view, play, stdout, ydl, loop, executor, fr2, fr, linkqueue, linklist, rurl, channel={},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{},{}

class HelpOptions(ui.Select):
  def __init__(self, ctx, bot):
    options = [
      SelectOption(label = "Track 1", emoji = "🎶", description = data[ctx.guild.id]['result'][0]['title']),
      SelectOption(label = "Track 2", emoji = "🎶", description = data[ctx.guild.id]['result'][1]['title']),
      SelectOption(label = "Track 3", emoji = "🎶", description = data[ctx.guild.id]['result'][2]['title']),
      SelectOption(label = "Track 4", emoji = "🎶", description = data[ctx.guild.id]['result'][3]['title']),
      SelectOption(label = "Track 5", emoji = "🎶", description = data[ctx.guild.id]['result'][4]['title'])
    ]
    super().__init__(placeholder = "Select a track", min_values = 1, max_values = 1, options=options)
    self.ctx = ctx
    self.bot = bot

  async def callback(self, interaction: Interaction):
    if self.values[0] == "Track 1":
      try:
        linkqueue[self.ctx.guild.id].append("https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][0]['id'])
      except:
        linkqueue[self.ctx.guild.id] = ["https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][0]['id']]
        data[self.ctx.guild.id] = None
    if self.values[0] == "Track 2":
      try:
        linkqueue[self.ctx.guild.id].append("https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][1]['id'])
      except:
        linkqueue[self.ctx.guild.id] = ["https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][1]['id']]
        data[self.ctx.guild.id] = None
    if self.values[0] == "Track 3":
      try:
        linkqueue[self.ctx.guild.id].append("https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][2]['id'])
      except:
        linkqueue[self.ctx.guild.id] = ["https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][2]['id']]
        data[self.ctx.guild.id] = None
    if self.values[0] == "Track 4":
      try:
        linkqueue[self.ctx.guild.id].append("https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][3]['id'])
      except:
        linkqueue[self.ctx.guild.id] = ["https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][3]['id']]
        data[self.ctx.guild.id] = None
    if self.values[0] == "Track 5":
      try:
        linkqueue[self.ctx.guild.id].append("https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][4]['id'])
      except:
        linkqueue[self.ctx.guild.id] = ["https://www.youtube.com/watch?v="+data[self.ctx.guild.id]['result'][4]['id']]
        data[self.ctx.guild.id] = None
    try:
      vc[self.ctx.guild.id].is_playing()
    except:
      await interaction.response.edit_message(embed = Embed(title = "Processing request, please wait...", colour=Colour.blue()))
      self.bot.loop.create_task(queue(self.ctx, self.bot))
      return
    if vc[self.ctx.guild.id].is_playing() == True:
      if len(linkqueue[self.ctx.guild.id]) == 1:
        self.bot.loop.create_task(queue(self.ctx, self.bot))
      await interaction.response.edit_message(embed=Embed(title="Placed in queue", description=f"Current songs in position: {len(linkqueue[self.ctx.guild.id])}", colour=Colour.blue()))
    else:
      await interaction.response.edit_message(embed = Embed(description = "Processing request, please wait...", colour=Colour.blue()))
      self.bot.loop.create_task(queue(self.ctx, self.bot))

class HelpView(ui.View):
  def __init__(self, ctx, bot):
    super().__init__()
    self.add_item(HelpOptions(ctx, bot))

def getyt(ctx):
  global ydl_opts, ydl, info, linkqueue
  with YoutubeDL(ydl_opts) as ydl[ctx.guild.id]: info[ctx.guild.id] = ydl[ctx.guild.id].extract_info(linkqueue[ctx.guild.id][0],download=False)

async def agetyt(loop, executor, ctx):
  await wait(
    fs={
        loop.run_in_executor(executor, getyt, ctx),
    },
    return_when=ALL_COMPLETED
    )

async def quit(ctx):
  global channel, vc, linkqueue
  while vc[ctx.guild.id].is_playing():
    if len(channel[ctx.guild.id].members) == 1:
      await ctx.send(embed=Embed(description="All users have left the voice channel, stopping...", colour=Colour.blue()))
      try:
        vc[ctx.guild.id].stop()
        linkqueue[ctx.guild.id] = []
      except:
        pass
      break
    else:
      await sleep(1)

async def Player(ctx, bot):
  global channel, linkqueue, q, p, info, audio, title, vc, data, optio, view, loop, executor, fr2, fr, ydl_opts, FFMPEG_OPTIONS
  q[ctx.guild.id] = time()
  try:
    fr[ctx.guild.id] = time()
    data[ctx.guild.id] = ""
    loop[ctx.guild.id] = get_event_loop()
    executor[ctx.guild.id] = ThreadPoolExecutor(max_workers=2)
    loop[ctx.guild.id].run_until_complete(agetyt(loop[ctx.guild.id], executor[ctx.guild.id], ctx))
    audio[ctx.guild.id] = info[ctx.guild.id]['formats'][3]['url']
    title[ctx.guild.id] = info[ctx.guild.id]['title']
    fr2[ctx.guild.id] = time()
    print("process link needed: "+str(fr2[ctx.guild.id]-fr[ctx.guild.id]))
  except:
    server = ctx.message.guild.voice_client
    await server.disconnect()
    await ctx.send(embed=Embed(title="Error", description="No audio could be found for \""+linkqueue[ctx.guild.id][0]+"\"", colour=Colour.red()))
    return
  try:
    await vc[ctx.guild.id].disconnect()
    vc[ctx.guild.id] = await channel[ctx.guild.id].connect()
  except:
    vc[ctx.guild.id] = await channel[ctx.guild.id].connect()
  #-------------------------------------------------------------------------------------------------#

    #Run audio
      
  vc[ctx.guild.id].play(FFmpegPCMAudio(source=audio[ctx.guild.id],  **FFMPEG_OPTIONS))
  p[ctx.guild.id] = time()
    
  await ctx.send(embed=Embed(title="Now playing", description=f"**[{title[ctx.guild.id]}]({linkqueue[ctx.guild.id][0]})**\n`0:00:00 / {str(timedelta(seconds=int(info[ctx.guild.id]['duration'])))}`\n", colour=Colour.blue()).set_image(url=info[ctx.guild.id]['thumbnail']).set_footer(text = f"Time elapsed to handle the request: {str(round(p[ctx.guild.id] - q[ctx.guild.id], 3))}s"))
  linkqueue[ctx.guild.id].pop(0)
  bot.loop.create_task(quit(ctx))

async def queue(ctx, bot):
  global linkqueue, vc
  try:
    vc[ctx.guild.id].is_playing()
  except:
    await Player(ctx, bot)
  while len(linkqueue[ctx.guild.id]) != 0:
    if linkqueue[ctx.guild.id] == []:
      break
    if vc[ctx.guild.id].is_playing() == False and vc[ctx.guild.id].is_paused() == False:
      await Player(ctx, bot)
    await sleep(1)

async def Play(ctx, url, bot):
  global vc, data, optio, view, linkqueue
  try:
    channel[ctx.guild.id] = ctx.user.voice.channel
  except:
    await ctx.send(embed=Embed(title="Error", description="You must join a voice channel first!", colour=Colour.red()))
    return

  if "https://" not in url:
    try:
      data[ctx.guild.id] = await VideosSearch(url, limit = 5).next()
      print(data[ctx.guild.id])
      view[ctx.guild.id] = HelpView(ctx, bot)
      optio[ctx.guild.id] = await ctx.send(embed=Embed(title="Please select a track!", colour=Colour.blue()), view=view[ctx.guild.id])
      await view[ctx.guild.id].wait()
    except:
      await ctx.send(embed=Embed(title="Error", description="No result found! Have you checked your query?", colour=Colour.red()))
      return
  else:
    try:
      linkqueue[ctx.guild.id]
    except:
      linkqueue[ctx.guild.id] = []
    linkqueue[ctx.guild.id].append(url)
    try:
      vc[ctx.guild.id].is_playing()
    except:
      bot.loop.create_task(queue(ctx, bot))
      await ctx.send(embed = Embed(title = "Processing request, please wait...", colour=Colour.blue()))
      return
    if vc[ctx.guild.id].is_playing() == True:
      if len(linkqueue[ctx.guild.id]) == 1:
        bot.loop.create_task(queue(ctx, bot))
      await ctx.send(embed=Embed(title="Placed in queue", description=f"Current position: {len(linkqueue[ctx.guild.id])}", colour=Colour.blue()))
    else:
      await ctx.send(embed = Embed(title = "Processing request, please wait...", colour=Colour.blue()))
      bot.loop.create_task(queue(ctx, bot))
  

async def Stop(ctx):
  global vc, linkqueue, linklist
  try:
    vc[ctx.guild.id].stop()
    linkqueue[ctx.guild.id], linklist[ctx.guild.id], rurl[ctx.guild.id] = [], [], []
    await ctx.guild.voice_client.disconnect()
  except:
    await ctx.send(embed=Embed(title="Nothing to stop :L", colour=Colour.red()))
  else:
    await ctx.send(embed=Embed(title="Stopped!", colour=Colour.blue()))

async def Skip(ctx):
  global vc, linkqueue
  try:
    vc[ctx.guild.id].stop()
    await ctx.guild.voice_client.disconnect()
  except:
    await ctx.send(embed=Embed(title="Nothing to skip :L", colour=Colour.red()))
  else:
    await ctx.send(embed=Embed(title=f"Skipped! Current queue list: {len(linkqueue[ctx.guild.id])}", colour=Colour.blue()))

async def Pause(ctx):
  global vc
  try:
    if vc[ctx.guild.id].is_playing():
      vc[ctx.guild.id].pause()
      await ctx.send(embed=Embed(title="Paused!", colour=Colour.blue()))
    else:
      await ctx.send(embed=Embed(title="Already paused :L", colour=Colour.red()))
  except:
    await ctx.send(embed=Embed(title="Nothing to pause :L", colour=Colour.red()))

async def Resume(ctx):
  global vc
  try:
    if vc[ctx.guild.id].is_paused():
      vc[ctx.guild.id].resume()
      await ctx.send(embed=Embed(title="Resumed!", colour=Colour.blue()))
    else:
      await ctx.send(embed=Embed(title="Already resumed :L", colour=Colour.red()))
  except:
    await ctx.send(embed=Embed(title="Nothing to resume :L", colour=Colour.red()))