import discord
from discord import message
from discord.ext import commands
from discord.ext.commands import has_permissions, CheckFailure
import time
import platform
from discord.ext import tasks
import json,urllib.request
import random
import asyncio
import datetime
from itertools import cycle
import os
import datetime
import json
import itertools
from typing import Union
import traceback
import sys
from random import choice, randint
from typing import Optional
import a2s

from aiohttp import request
from discord import Member, Embed
from discord.ext.commands import Cog, BucketType
from discord.ext.commands import BadArgument
from discord.ext.commands import command, cooldown


# random shit for new python update
intents = discord.Intents.default()
intents.members = True



client = commands.Bot(command_prefix=['-'], case_insensitive=True, intents=intents)
client.remove_command('help')

class FetchedUser(commands.Converter):
        async def convert(self, ctx, argument):
                if not argument.isdigit():
                        raise commands.BadArgument('Not a valid user ID.')
                try:
                        return await ctx.bot.fetch_user(argument)
                except discord.NotFound:
                        raise commands.BadArgument('User not found.') from None
                except discord.HTTPException:
                        raise commands.BadArgument('An error occurred while fetching the user.') from None
                                                        
@client.event
async def on_ready():
        channel = client.get_channel(861159753145122816)
        await channel.send('Bot is being started.')
        global startTime
        startTime = time.time()
        activity = discord.Game(name="playazclub.xyz | -help")
        await client.change_presence(status=discord.Status.dnd, activity=activity)
        print("Commands Loading...")
        await asyncio.sleep(2)
        print("Commands Loaded!")
        print("Loading Cogs...")
        await asyncio.sleep(2)
        print(f"Main Cog has been loaded!")
        print("Fun Cog has been loaded!\n-----------")
        await channel.send('Bot is fully loaded.')




                  
#######################
# /  __ \|  ___|  __ \#
# | /  \/| |_  | |  \/#
# | |    |  _| | | __ #
# | \__/\| |   | |_\ \#
#  \____/\_|    \____/#
#######################               
                   
# Version of the Bot
chromeversion = 'Alpha'

# Bot Token
TOKEN = 'ODYxMTE4NTQ0MjgwMjg5Mjgw.YOFJIw.qEMLN64-HFGncDBVwZa898z_fFc'

# Autorole Config
autorole = 'Users'

#@commands.has_permissions(permissionhere=True)

#######################################
#|  ___| | | |  ___| \ | |_   _/  ___|#
#| |__ | | | | |__ |  \| | | | \ `--. #
#|  __|| | | |  __|| . ` | | |  `--. \#
#| |___\ \_/ / |___| |\  | | | /\__/ /#
#\____/ \___/\____/\_| \_/ \_/ \____/ #
#######################################       

@client.event
async def on_command_error(ctx, error):
        try: 
                if hasattr(ctx.command,'on_error'):
                        return
                else:
                        embed = discord.Embed(title=f'Error in {ctx.command}', description=f'`{ctx.command.qualified_name} {ctx.command.signature}`\n{error}', color=0xD8122F)
                        await ctx.send(embed=embed)
        except:
                embed = discord.Embed(title=f'Error in {ctx.command}', description=f'`{error}`', color=0xD8122F)
                await ctx.send(embed=embed)

@client.event
async def on_member_join(member):
        if autorole in str(discord.utils.get(member.guild.roles, name=autorole)):
                await member.add_roles(discord.utils.get(member.guild.roles, name=autorole))

                async def on_ready(self):
                        print('Logged on as', self.user)

# @client.event
# async def on_member_remove(member):
#         embed = discord.Embed(color=0x8912d8, description=f"We lost a member! We now only have {len(list(member.guild.members))} members.", )
#         embed.set_thumbnail(url=f"{member.avatar_url}")
#         embed.set_author(name=f"{member.name}", icon_url=f"{member.avatar_url}")
#         embed.set_footer(text=f"{member.guild}", icon_url=f"{member.guild.icon_url}")
#         embed.timestamp = datetime.datetime.utcnow()

#         channel = client.get_channel(id=752331400803385385)
#         await channel.send(embed=embed) 

