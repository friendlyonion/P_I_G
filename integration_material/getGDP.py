import requests
import time
data = requests.get('https://api.earthmc.net/v1/aurora/nations/Cascadia')
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

print(gdp)