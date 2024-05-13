if __name__ == '__main__':  
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
    from discord.ext import commands

    intents = discord.Intents.default()
    intents.typing = False
    intents.presences = False
    intents.members = True

    bot = discord.Bot(intents = intents)

    @bot.event
    async def on_ready():
        #PUAV.start()
        ftchecker.start()
        #onlinePlayerChecker.start()
        #checkChanges.start()
        #calcGDG.start()
    
    @bot.event
    async def on_member_join(member):
        if member.guild.id == 1111152465367289988:
            channel = bot.get_channel(1115803316060950631)
            await channel.send(f'Welcome {member.name} to the server! Please send your username and town name in https://discord.com/channels/1111152465367289988/1130261392465862676. Then read https://discord.com/channels/1111152465367289988/1132430977810042900 .')

    hunters = ['417squezpvp', 'god0', 'slyprince', 'OmeiBey', '_thepotatoman_', 'Knifery', 'ozzyniner', 'karrw', 'Mirkovic64', 'By____________Un', 'Mirkovic64', 'Crowishere', 'daedalus','DEMON_lodos', 'Emreyeten','BobkaKZ', 'Erwxn1337', 'Batu8747', 'WestoverWill12','TheBlazeMan69', 'EgirlSeethan','Coolman59999','Frede','kasana1919810','Jayden7566','Chengwen07','Gazoobas','RRYCER8746','kasana2007', 'DubsrVSF','Alzxdnr','kasana2003', 'AmethystPluto', 'DRX_Kingen', 'rainbowguy77','ManofWarfare']
    found_players = []
    pcounter = 0
    @tasks.loop(minutes=2)
    async def PUAV():
        try:
            global pcounter
            global found_players
            print('searching for incoming targets...')
            channel = bot.get_channel(1101345276691746866)
            data = getData()
            print('sorting data')
            #check if player is within range of Cascadia
            await asyncio.sleep(0)
            for b in data:
                    if (-24344<b['x']<-19664) and (-11000<b['z']<-7548):
                        time.sleep(1)
                        data2 = requests.get(('https://api.earthmc.net/v1/aurora/residents/{ign}').format(ign=b['name']))
                        data2 = data2.json()
                        if data2['affiliation']['nation']!= 'No Nation' and data2['affiliation']['nation']!= 'Cascadia' and data2['affiliation']['nation']!='Alberta' and data2['affiliation']['nation']!='Washington' and data2['affiliation']['nation']!='Oregon' and 'nation' in data2['affiliation']:
                                print(b['x'], b['z'], data2['affiliation']['nation'], data2['strings']['username'])
                                #print('does not equal no nation')
                                #if they are not in Cascadia, Alberta, WAshington, or Oregon
                                #if b['nation']!='Cascadia' and b['nation']!='Alberta' and b['nation']!='Washington' and b['nation']!='Oregon' and b['nation']!='California' and b['nation']!='Colorado' and b['nation']!='Yukon' and b['nation']!='Russian_Alaska' and b['nation']!='Alaska' and b['nation']!='Far_North'and b['nation']!='Arizona' and b['nation']!='Saskatchewan':
                                    #if they have not already been found in the past 9 mins
                                if b['name'] not in found_players:
                                    print('Not on found players')
                                    closestcoord = 10000
                                    #for filename in os.listdir('townSpawns/'):
                                    #    town = filename
                                    #    with open('townSpawns/'+filename, 'r') as read_obj:
                                    #    # pass the file object to reader() to get the reader object
                                    #        csv_reader = reader(read_obj)
                                    #    # Iterate over each row in the csv using reader object
                                    #        for row in csv_reader:
                                    #            print(row)
                                    #            temp = list(row)
                                    #            x = float(temp[0])
                                    #            z = float(temp[1])
                                    #            await asyncio.sleep(0)
                                    #            tcoords = town
                                    #            xcoord = abs(x-float(b['x']))
                                    #            zcoord = abs(z-float(b['z']))
                                    #            combcoord = xcoord +zcoord
                                    #            if combcoord<closestcoord:
                                    #                    closestcoord = combcoord
                                    #                    closesttown = town[:-4]
                                    #                    closestz = b['z']
                                    #                    closestx = b['x']
                                    #print(closesttown)
                                    #check if known hunter
                                    knownHunter = knownHunters(b['name'])
                                    channel = bot.get_channel(1101345276691746866)
                                    closesttown = 'broken temp'
                                    #generate map link to where player is
                                    maplink = 'https://earthmc.net/map/aurora/?worldname=earth&mapname=flat&zoom=5&x='+str(b['x'])+'&y=64&z='+str(b['z'])
                                    #build embed and send it
                                    print(closesttown, b['x'], b['z'], b['name'], maplink, knownHunter, data2['affiliation']['nation'])
                                    embed = await buildEmbed(closesttown, b['x'], b['z'], b['name'], maplink, knownHunter, data2['affiliation']['nation'])
                                    await channel.send(embed=embed)
                                    #add player to found list
                                    found_players.append(b['name'])
    
                        #else:
                        #        if b['name'] not in found_players:
                        #            #check if known hunter
                        #            knownHunter = knownHunters(b['name'])   
                        #            channel = bot.get_channel(1101345276691746866)
                        #            #generate map link to where player is
                        #            #maplink = 'https://earthmc.net/map/aurora/?worldname=earth&mapname=flat&zoom=5&x='+str(closestx)+'&y=64&z='+str(closestz)
                        #            maplink = 'WIP'
                        #            #build embed and send it
                        #            embed = await buildEmbed(closesttown, b['x'], b['z'], b['name'], maplink, knownHunter, data2['affiliation']['nation'])
                        #            await channel.send(embed=embed)
                        #            #add player to found list
                        #            found_players.append(b['name'])
                    else:
                        pass
            pcounter +=1
            if pcounter%9 == 0:
                found_players.clear()
        except:
            print('Fail')
        print(pcounter)
    @tasks.loop(minutes=7200)
    async def ftchecker():
        try:
            await asyncio.sleep(0)
            data = requests.get('https://api.earthmc.net/v1/aurora/nations/Cascadia')
            data = data.json()
            towns = list(data['towns'])
            for town in towns:
                print(town)
                data2 = getTownsMayor(town)
                ign = data2['strings']['mayor']
                print(ign)
                if findLastOnline(ign) == True:
                    print('oof1')
                    channel = bot.get_channel(1112446714826207282)
                    await channel.send(ign)
                    await channel.send(town)

                else:
                    addToList(ign)
                time.sleep(1)
        except:
            pass
    @tasks.loop(minutes=1)
    async def onlinePlayerChecker():
        try:
            await asyncio.sleep(0)
            data = requests.get('https://emctoolkit.vercel.app/api/aurora/onlineplayers')
            data = data.json()
            for player in data:
                path = 'playersLoginData/{name}.csv'.format(name = player['name'])
                #check if player name has a file. If not create a file. If it does log that the player is online at current time.
                f = open(path, 'a')

                # create the csv writer
                writer = csv.writer(f)

                # write a row to the csv file
                now = datetime.datetime.now()
                hour = [str(now.hour)]
                writer.writerow(hour)

                # close the file
                f.close()

        except:
            pass
    @tasks.loop(minutes=5000)
    async def townSpawnUpdater():
        try:
            await asyncio.sleep(0)
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

    @bot.slash_command(name="conline") 
    async def conline(ctx, arg):
        await ctx.respond('Generating...')
        times = []
        path = 'playersLoginData/{arg}.csv'.format(arg = arg)
        if os.path.exists(path) == True:
            with open(path, 'r') as read_objj:
            # pass the file object to reader() to get the reader object
                csv_reader = reader(read_objj)
            # Iterate over each row in the csv using reader object
                for row in csv_reader:
                    times.append(str(row))
            cnt = collections.Counter()
            for word in times:
                cnt[word] += 1
            print(cnt)
            embed = await buildCounterEmbed(cnt, arg)
            await ctx.send(embed = embed)
    
    @bot.slash_command(name="gdp") 
    async def gdp(ctx, arg):
        try:
            await ctx.respond('Finding gdp of ' + arg)
            data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = arg))
            data = data.json()
            gdp = 0
            gdp +=data['stats']['balance']
            for x in data['residents']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/residents/'+x)
                data2 = data2.json()
                gdp +=int(data2['stats']['balance'])
                time.sleep(0.1)
            for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                gdp +=int(data2['stats']['balance'])
                time.sleep(0.1)
            embed = await buildEmbedGdp(str(gdp), arg, 'Nation')
            await ctx.send(embed=embed)
        except:
            pass
    
    @tasks.loop(minutes=1440)
    async def calcGDG():
        print('Starting daily report...')
        casc = gdpp('Cascadia')
        await asyncio.sleep(0)
        vinland = gdpp('Laurentia')
        await asyncio.sleep(0)
        bc = gdpp('British_Columbia')
        await asyncio.sleep(0)

        rmf = gdpp('Rocky_Mountains')
        await asyncio.sleep(0)

        jefferson = gdpp('Jefferson')
        embed = await buildEmbedDailyReportGDP(casc, vinland, bc, rmf, jefferson)
        channel = bot.get_channel(1132700618461556757)
        await channel.send(embed=embed)

    #town gdg calc
    @bot.slash_command(name="tgdp") 
    async def tgdp(ctx, arg):
        if "-" in arg:
            arg = arg.replace("-", "_")
        try:
            await ctx.respond('Finding gdp of ' + arg)
            data = requests.get('https://api.earthmc.net/v1/aurora/towns/{town}'.format(town = arg))
            data = data.json()
            gdp = 0
            gdp +=data['stats']['balance']
            for x in data['residents']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/residents/'+x)
                data2 = data2.json()
                gdp +=int(data2['stats']['balance'])
                time.sleep(0.1)
            embed = await buildEmbedGdp(str(gdp), arg, 'Town')
            await ctx.send(embed=embed)
        except:
            pass
        
    @bot.command() 
    async def fnation(ctx):
        try:
            data = requests.get('https://api.earthmc.net/v1/aurora/towns')
            data = data.json()
            for town in data['allTowns']:
                data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
                data2 = data2.json()
                if data2['stats']['numResidents'] == 1 and data2['status']['isCapital'] and data2['status']['isOpen'] == True and findLastOnline(data2['strings']['mayor']) == True:
                    with open('tlistcheck.txt', 'a+') as f:
                        text = f.readlines()
                        if town in text:
                            pass
                        else:
                            print(town)
                            await ctx.send(town)
                            f.write(town+'\n')
                time.sleep(0.5)
        except:
            pass
    @tasks.loop(minutes=60)
    async def checkChanges():
        print('Running town changed check...')
        #Cascadia
        nation = 'Cascadia'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1125963338543796305)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)
        #British Columbia
        nation = 'British_Columbia'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1132718491573702727)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)

        #Rocky Mountains
        nation = 'Rocky_mountains'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1132718325684785162)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)
        #Laurentia
        nation = 'Laurentia'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1132718779995013232)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)
        #Yukon
        nation = 'Yukon'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1135631485232218122)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)
        #Jefferson
        nation = 'Jefferson'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                if diff(loaded_data2, loaded_data3) == {}:
                    pass
                else:

                    channel = bot.get_channel(1132718574998401075)
                    difference = diff(loaded_data2, loaded_data3)
                    results = differenceOrganizer(difference, loaded_data2, loaded_data3)
                    print(results)
                    if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                        print('no notable changes')
                    else:
                        embed = await buildEmbedFileNation(results, x)
                        await channel.send(embed=embed)
                        ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                        with open(ffn, 'w', encoding='utf-8') as l:
                            json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
                time.sleep(1)

    @tasks.loop(minutes=60)
    async def checkChangesNation():
        print('Running town changed check...')
        #Cascadia
        nation = 'Cascadia'
        data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
        
        data = data.json()
        mypath = 'nations/'+ nation+'.json'
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        if not os.path.isfile(mypath + '/'+ x + '.json'):
            print((mypath + '/'+ x + '.json'))
            createProfileTown(nation, x)
        ffn = mypath + '/'+ nation + '.json'
        with open(ffn, 'r') as f:
            loaded_data3 = json.load(f)
            f.close()
        
        loaded_data2 = json.loads(data)
        if diff(loaded_data2, loaded_data3) == {}:
            pass
        else:

            channel = bot.get_channel(1132711280009035859)
            difference = diff(loaded_data2, loaded_data3)
            results = differenceOrganizer(difference, loaded_data2, loaded_data3)
            print(results)
            if results[0] == False and results[1] == False and results[2] == False and results[3] == False and results[4] == False:
                print('no notable changes')
            else:
                embed = await buildEmbedFileNation(results, x)
                await channel.send(embed=embed)
                ffn = 'nations/{nation}/towns/{x}/{x}.json'.format(x = x, nation = nation)
                with open(ffn, 'w', encoding='utf-8') as l:
                    json.dump(loaded_data2, l, ensure_ascii=False, indent=4)
        time.sleep(1)
    def nationTownScanner(nation, x):
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                mypath = 'nations/'+ nation + '/towns/'+x
                if not os.path.isdir(mypath):
                    os.makedirs(mypath)
                if not os.path.isfile(mypath + '/'+ x + '.json'):
                    print((mypath + '/'+ x + '.json'))
                    createProfileTown(nation, x)
                data2 = json.dumps(data2)
                ffn = mypath + '/'+ x + '.json'
                with open(ffn, 'r') as f:
                    loaded_data3 = json.load(f)
                    f.close()
                
                loaded_data2 = json.loads(data2)
                print(loaded_data2, loaded_data3)
                if diff(loaded_data2, loaded_data3) == {}:
                    return False, loaded_data2, loaded_data3, ffn
                else:
                    return True, loaded_data2, loaded_data3, ffn
    #Build an embed for gdp to post in a channel
    async def buildEmbedGdp(gdp, nation, value):
        embed=discord.Embed(title=value+" GDP", description='GDG of '+value.lower())
        embed.set_author(name="P.I.G By DaPigThatBig", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.add_field(name=value, value=nation, inline=True)
        embed.add_field(name="GDP", value=gdp, inline=True)
        embed.set_footer(text="Powered by DaPigThatBig")
        return embed

    #Build an embed for daily report of GDP to post in a channel
    async def buildEmbedDailyReportGDP(a,b,c,d,e):
        embed=discord.Embed(title='GDG Daily Report', description='Total amount of liquid gold in a nation')
        embed.set_author(name="P.I.G By DaPigThatBig", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.add_field(name=a[0], value=str(a[1])+'g', inline=True)
        embed.add_field(name=b[0], value=str(b[1])+'g', inline=True)
        embed.add_field(name=c[0], value=str(c[1])+'g', inline=True)
        embed.add_field(name=d[0], value=str(d[1])+'g', inline=True)
        embed.add_field(name=e[0], value=str(e[1])+'g', inline=True)
        embed.set_footer(text="Powered by DaPigThatBig")
        return embed
    
    async def buildEmbedFileNation(results, town):
        embed=discord.Embed(title=town+' Change Report')
        embed.set_author(name="P.I.G By DaPigThatBig", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.add_field(name='Gold', value=str(results[0]), inline=True)
        embed.add_field(name='Residents', value=str(results[1]), inline=True)
        embed.add_field(name='Total Chunks', value=str(results[2]), inline=True)
        embed.add_field(name='Nation', value=str(results[3]), inline=True)
        embed.add_field(name='Mayor', value=str(results[4]), inline=True)
        embed.set_footer(text="Powered by DaPigThatBig")
        return embed

    #Makes an embed if a player is too close to the nation
    async def buildEmbed(closesttown, x, z, name, maplink, knownHunter, nation):
        embed=discord.Embed(title="Player Spotted", description=name)
        embed.set_author(name="P.I.G UAV By DaPigThatBig", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.add_field(name="Known Hunter?", value=knownHunter, inline=True)
        embed.add_field(name="Nearest Town", value=closesttown, inline=True)
        embed.add_field(name="Coordinates", value=str(x) + ' '+ str(z), inline=True)
        embed.add_field(name="Nation", value=nation, inline=True)
        embed.add_field(name="Map Link", value=maplink, inline=True)
        embed.set_footer(text="Powered by DaPigThatBig")
        return embed

    async def buildCounterEmbed(counter, arg):
        embed=discord.Embed(title="Player Data", description=arg)
        embed.set_author(name="P.I.G By DaPigThatBig", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
        for items in counter.items():
            embed.add_field(name=str(items[0]).strip('[]\'')+ ':00 CST', value=str(items[1]) + ' pings', inline=True)
        embed.set_footer(text="Powered by DaPigThatBig")
        return embed

    def getData():
        response = requests.get(
        "https://emctoolkit.vercel.app/api/aurora/onlineplayers")
        data = response.json()
        return data

    def getDataForLOT():
        response = requests.get(
        "https://emctoolkit.vercel.app/api/aurora/allplayers")
        data = response.json()
        return data

    def townspawnfinder(town):
        response = requests.get(
        "https://emctoolkit.vercel.app/api/aurora/towns/"+town)
        data = response.json()
        time.sleep(0.2)
        return data
    def townSpawnFinderMAX():
        response = requests.get(
        "https://emctoolkit.vercel.app/api/aurora/towns")
        data = response.json()
        time.sleep(1)
        return data
    def townFallDateCalc(lastonline):
        epoch = time.time()
        fourtytwodays = 3666543

        return lastonline+fourtytwodays

    def epochToTime(epoch):
        realtime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(epoch))
        return realtime

    def knownHunters(name):
        if name in hunters:
            return ':white_check_mark:'
        else:
            return ':x:'
    
    def findLastOnline(ign):
        data = requests.get(('https://api.earthmc.net/v1/aurora/residents/{ign}').format(ign=ign))
        data = data.json()

        import time
        import datetime
        
        presentDate = datetime.datetime.now()
        unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
        lo = data['timestamps']['lastOnline']
        if int(unix_timestamp) - lo > 2551200000:
            return True          
        return False
    def checkIfOnList(ign):
                    
        with open("42check.txt", "r") as k:
                lines = k.readlines()
                k.close()
        print(lines)
        if ign in lines:
            print('Already notified')
            return False
        else:
            print('test')
            wtl(ign)
            return True
    def addToList(ign):
        with open("42check.txt", "r") as l:
            lines = l.readlines()

        with open("42check.txt", "w+") as i:
            for line in i:
                if line.strip("\n") != ign:
                    
                    i.write(line)
    def getTownsMayor(town):
            data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
            data2 = data2.json()
            return data2
    def wtl(ign):
            with open("42check.txt", "a") as b:
                b.write(ign + '\n')

    def createProfileTown(nation, x):
        data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
        data2 = data2.json()
        mypath = 'nations/'+ nation + '/towns/'+x
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        fn = x + '.json'
        with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
             json.dump(data2, f, ensure_ascii=False, indent=4)
        time.sleep(1)
    
    def gdpp(nation):
        try:
            data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
            data = data.json()
            gdp = 0
            gdp +=data['stats']['balance']
            for x in data['residents']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/residents/'+x)
                data2 = data2.json()
                gdp +=int(data2['stats']['balance'])
                time.sleep(0.1)
            for x in data['towns']:
                data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
                data2 = data2.json()
                gdp +=int(data2['stats']['balance'])
                time.sleep(0.1)
                return nation, gdp
        except:
            pass

    def differenceOrganizer(x, ld2, ld3):
        #get bal
        if 'stats' in x:
            if 'balance' in x['stats']:
                balcalc = int(ld3['stats']['balance']) - int(ld2['stats']['balance'])
                bal = str(balcalc) + 'g'
            else:
                bal = False
            if 'numTownBlocks' in x['stats']:
                chunks = residents = int(ld3['stats']['numTownBlocks']) - int(ld2['stats']['numTownBlocks']) 
            else:
                chunks = False
            if 'numResidents' in x['stats']:
                residents = int(ld3['stats']['numResidents']) - int(ld2['stats']['numResidents']) 

            else:
                residents = False
        else:
            bal = False
            chunks = False
            residents = False

        #get mayor
        if 'strings' in x:
            if 'mayor' in x['strings']:
                mayor = x['strings']['mayor']
            else:
                mayor = False
        else:
            mayor = False
        #get nation
        if 'affiliation' in x:
            if 'nation' in x['affiliation']:
                nation = x['affiliation']['nation']
            else:
                nation = False

        else:
            nation = False
        return bal, residents, chunks, nation, mayor







    bot.run('')
