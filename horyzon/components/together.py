from nextcord import ui, ButtonStyle, Interaction, Embed, Colour

global link, view, optio
link, view, optio = {},{},{}

class slgame(ui.View):
  def __init__(self):
    super().__init__()
    self.value = None
  
  @ui.button(label="▶ Watch Together (YouTube)", style=ButtonStyle.green)
  async def t1(self, button: ui.button, interaction: Interaction):
    self.value = 1
    self.stop()
  

  @ui.button(label="🃏 Poker Night", style=ButtonStyle.green)
  async def t2(self, button: ui.button, interaction: Interaction):
    self.value = 2
    self.stop()


  @ui.button(label="♟ Chess in the Park", style=ButtonStyle.green)
  async def t3(self, button: ui.button, interaction: Interaction):
    self.value = 3
    self.stop()


  @ui.button(label="🔫 Betrayal.io", style=ButtonStyle.green)
  async def t4(self, button: ui.button, interaction: Interaction):
    self.value = 4
    self.stop()


  @ui.button(label="🎣 Fishington.io", style=ButtonStyle.green)
  async def t5(self, button: ui.button, interaction: Interaction):
    self.value = 5
    self.stop()


  @ui.button(label="🔠 Letter Tile", style=ButtonStyle.green)
  async def t6(self, button: ui.button, interaction: Interaction):
    self.value = 6
    self.stop()


  @ui.button(label="🆎 Word Snack", style=ButtonStyle.green)
  async def t7(self, button: ui.button, interaction: Interaction):
    self.value = 7
    self.stop()


  @ui.button(label="🎨 Doodle Crew", style=ButtonStyle.green)
  async def t8(self, button: ui.button, interaction: Interaction):
    self.value = 8
    self.stop()


  @ui.button(label="🧙‍♂️ SpellCast", style=ButtonStyle.green)
  async def t9(self, button: ui.button, interaction: Interaction):
    self.value = 9
    self.stop()


  @ui.button(label="Cancel", style=ButtonStyle.red)
  async def cancel(self, button: ui.button, interaction: Interaction):
    self.value = False
    self.stop()

async def Together(ctx, bot):
  global link, optio
  try:
    ctx.user.voice.channel.id
  except:
    await ctx.send(embed=Embed(title="Error", description="You must join a voice channel first!", colour=Colour.red()))
    return
  
  view[ctx.guild.id] = slgame()
  optio[ctx.guild.id] = await ctx.send(embed=Embed(title="Discord Together", description="Choose an activity and start playing!", colour=Colour.blue()), view=view[ctx.guild.id])
    
  await view[ctx.guild.id].wait()
  if view[ctx.guild.id].value == 1:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'youtube')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Youtube Together activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 2:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'poker')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Poker Night activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 3:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'chess')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Chess in the Park activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 4:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'betrayal')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Betrayal.io activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 5:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'fishing')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Fishington.io activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 6:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'letter-tile')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Letter Tile activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 7:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'word-snack')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Word Snack activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 8:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'doodle-crew')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open Doodle Crew activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))

  if view[ctx.guild.id].value == 9:
    #await optio[ctx.guild.id].delete()
    link[ctx.guild.id] = await bot.togetherControl.create_link(ctx.user.voice.channel.id, 'spellcast')
    await ctx.send(embed=Embed(title="Activity created!", description="Activity requested by \""+ctx.user.name+"\". Click [HERE]("+str(link[ctx.guild.id])+") to open SpellCast activity for voice channel \""+ctx.user.voice.channel.name+"\"!", colour=Colour.blue()))
  
  if view[ctx.guild.id].value == False:
    #await optio[ctx.guild.id].delete()
    pass
  return