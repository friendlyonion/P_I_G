import requests
import keyboard
import time
import random

def townless():
    data2 = requests.get(('https://emctoolkit.vercel.app/api/aurora/townless'))
    data2 = data2.json()
    time.sleep(5)
    keyboard.press('enter')
    time.sleep(2)
    keyboard.write('Townless? Type /t join Fjord -> Free diamond gear/food -> A home and a job.')
    keyboard.press('enter')
    time.sleep(2)
    playerlist = []
    for player in data2:
        #print(player['name'])
        keyboard.press('enter')
        time.sleep(randomIntt())
        keyboard.write('/t invite ' + player['name'])
        time.sleep(0.3)
        keyboard.press('enter')

        time.sleep(1)
        playerlist.append(player['name'])

    time.sleep(60)
    command = '/t invite -'
    for player in playerlist:
        keyboard.press('enter')
        time.sleep(0.3)
        keyboard.write(command + player )
        time.sleep(1)
        keyboard.press('enter')
        time.sleep(1)
def randomIntt():
    return random.uniform(0.5, 1.5)
townless()