#########################################################
#/  __ \  _  |  \/  ||  \/  | / _ \ | \ | |  _  \/  ___|#
#| /  \/ | | | .  . || .  . |/ /_\ \|  \| | | | |\ `--. #
#| |   | | | | |\/| || |\/| ||  _  || . ` | | | | `--. \#
#| \__/\ \_/ / |  | || |  | || | | || |\  | |/ / /\__/ /#
# \____/\___/\_|  |_/\_|  |_/\_| |_/\_| \_/___/  \____/ #
#########################################################


@client.command(pass_context=True)
async def giverole(ctx, user: discord.Member, role: discord.Role):
    await user.add_roles(role)

@client.command()
async def shutdown(ctx):
        perms = ctx.author.permissions_in(ctx.channel)
        if perms.administrator:
                channel = ctx.guild.get_channel(861159753145122816)
                await ctx.message.delete()
                await channel.send('Bot was forcibly shut down.')
                await client.logout()

@client.command()
async def players(ctx):
        try:
                output = []
                address = ("95.216.30.3", 27414)
                players = a2s.players(address)

                for player in players:
                        if player.name:
                                output.append(player.name)
                if len(output) >= 1:
                        ihatemylife = ", ".join(output)
                        numbercount = len(output)
                        content = discord.Embed(title=f"{numbercount} players currently online", description=ihatemylife, color=ctx.author.color, timestamp=ctx.message.created_at)
                        await ctx.send(embed=content)
                else:
                        content = discord.Embed(title="Players Online", description="There are currently no players online!", color=ctx.author.color, timestamp=ctx.message.created_at)
                        await ctx.send(embed=content)
        except:
                await ctx.reply("The server is currently offline.", mention_author=True)

@client.command()
async def ping(ctx):
    start = time.perf_counter()
    message = await ctx.send("Ping...")
    end = time.perf_counter()
    duration = (end - start) * 1000
    await message.edit(content='Pong! {:.2f}ms'.format(duration))

# @client.command()
# async def rules(ctx):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if perms.administrator:
#                 embed = discord.Embed(title="Community Information", description='', color=0x9c081e, url="https://steamcommunity.com/sharedfiles/filedetails/?id=2445060029")
#                 embed.add_field(name='**Useful Links:**', value='**Invite:** https://discord.chromeroleplay.com/\n**Forums:** https://chromeroleplay.com\n**Store:** https://chromeroleplay.com/donate\n**Steam Group:** https://steamcommunity.com/groups/chromeroleplay', inline=False)
#                 embed.add_field(name='**Servers:**', value='Chrome Roleplay - DarkRP\n`135.148.31.97`', inline=False)
#                 embed.add_field(name='**Discord Rules:**', value='**1.** Use common sense, \n**2.** Spamming is not allowed.\n**3.** Bypassing our chat filter is not allowed\n**4.** Harassment will not be tolerated.\n**5.** No NSFW pictures or videos.\n**6.** Do not disrespect at all.\n**7.** Links are prohibited.\n**8.** Promoting/advertising anything is not allowed under any circumstance.\n**9.** Derogatory speech is prohibited. Keep it in-character.\n**10.** Personal information (links, pictures, IPs, etc) are extremely prohibited. We will not tolerate doxxing.\n**11.** Threatening to harm another ones being is not allowed under any circumstance. This includes: DDoS threats, in-real-life threats, etc.\n**12.** A staff member has final say on all rule interpretations including those not explicitly stated in the rules.\n**13.** Follow the Discord TOS\n**14.** Cussing is allowed, however, do not use it with excess.\n**15.** Any threats or intent to harm other players in the community, or the server, will result in a permanent ban.', inline=False)
#                 embed.set_footer(text="5/23/2021", icon_url='')
#                 await ctx.send(embed=embed)

@client.command()
async def status(ctx):
        channel = ctx.channel
        data = urllib.request.urlopen("https://api.battlemetrics.com/servers/10662906").read()
        output = json.loads(data)
        embed = discord.Embed(title=output["data"]["attributes"]["name"], color=ctx.author.color)
        maxPlayers = output["data"]["attributes"]["maxPlayers"]
        players = output["data"]["attributes"]["players"]
        status = output["data"]["attributes"]["status"]
        password = output["data"]["attributes"]["details"]["password"]
        slash = "/"
        embed.add_field(name="Player Count", value=f"{players}{slash}{maxPlayers}", inline=True)
        embed.add_field(name="Gamemode", value=output["data"]["attributes"]["details"]["gameMode"], inline=True)
        embed.add_field(name="Status", value=f"{status}", inline=True)
        embed.add_field(name="Password", value=f"{password}", inline=True)
        embed.add_field(name="Map", value=output["data"]["attributes"]["details"]["map"], inline=True)
        embed.add_field(name="Join", value="steam://connect/95.216.30.3:27414" ,inline=True)
     #   embed.set_thumbnail(url="https://i.imgur.com/KWoh1kT.png")
        embed.set_footer(text="This information refreshes every 30 minutes")
        await channel.send(embed=embed)

