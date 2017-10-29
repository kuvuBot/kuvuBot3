import asyncio
import aiohttp
import json

class Language:
    def __init__(self, locale:str, **kwargs):
        self.locale = locale
        if kwargs.get('url') is not None:
            r = aiohttp.get(kwargs.get('url'))
            if r.status == 200:
                j = r.json()
                self.dictionary = j
        if kwargs.get('local') is not None:
            stream = open(kwargs.get('local'), mode="r", encoding="utf-8")
            self.dictionary = json.load(stream)
            stream.close()

    def key(self, key:str, *kwargs):
        val:str = self.dictionary.get(key)
        if "{}" in val and kwargs is not None:
            val = u"{}".format(val.format(*kwargs))
        return val
