import requests
import time
import os
from datetime import timezone
import json
import datetime
def genTimestamp():
    dt = datetime.datetime.now(timezone.utc)
  
    utc_time = dt.replace(tzinfo=timezone.utc)
    utc_timestamp = utc_time.timestamp()
    return utc_timestamp
while True:
    data = requests.get('https://api.earthmc.net/v1/aurora/nations/')
    data = data.json()
    for x in data['allNations']:
        print(x)
        data2 = requests.get('https://api.earthmc.net/v1/aurora/nations/'+x)
        data2 = data2.json()
        time.sleep(0.1)
        mypath = 'nations/'+x
        if not os.path.isdir(mypath):
            os.makedirs(mypath)
        ts = genTimestamp()
        fn = str(ts) + '.json'
        with open(mypath+'/'+fn, 'w', encoding='utf-8') as f:
             json.dump(data2, f, ensure_ascii=False, indent=4)
    time.sleep(500)



