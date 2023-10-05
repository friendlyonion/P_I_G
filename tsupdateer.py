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

try:
    data = requests.get('https://api.earthmc.net/v1/aurora/towns/')
    data = data.json()
    for town in data['allTowns']:
        data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
        data2 = data2.json()
        path = 'townSpawns/{town}.csv'.format(town = 'towns')
        with open(path, 'w') as d:
            writer = csv.writer(d)
            rows = [data2['spawn']['x'], data2['spawn']['z']]
            writer.writerow(rows)
            # close the file
            d.close()
        time.sleep(0.5)
except:
    pass