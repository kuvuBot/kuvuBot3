import asyncio;
from discord.ext import commands;
import discord
import json
import xml.etree.ElementTree as ET
import aiohttp
from lang import Language

class Kiciusie:
    def __init__(self, bot:commands.Bot, logger, lang):
        self.bot:commands.Bot = bot
        self.logger = logger
        self.lang:Language = lang

    @commands.command(
        name="kiciusie",
        cog_name="Image Commands",
        description="Pokazuje słodkiego kotka.",
        pass_context=True,
        aliases=["cat", "kot", "koty", "cats"]
    )
    async def kiciusie(self, ctx):
        message:discord.Message = ctx.message;
        async with aiohttp.get('http://random.cat/meow') as req:
            if req.status != 200:
                await self.bot.send_message(message.channel, self.lang.key('warning', message.author.mention, self.lang.key('bad_response', req.status)))
            else:
                emb=discord.Embed()
                j = await req.json()
                emb.set_image(url=j['file'])
                emb.colour = discord.Colour.magenta()
                await self.bot.send_message(message.channel, '', embed=emb)