# @client.command(pass_context=True)
# async def unban(ctx, user: int):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if perms.ban_members:
#                 member = await client.fetch_user(user)
#                 await ctx.guild.unban(member)
#                 content = discord.Embed(title="Unbanned", description=f'{member} was unbanned', color=0xD8122F)
#                 await ctx.send(embed=content)
#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command()
# async def coinflip(ctx):
#         choices = ['Heads', 'Tails']
#         rancoin = random.choice(choices)
#         content = discord.Embed(title=rancoin, description="", color=ctx.author.color)
#         content.set_footer(text=f"Requested by {ctx.author}")
#         await ctx.send(embed=content)

# @client.command(aliases=['8ball'])
# async def _8ball(ctx, *, question):
#   responses = [
#             "It is certain.",
#             "It is decidedly so.",
#             "Without a doubt.",
#             "Yes - definitely.",
#             "You may rely on it.",
#             "As I see it, yes.",
#             "Most likely.",
#             "Outlook good.",
#             "Yes.",
#             "Signs point to yes.",
#             "Reply hazy, try again.",
#             "Ask again later.",
#             "Better not tell you now.",
#             "Cannot predict now.",
#             "Concentrate and ask again.",
#             "Don't count on it.",
#             "My reply is no.",
#             "My sources say no.",
#             "Outlook not so good.",
#             "Very doubtful."]
#   content = discord.Embed(title="Answer", description=(f'\n *{random.choice(responses)}*'), color=ctx.author.color)
#   await ctx.send(embed=content)

# @client.command()
# async def mute(ctx, user: discord.Member):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if user.guild_permissions.manage_messages:
#                 content = discord.Embed(title="Error".format(client.user), description='I cannot mute this user. They are either an admin or moderator.', color=0xD8122F)
#                 await ctx.send(embed=content)
#         elif perms.manage_messages:
#                 await user.add_roles(discord.utils.get(ctx.message.guild.roles, name="Muted"))
#                 content = discord.Embed(title="Member Muted!", description="{0} has been muted permanently".format(user.mention), color=0xD8122F)
#                 await ctx.send(embed=content)
#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command()
# async def unmute(ctx, user: discord.Member):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if user.guild_permissions.manage_messages:
#                 content = discord.Embed(title="Error".format(client.user), description='I cannot unmute this user. They are either an admin or moderator.', color=0xD8122F)
#                 await ctx.send(embed=content)
#         elif perms.manage_roles:
#                 await user.remove_roles(discord.utils.get(ctx.message.guild.roles, name="Muted"))
#                 content = discord.Embed(title="Member Unmuted!", description="Unmuted: {0}".format(user.mention), color=0xD8122F)
#                 await ctx.send(embed=content)
#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command(pass_context = True , aliases=['purge', 'clean', 'delete'])
# async def clear(ctx, amount : int):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if perms.manage_messages:
#                 await ctx.channel.purge(limit=amount)
#                 if amount == 1:
#                         content = discord.Embed(title="Messages Deleted!", description=f"Removed {amount} message", color=0x00c42b)
#                 else:
#                         content = discord.Embed(title="Messages Deleted!", description=f"Removed {amount} messages", color=0x00c42b)
#                 msg = await ctx.send(embed=content)
#                 await asyncio.sleep(2)
#                 await msg.delete()
#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command()
# async def report(ctx, user, *, reason):
#         embed = discord.Embed(title='New Report!', description=f'Report by: {ctx.author.mention}\nUser Reported: *{user}*', color=ctx.author.color)
#         embed.add_field(name='Report Reason:', value=reason)
#         channel = ctx.guild.get_channel(843657865940041748)
#         msg = await channel.send(embed=embed)
	
