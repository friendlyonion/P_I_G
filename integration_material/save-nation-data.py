import requests
import time
import os
from datetime import timezone
import json
import datetime
import jsondiff as jd
from jsondiff import diff
def createProfile(nation):
    data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
    data = data.json()
    for x in data['towns']:
        data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
        data2 = data2.json()
        mypath = 'nations/Rocky_Mountains/towns/'+x
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        fn = x + '.json'
        with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
             json.dump(data2, f, ensure_ascii=False, indent=4)
        time.sleep(1)
        print(x)

def createProfileTown(town):
    data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = 'vinland'))
    data = data.json()
    for x in data['towns']:
        if x == town:
            data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
            data2 = data2.json()
            mypath = 'nations/Cascadia/towns/'+x
            if not os.path.isdir(mypath):
                os.makedirs(mypath)
            fn = x + '.json'
            with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
                 json.dump(data2, f, ensure_ascii=False, indent=4)
            time.sleep(1)
            print(x)


def checkChanges(nation):
    data = requests.get('https://api.earthmc.net/v1/aurora/nations/{nation}'.format(nation = nation))
    data = data.json()
    for x in data['towns']:
        data2 = requests.get('https://api.earthmc.net/v1/aurora/towns/'+x)
        data2 = data2.json()
        mypath = 'nations/Cascadia/towns/'+x
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        ts = x
        fn = str(ts) + '.json'
        data2 = json.dumps(data2)
        ffn = mypath+'/'+fn
        with open(ffn) as f:
            loaded_data3 = json.load(f)
        loaded_data2 = json.loads(data2)
        if diff(loaded_data2, loaded_data3) == []:
            pass
        else:
            with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
                 json.dump(data2, f, ensure_ascii=False, indent=4)
createProfile('Rocky_Mountains')


def genTimestamp():
    dt = datetime.datetime.now(timezone.utc)
  
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp

#while True:
#    data = requests.get('https://api.earthmc.net/v1/aurora/nations/')
#    data = data.json()
#    for x in data['allNations']:
#        print(x)
#        data2 = requests.get('https://api.earthmc.net/v1/aurora/nations/'+x)
#        data2 = data2.json()
#        time.sleep(0.1)
#        mypath = 'nations/'+x
#        if not os.path.isdir(mypath):
#            os.makedirs(mypath)
#        ts = x
#        fn = str(ts) + '.json'
#        with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
#             json.dump(data2, f, ensure_ascii=False, indent=4)
#    time.sleep(500)

    




