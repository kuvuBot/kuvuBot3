import importlib;
import sys;
import discord.ext.commands.bot as dbot;

__all__ = ['kiciusie']


def setup_all(bot: dbot, logger, lang):
    for module in __all__:
        bot.add_cog( (getattr(importlib.import_module('.'+module, 'commands'),module.capitalize()))(bot, logger, lang) )
    return bot