# @client.command()
# async def kick(ctx, member : discord.Member, *, reason=None):
#         if member.guild_permissions.manage_messages:
#                 content = discord.Embed(title="Error".format(client.user), description='I cannot kick this user. They are either an admin or moderator.', color=0xD8122F)
#                 await ctx.send(embed=content)
#         elif member != ctx.author:
#                 perms = ctx.author.permissions_in(ctx.channel)
#                 if perms.kick_members:
#                         content = discord.Embed(title="Kicked!", description="**You have been kicked from {0}!**\nAdmin: *{1}*\nReason: *{2}*".format(ctx.message.guild, ctx.message.author, reason), timestamp=ctx.message.created_at, color=0xD8122F)
#                         await member.send(embed=content)
#                         await member.kick(reason=reason)
#                         content = discord.Embed(title="Member Kicked!", description="Member: {0}\nReason: {1}".format(member, reason), color=ctx.author.color)
#                         msg = await ctx.send(embed=content)
#                 else:
#                         content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                         await ctx.send(embed=content)
#         else:
#                 content = discord.Embed(title="Error".format(client.user), description='You cannot kick yourself.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command()
# async def ban(ctx, member : discord.Member, *, reason=None):
#         if member.guild_permissions.manage_messages:
#                 content = discord.Embed(title="Error".format(client.user), description='I cannot ban this user. They are either an admin or moderator.', color=0xD8122F)
#                 await ctx.send(embed=content)
#         elif member != ctx.author:
#                 perms = ctx.author.permissions_in(ctx.channel)
#                 if perms.ban_members:
#                         content = discord.Embed(title="Banned!", description="**You have been banned from {0}!**\nAdmin: *{1}*\nReason: *{2}*".format(ctx.message.guild, ctx.message.author, reason), timestamp=ctx.message.created_at, color=0xD8122F)
#                         await member.send(embed=content)
#                         await member.ban(reason=reason)
#                         content = discord.Embed(title="Member Banned!", description="Member: {0}\nReason: {1}".format(member, reason), color=ctx.author.color)
#                         msg = await ctx.send(embed=content)
#                 else:
#                         content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                         await ctx.send(embed=content)
#         else:
#                 content = discord.Embed(title="Error".format(client.user), description='You cannot ban yourself.', color=0xD8122F)
#                 await ctx.send(embed=content)

@client.group(name='help', invoke_without_command=True, case_insensitive=True)
async def help_cmd(ctx):
        embed = discord.Embed(
                color=ctx.author.color,
                title="Help",
                description="This is the main page for the help command. Please use `-help [group]` in order to see the commands"
        )
        
        embed.add_field(name="Command Groups", value="`Server`", inline=False)
        await ctx.send(embed=embed)

# @help_cmd.command(name='staff')
# async def whatever_subcommand(ctx):

#         perms = ctx.author.permissions_in(ctx.channel)
#         if perms.manage_messages:
#                 embed = discord.Embed(
#                 color=ctx.author.color,
#                 title="Help",
#                 description="All staff commands. Use `-[command]` to see how it's used and the args used")
                
#                 embed.add_field(name="Commands", value="`Ban`, `Unban`, `Kick`, `Mute`, `Unnmute`, `Poll`, `Clear`", inline=False)
#                 await ctx.send(embed=embed)

#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @help_cmd.command(name='fun')
# async def whatever_subcommand(ctx):
#         embed = discord.Embed(
#                 color=ctx.author.color,
#                 title="Help",
#                 description="All fun commands. Use `-[command]` to see how it's used and the args used"
#         )
        
#         embed.add_field(name="Commands", value="`Coinflip`, `8Ball`, `WhoIs`, `Avatar`, `Ping`, `Slap`, `Fact`", inline=False)
#         await ctx.send(embed=embed)

@help_cmd.command(name='server')
async def whatever_subcommand(ctx):
        embed = discord.Embed(
                color=ctx.author.color,
                title="Help",
                description="All server related commands. Use `-[command]` to see how it's used and the args used"
        )
        
        embed.add_field(name="Commands", value="`Players`, `Status`, `Ping`, `Stats`", inline=False)

        await ctx.send(embed=embed)

