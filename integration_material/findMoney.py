import requests
import time
data = requests.get('https://api.earthmc.net/v1/aurora/towns')
data = data.json()
def findLastOnline(ign):
    data = requests.get(('https://api.earthmc.net/v1/aurora/residents/{ign}').format(ign=ign))
    data = data.json()

    import time
    import datetime
    
    presentDate = datetime.datetime.now()
    unix_timestamp = datetime.datetime.timestamp(presentDate)*1000
    lo = data['timestamps']['lastOnline']
    if int(unix_timestamp) - lo > 1728000000:
        return True         
    return False
for town in data['allTowns']:
    data2 = requests.get(('https://api.earthmc.net/v1/aurora/towns/{town}').format(town = town))
    data2 = data2.json()
    if data2['stats']['numResidents'] == 1 and data2['stats']['balance'] >10 and data2['status']['isOpen'] == True and findLastOnline(data2['strings']['mayor']) == True:
        print(town)
    time.sleep(1)

