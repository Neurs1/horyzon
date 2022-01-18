from nextcord import Embed, Colour, ui, SelectOption, Interaction
from replit import db

global view, mess
view, mess = {}, {}

async def Author(ctx):
  await ctx.send(embed=Embed(title="Stupidly made by Neurs#5864", description="The code is quite dumb and slow, so... Don't ask about it :)\nProfile picture: Niko Oneshot (Video game)", colour=Colour.blue()).set_thumbnail(url = "https://cdn.discordapp.com/avatars/453468750650408961/af3b1463e615d2006f47f774da981127.png"))

class HelpOptions(ui.Select):
  def __init__(self):
    options = [
      SelectOption(label = "Play music", emoji = "🎶"),
      SelectOption(label = "Discord activities", emoji = "🎮"),
      SelectOption(label = "Bot & User info", emoji = "ℹ")
    ]
    super().__init__(placeholder = "Select a category", min_values = 1, max_values = 1, options=options)
  
  async def callback(self, interaction: Interaction):
    if self.values[0] == "Play music":
      await interaction.response.edit_message(embed = Embed(title="🎶 Play music", colour=Colour.blue()).add_field(name = f"``/play <url/query>``", value = "Type YouTube, SoundCloud URL or search for a YouTube video", inline = False).add_field(name = f"``/stop``", value = "Stop da music and clear the whole queue.", inline = True).add_field(name = f"``/skip``", value = "Skip queue to next position.", inline = True).add_field(name = f"``/pause``", value = "Pause the music.", inline = True).add_field(name = f"``/resume``", value = "Resume the music.", inline = True))

    if self.values[0] == "Discord activities":
      await interaction.response.edit_message(embed = Embed(title="🎮 Discord activities", colour=Colour.blue()).add_field(name = f"``/together``", value = "Select and launch Discord activities!"))
    
    if self.values[0] == "Bot & User info":
      await interaction.response.edit_message(embed = Embed(title="ℹ Bot & User info", colour=Colour.blue()).add_field(name = f"``/info``", value = "Get info of yourself or a member in your Discord guild.").add_field(name = f"``/mci``", value = "Get information about a name in Minecraft or check the availability of the name.").add_field(name = f"``/author``", value = "Info about author.").add_field(name = f"``/version``", value = "View current version of the bot and check for new features!"))

class HelpView(ui.View):
  def __init__(self):
    super().__init__()
    self.add_item(HelpOptions())

async def Help(ctx):
  global view, mess
  view[ctx.guild.id] = HelpView()
  mess[ctx.guild.id] = await ctx.send(embed = Embed(title = "Help menu", description = "Please select a category!", colour=Colour.blue()), view = view[ctx.guild.id])
  await view[ctx.guild.id].wait()


async def Version(ctx):
  await ctx.send(embed=Embed(title="Current version: 3.0", description="No new update since: 06:12 | 12/28/2021 (EDT)\n**What's new:**\n- Bug fixed.\n- Slash commands now available! Check it out using `/help`", colour=Colour.blue()))