from nextcord import Embed, Colour, ui, Interaction, ButtonStyle
from asyncio import sleep
import random

global players, ww_vl, view, ready_count, is_playing, currenttime, kill, vote, days, killed, voted
players, ww_vl, view, ready_count, is_playing, currenttime, kill, vote, days, killed, voted = {}, {}, {}, {}, {}, {}, {}, {}, {}, {}, {}

async def Clear(ctx):
  try: del players[ctx.guild.id]
  except: pass
  try: del ww_vl[ctx.guild.id]
  except: pass
  try: del view[ctx.guild.id]
  except: pass
  try: del ready_count[ctx.guild.id]
  except: pass
  try: del is_playing[ctx.guild.id]
  except: pass
  try: del currenttime[ctx.guild.id]
  except: pass
  try: del kill[ctx.guild.id]
  except: pass
  try: del vote[ctx.guild.id]
  except: pass
  try: del days[ctx.guild.id]
  except: pass
  try: del killed[ctx.guild.id]
  except: pass
  try: del voted[ctx.guild.id]
  except: pass

async def MainGame(ctx):
  while True:
    ww = 0; vl = 0
    for i in players[ctx.guild.id].keys():
      if players[ctx.guild.id][i]["role"] == "WW":
        ww += 1
      else:
        vl += 1
    if ww > vl or ww == vl == 1:
      await ctx.send(embed = Embed(title = "WEREWOLVES WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    if ww == 0 and vl > 0:
      await ctx.send(embed = Embed(title = "VILLAGERS WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    for i in players[ctx.guild.id].keys():
      players[ctx.guild.id][i]["voted"] = False
    try:
      days[ctx.guild.id]
    except:
      days[ctx.guild.id] = 0
    currenttime[ctx.guild.id] = "NIGHT"
    await ctx.send(embed = Embed(title = f"DAY {days[ctx.guild.id]}", description = f"Night has fallen, the whole village in the woods went to sleep. Werewolves, you have 30 seconds to decide who is your victim..."))
    print("30")
    await sleep(30)
    print(0)
    if is_playing[ctx.guild.id] == False:
      break
    currenttime[ctx.guild.id] = "DAY"
    days[ctx.guild.id] += 1
    for i in players[ctx.guild.id].keys():
      players[ctx.guild.id][i]["voted"] = False
    ww = 0; vl = 0
    for i in players[ctx.guild.id].keys():
      if players[ctx.guild.id][i]["role"] == "WW":
        ww += 1
      else:
        vl += 1
    if ww > vl or ww == vl == 1:
      await ctx.send(embed = Embed(title = "WEREWOLVES WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    if ww == 0 and vl > 0:
      await ctx.send(embed = Embed(title = "VILLAGERS WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    try:
      kill[ctx.guild.id]
    except:
      await ctx.send(embed = Embed(title = f"DAY {days[ctx.guild.id]}", description = f"The sun has rised up. Nobody was hurt because Werewolves don't choose anyone.\nNext acitivity: Vote one player out of the game. Everyone, you have 120 seconds to discuss and cast your vote."))
    else:
      if len(kill[ctx.guild.id]) == 0:
        await ctx.send(embed = Embed(title = f"DAY {days[ctx.guild.id]}", description = f"The sun has rised up. Nobody was hurt because Werewolves don't choose anyone.\nNext acitivity: Vote one player out of the game. Everyone, you have 120 seconds to discuss and cast your vote."))
      else:
        print("process")
        killed[ctx.guild.id] = max(kill[ctx.guild.id], key=kill[ctx.guild.id].get)
        print("shet")
        try: del players[ctx.guild.id][killed[ctx.guild.id]]
        except: pass
        await ctx.send(embed = Embed(title = f"DAY {days[ctx.guild.id]}", description = f"The sun has rised up. But sadly, <@{killed[ctx.guild.id]}> has been killed yesterday.\nNext acitivity: Vote one player out of the game. Everyone, you have 120 seconds to discuss and cast your vote."))
        try: del killed[ctx.guild.id], kill[ctx.guild.id]
        except: pass
    if ww > vl or ww == vl == 1:
      await ctx.send(embed = Embed(title = "WEREWOLVES WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    if ww == 0 and vl > 0:
      await ctx.send(embed = Embed(title = "VILLAGERS WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    print(120)
    await sleep(120)
    print(0)
    if is_playing[ctx.guild.id] == False:
      break
    try:
      vote[ctx.guild.id]
    except:
      await ctx.send(embed = Embed(title = "VOTE RESULT", description = "Everybody love each other, they don't vote anybody out."))
      await sleep(2)
    else:
      if len(vote[ctx.guild.id]) == 0:
        await ctx.send(embed = Embed(title = "VOTE RESULT", description = "Everybody love each other, they don't vote anybody out."))
        await sleep(2)
      else:
        print("Process")
        voted[ctx.guild.id] = max(vote[ctx.guild.id], key=vote[ctx.guild.id].get)
        h = 0
        for i in vote[ctx.guild.id].keys():
          if vote[ctx.guild.id][voted[ctx.guild.id]] == vote[ctx.guild.id][i]:
            h += 1
        print(h)
        if h > 1:
          await ctx.send(embed = Embed(title = "VOTE RESULT", description = "Can't kick anyone out because more than two players have the same vote!"))
        else:
          await ctx.send(embed = Embed(title = "VOTE RESULT", description = f"<@{voted[ctx.guild.id]}> has been removed from the game..."))
          try: del players[ctx.guild.id][voted[ctx.guild.id]]
          except: pass
        try: del voted[ctx.guild.id], vote[ctx.guild.id]
        except: pass
    
    #HANDLE RULES IN GAME

    ww = 0; vl = 0
    for i in players[ctx.guild.id].keys():
      if players[ctx.guild.id][i]["role"] == "WW":
        ww += 1
      else:
        vl += 1
    if ww > vl or ww == vl == 1:
      await ctx.send(embed = Embed(title = "WEREWOLVES WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break
    if ww == 0 and vl > 0:
      await ctx.send(embed = Embed(title = "VILLAGERS WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
      is_playing[ctx.guild.id] = False
      await Clear(ctx)
      break


class StartButton(ui.View):
  def __init__(self, ctx, bot):
    super().__init__(timeout=None)
    self
    self.ctx = ctx
    self.bot = bot
  @ui.button(label="START", emoji="🚩", style=ButtonStyle.green)
  async def t1(self, button: ui.button, interaction: Interaction):
    try:
      players[self.ctx.guild.id][interaction.user.id]
    except:
      await interaction.send(embed = Embed(title = "You haven't join yet, run `/jww` to join in before it start!"), ephemeral = True)
    else:
      if players[self.ctx.guild.id][interaction.user.id]["ready"] == False:
        players[self.ctx.guild.id][interaction.user.id]["ready"] = True
        try:
          ready_count[self.ctx.guild.id] += 1
        except:
          ready_count[self.ctx.guild.id] = 1
        if ready_count[self.ctx.guild.id] == len(players[self.ctx.guild.id]):
          is_playing[self.ctx.guild.id] = True
          ready_count[self.ctx.guild.id] = 0
          vl = []
          for i in players[self.ctx.guild.id].keys():
            vl.append(i)
          ww = random.choices(vl, k = ww_vl[self.ctx.guild.id][0])
          for i in ww:
            dm = self.bot.get_user(i)
            players[self.ctx.guild.id][i]["role"] = "WW"
            await dm.send(embed = Embed(title = "YOU'RE WEREWOLF", description = "Every night, you could kill one person.\nUse `/kill <player>` to choose your victim. YOU COULD ONLY CHOOSE ONCE, YOU CANNOT CHANGE YOUR VICTIM!"))
            vl.remove(i)
          for i in vl:
            players[self.ctx.guild.id][i]["role"] = "VL"
            dm = self.bot.get_user(i)
            await dm.send(embed = Embed(title = "YOU'RE VILLAGER", description = "Every day, you could vote to kill one person, discuss with others to vote one out.\nUse `/vote <player>` to cast your vote."))
          await interaction.send(content = "You have 20 seconds to see your role in DM")
          await sleep(20)
          if is_playing[self.ctx.guild.id] == True:
            self.bot.loop.create_task(MainGame(self.ctx))
        else:
          await interaction.send(embed = Embed(title = f"Players ready: {ready_count[self.ctx.guild.id]}/{len(players[self.ctx.guild.id])}"))
      else:
        await interaction.send(embed = Embed(title = f"You've already voted!"), ephemeral = True)

async def Kill(ctx, player):
  try:
    try:
      players[ctx.guild.id][ctx.user.id]
    except:
      await ctx.send(embed = Embed(title = "You can't use this command!"), ephemeral = True)
      return
    try:
      players[ctx.guild.id][player.id]
    except:
      await ctx.send(embed = Embed(title = f"You can't use this command on {player.name}!"), ephemeral = True)
      return
    if is_playing[ctx.guild.id] == True and currenttime[ctx.guild.id] == "NIGHT" and players[ctx.guild.id][ctx.user.id]["role"] == "WW" and players[ctx.guild.id][ctx.user.id]["voted"] == False:
      if players[ctx.guild.id][player.id]["role"] == "VL":
        players[ctx.guild.id][ctx.user.id]["voted"] = True
        try:
          kill[ctx.guild.id][player.id]
        except:
          try:
            kill[ctx.guild.id][player.id] = 1
          except:
            kill[ctx.guild.id] = {}
            kill[ctx.guild.id][player.id] = 1
        else:
          kill[ctx.guild.id][player.id] += 1
        await ctx.send(embed = Embed(description = f"You've chosen {player}"), ephemeral = True)
      else:
        await ctx.send(embed = Embed(description = f"{player} is a Werewolf, pick another person!"), ephemeral = True)
    else:
      await ctx.send(embed = Embed(title = f"You can't use this command!"), ephemeral = True)
  except:
    await ctx.send(embed = Embed(title = f"You can't use this command!"), ephemeral = True)

async def Vote(ctx, player):
  try:
    try:
      players[ctx.guild.id][ctx.user.id]
    except:
      await ctx.send(embed = Embed(title = f"You can't use this command!"), ephemeral = True)
      return
    try:
      players[ctx.guild.id][player.id]
    except:
      await ctx.send(embed = Embed(title = f"You can't use this command on {player.name}!"), ephemeral = True)
      return
    if is_playing[ctx.guild.id] == True and currenttime[ctx.guild.id] == "DAY" and players[ctx.guild.id][ctx.user.id]["voted"] == False:
      players[ctx.guild.id][ctx.user.id]["voted"] = True
      try:
        vote[ctx.guild.id][player.id]
      except:
        try:
          vote[ctx.guild.id][player.id] = 1
        except:
          vote[ctx.guild.id] = {}
          vote[ctx.guild.id][player.id] = 1
      await ctx.send(embed = Embed(description = f"<@{ctx.user.id}> voted {player.mention}"))
    else:
      await ctx.send(embed = Embed(title = f"You can't use this command!"), ephemeral = True)
  except:
    await ctx.send(embed = Embed(title = f"You can't use this command!"), ephemeral = True)

async def LeaveWW(ctx):
  try:
    if is_playing[ctx.guild.id] == False:
      players[ctx.guild.id][ctx.user.id]
    if is_playing[ctx.guild.id] == True:
      try: del players[ctx.guild.id][ctx.user.id]
      except: pass
      await ctx.send(embed = Embed(title = f"{ctx.user} left the game!"))
      ww = 0; vl = 0
      for i in players[ctx.guild.id].keys():
        if players[ctx.guild.id][i]["role"] == "WW":
          ww += 1
        else:
          vl += 1
      if ww > vl or ww == vl == 1:
        await ctx.send(embed = Embed(title = "WEREWOLVES WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
        is_playing[ctx.guild.id] = False
        await Clear(ctx)
      if ww == 0 and vl > 0:
        await ctx.send(embed = Embed(title = "VILLAGERS WINS!", description = f"Number of Werewolves: {ww}\nNumber of villager: {vl}"))
        is_playing[ctx.guild.id] = False
        await Clear(ctx)
    else:
      try: del players[ctx.guild.id][ctx.user.id]
      except: pass
      ww_vl[ctx.guild.id] = [round(len(players[ctx.guild.id])/3), round(len(players[ctx.guild.id]) - (len(players[ctx.guild.id])/3))]
      await ctx.send(embed = Embed(title = f"{ctx.user} left the game!", description = f"Number of players waiting: {len(players[ctx.guild.id])}\nNumber of Were Wolfs: {ww_vl[ctx.guild.id][0]}\nNumber of Villagers: {ww_vl[ctx.guild.id][1]}"))
  except:
    await ctx.send(embed = Embed(title = "You haven't join yet!"), ephemeral = True)
    

async def JoinWereWolf(ctx, bot):
  try:
    is_playing[ctx.guild.id]
  except:
    is_playing[ctx.guild.id] = False
  if is_playing[ctx.guild.id] == False:
    try:
      players[ctx.guild.id]
    except:
      players[ctx.guild.id] = {
        ctx.user.id: {
          "ready": False,
          "role": None,
          "voted": False
        }
      }
      ww_vl[ctx.guild.id] = [round(len(players[ctx.guild.id])/3), round(len(players[ctx.guild.id]) - (len(players[ctx.guild.id])/3))]
      await ctx.send(embed = Embed(title = f"{ctx.user} Joined the game!", description = f"Number of players waiting: {len(players[ctx.guild.id])}\nNumber of Were Wolfs: {ww_vl[ctx.guild.id][0]}\nNumber of Villagers: {ww_vl[ctx.guild.id][1]}", colour = Colour.blue()))
    else:
      if ctx.user.id not in players[ctx.guild.id]:
        players[ctx.guild.id].update({ctx.user.id: {"ready": False, "role": None, "voted": False}})
        ww_vl[ctx.guild.id] = [round(len(players[ctx.guild.id])/3), round(len(players[ctx.guild.id]) - (len(players[ctx.guild.id])/3))]
        if len(players[ctx.guild.id]) > 1:
          view[ctx.guild.id] = StartButton(ctx, bot)
          await ctx.send(embed = Embed(title = f"{ctx.user} Joined the game!", description = f"Number of players waiting: {len(players[ctx.guild.id])}\nNumber of Were Wolfs: {ww_vl[ctx.guild.id][0]}\nNumber of Villagers: {ww_vl[ctx.guild.id][1]}\nMinimum players reached! Press `🚩 START` to receice your role and join in the game!", colour = Colour.blue()), view = view[ctx.guild.id])
        else:
          await ctx.send(embed = Embed(title = f"{ctx.user} Joined the game!", description = f"Number of players waiting: {len(players[ctx.guild.id])}\nNumber of Were Wolfs: {ww_vl[ctx.guild.id][0]}\nNumber of Villagers: {ww_vl[ctx.guild.id][1]}", colour = Colour.blue()))
        
      else:
        await ctx.send(embed = Embed(title = "You've already joined!", description = f"Number of players waiting: {len(players[ctx.guild.id])}\nNumber of Were Wolfs: {ww_vl[ctx.guild.id][0]}\nNumber of Villagers: {ww_vl[ctx.guild.id][1]}", colour = Colour.blue()), ephemeral = True)
  else:
    await ctx.send(embed = Embed(title = "There is currently a game in process!", description = "Wait until the game is finished, you could join them!", colour = Colour.blue()), ephemeral = True)