@client.command()
async def stats(ctx):
        serverCount = len(client.guilds)
        memberCount = sum([i.member_count for i in client.guilds])
        dpyVersion = discord.__version__

        embed = discord.Embed(title="Kai.PR".format(client.user), description='', color=ctx.author.color)
        uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))

        embed.add_field(name='Bot Version', value=chromeversion)
        embed.add_field(name='Discord Version', value=dpyVersion)
        embed.add_field(name='Total Servers', value=serverCount)
        embed.add_field(name='Total Members:', value=memberCount)
        embed.add_field(name='Bot Developers', value="<@282330894197325824>")
        embed.add_field(name='Uptime', value=uptime)
        
        embed.set_author(name='', icon_url=client.user.avatar_url)
        embed.set_footer(text=client.user, icon_url=client.user.avatar_url)

        await ctx.send(embed=embed)

# @client.command()
# async def poll(ctx,*,message):
#         perms = ctx.author.permissions_in(ctx.channel)
#         if perms.administrator:
#                 emb=discord.Embed(title="**Server Poll**", description=f"**{message}**", color=ctx.author.color)
#                 msg=await ctx.channel.send(embed=emb)
#                 await msg.add_reaction('<:agree:757957578599694456>')
#                 await msg.add_reaction('<:disagree:757957632546963556>')
#                 await ctx.send("@everyone")
#         else:
#                 content = discord.Embed(title="Insufficient Permissions".format(client.user), description='If you feel like this was an error, contact a server administrator.', color=0xD8122F)
#                 await ctx.send(embed=content)

# @client.command()
# async def avatar(ctx, *, user: Union[discord.Member, FetchedUser] = None):
#         """Shows a user's enlarged avatar (if possible)."""
#         embed = discord.Embed()
#         user = user or ctx.author
#         avatar = user.avatar_url_as(static_format='png')
#         embed.set_author(name=str(user), url=avatar)
#         embed.set_image(url=avatar)
#         await ctx.send(embed=embed)

# @client.command(aliases=['lookup'])
# async def whois(ctx, *, user: Union[discord.Member, FetchedUser] = None):
#         user = user or ctx.author
#         roles = [role for role in user.roles[1:]]
#         embed = discord.Embed(colour=user.color, timestamp=ctx.message.created_at)
#         embed.set_author(name=f"User Information For: {user}")
#         embed.set_thumbnail(url=user.avatar_url)
#         embed.set_footer(text=f"Requested By: {ctx.author}", icon_url=ctx.author.avatar_url)
#         embed.add_field(name="Display Name:", value=user.display_name)
#         embed.add_field(name="Created At:", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
#         embed.add_field(name="Joined At:", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"))
#         embed.add_field(name=f"Roles [{len(roles)}]", value=", ".join([role.mention for role in roles]))
#         embed.add_field(name="Highest Role:", value=user.top_role.mention)

#         await ctx.send(embed=embed)

# @client.command()
# async def content(ctx):
#         embed = discord.Embed(colour=ctx.author.color, timestamp=ctx.message.created_at)
#         embed.set_author(name="Content")
#         embed.set_thumbnail(url=ctx.author.avatar_url)
#         embed.set_footer(text=f"Requested By: {ctx.author}", icon_url=ctx.author.avatar_url)
#         content = discord.Embed(title="Banned!", description="Hi", timestamp=ctx.message.created_at, color=0xD8122F)
#         await client.send(embed=content)
#         #embed.add_field(name="Content Pack", url="https://steamcommunity.com/sharedfiles/filedetails/?id=2445060029")
#      #   await ctx.send(embed=embed)

# @client.command()
# async def checklines(ctx):
#         file = open("C:\\Users\\owenm\\Documents\\gmod\\ChromeRP\\bot\\main.py", "r")
#         num = 0
#         for i in file.readlines():
#                 num += 1
#         file.close()
#         embed = discord.Embed(title="", description="Amount of lines for the bot:\n**{0}**".format(str(num)), color=ctx.author.color)
#         embed.set_author(name='Chrome Roleplay', icon_url=client.user.avatar_url)
#         await ctx.send(embed=embed)

# @client.command()
# async def slap(ctx, member):
#         if member != ctx.author:
#                 print('nigger')
#         else:
#                 responses = [
#                         "back to rc3",
#                         "for no reason.",
#                         "into mikey's lap.",
#                         "to gm_construct.",
#                         "into the council's chamber.",
#                         "into light's lap.",
#                 ]
#                 await ctx.send(f"{ctx.author.mention} slapped {member} {random.choice(responses)}")

client.run(TOKEN)
