
from dataclasses import dataclass
from re import L
from discord.ext import commands
from discord.ext.commands import Bot
import discord
#import geopandas as gpd
#from geopandas import GeoDataFrame
import os
import time
import collections
import platform
import asyncio
import datetime
from csv import reader
import requests
from discord.ext import tasks
from selenium.webdriver.chrome.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import aiofiles
import csv
import json
import jsondiff as jd
from jsondiff import diff

bot = commands.Bot(command_prefix = '&', intents = discord.Intents.all())

@bot.event
async def on_ready():
    guild = bot.get_guild(966171948520464444)
    listt = []
    for r in guild.roles:
        role = guild.get_role(r.id)  # get the role
        town = str(role.name).replace(' ', '_')
        data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
        if data2.status_code == 200:
            data2 = data2.json()
            print(role.name)
            print('residents', data2['stats']['numResidents'])
            print('members on discord', len(role.members))
            print(" ")

    #print(listt)
    #for role in listt:





bot.run('NzM5NDcyOTQ4ODIxMzYwNzYx.GazEUH.XXOTlLhXivl901Oy4vIrGrvDTT0W-eM8g69cQQ')
