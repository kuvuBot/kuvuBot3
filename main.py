#-*- coding: utf-8 -*-
import asyncio;
import discord;
import discord.ext.commands as dec
import commands;
import yaml;
from lang import Language
from logger import Logger

bot = dec.Bot(command_prefix=".")

@bot.event
async def on_message(message):
    await bot.process_commands(message)

@bot.event
async def on_ready():
    print('Logged in as: '+bot.user.name)

configstream = open('./cache/config.yml')
config = yaml.load(configstream)
configstream.close()

lang = Language('', local=config['langfile'])
logger = Logger('log.txt')
bot = commands.setup_all(bot, logger, lang)
bot.run(config['token'])
