#have script check for all towns that are in cascadia.
#once all towns are found then check for mayors last online date.
#if last online date was more than 30 days ago then send notification..

import requests
import time
def findLastOnline(ign):
    data = requests.get(('https://api.earthmc.net/v1/aurora/residents/{ign}').format(ign=ign))
    data = data.json()

    import time
    import datetime
    
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    lo = data['timestamps']['lastOnline']
    if int(unix_timestamp) - lo > 2851200000:
        return True         
    return False
data = requests.get('https://api.earthmc.net/v1/aurora/nations/Cascadia')
data = data.json()
for town in data['towns']:
    data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
    data2 = data2.json()
    ign = data2['strings']['mayor']
    if findLastOnline(ign) == True:
        with open("42check.txt", "a+") as k:
            lines = k.readlines()
            if ign in lines:
                print('Already notified')
            else:
                k.write(ign)
                print(ign, town)
    else:
        with open("42check.txt", "r") as l:
            lines = l.readlines()

        with open("42check.txt", "w") as l:
            for line in lines:
                if line.strip("\n") != ign:
                    l.write(line)
    time.sleep(1)
