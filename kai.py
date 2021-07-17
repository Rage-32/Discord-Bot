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
        embed.set_footer(text="This information refreshes every 30 minutes")
        await channel.send(embed=embed)

@client.group(name='help', invoke_without_command=True, case_insensitive=True)
async def help_cmd(ctx):
        embed = discord.Embed(
                color=ctx.author.color,
                title="Help",
                description="This is the main page for the help command. Please use `-help [group]` in order to see the commands"
        )
        
        embed.add_field(name="Command Groups", value="`Server`", inline=False)
        await ctx.send(embed=embed)

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

client.run(TOKEN)
