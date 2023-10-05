import discord
import requests
import json
from decimal import Decimal
from web3 import Web3
import time
from discord.ext import tasks
bot = discord.Bot()
print('connected')

@tasks.loop(seconds=10)
async def statusloop():
    await bot.wait_until_ready()
    with open('c.txt', 'r') as ll:
        lll=ll.read()   
        llll = len(lll)
        #print(llll)
    await bot.change_presence(status=discord.Status.dnd, activity=discord.Activity(type=discord.ActivityType.watching, name=("{val} payments.").format(val = llll)))
statusloop.start()

@bot.slash_command(name="invoice")
async def invoice(ctx: discord.ApplicationContext, value, to):
    invoiceID = '129737'
    await ctx.respond('Generating invoice...')
    with open('c.txt', 'a') as l:
        l.write('1')
    embed = await buildEmbed('1237197', 'ETH', to, value)
    await ctx.send(embed=embed, view=MyView(value, to, invoiceID))


async def buildEmbed(invoiceNumber, token, toAddy, amount):
    embed=discord.Embed(title="Invoice", description=invoiceNumber)
    embed.set_author(name="Invoice created with XYZ", icon_url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
    embed.set_thumbnail(url="https://i.pinimg.com/originals/74/99/b2/7499b29c229af9dcad36b64d666d2d5a.png")
    embed.add_field(name="Amount", value=amount, inline=True)
    embed.add_field(name="Token", value=token, inline=True)
    embed.add_field(name="To", value=toAddy, inline=True)
    embed.set_footer(text="Powered by drasil.pro")
    return embed
class MyView(discord.ui.View): # Create a class called MyView that subclasses discord.ui.View
    def __init__(self, value, to, invoiceID):
        super().__init__()
        self.value = value
        self.to = to
        self.invoiceID = invoiceID
    @discord.ui.button(label="Pay Invoice", style=discord.ButtonStyle.primary) # Create a button with the label "😎 Click me!" with color Blurple
    async def button_callback(self, button, interaction):
        #await interaction.response.send_message("Transfer " + self.value + " to " + self.to + ". Then use the command /pinvoice with your invoice id and transaction hash.")
        await interaction.response.send_modal(MyText(self.value, self.to, title="Invoice Confirmation for "+ self.invoiceID))
class MyText(discord.ui.Modal):
    def __init__(self,  value, to, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.value = value
        self.to = to
        self.add_item(discord.ui.InputText(label="Transaction Hash", style=discord.InputTextStyle.short))

    async def callback(self, interaction: discord.Interaction):
        embed = discord.Embed(title="Transaction confirmed")
        if transactionCheckIfValid(str(self.children[0].value), self.to, self.value) == True:
            await interaction.response.send_message(embeds=[embed])
        else:
            await interaction.response.send_message('Fail')

def transactionCheckIfValid(hash, to, value):
    #Call api with transaction hash to see how much eth was transferred. If valid return True else False.
    r = requests.get('https://api.etherscan.io/api?module=proxy&action=eth_getTransactionByHash&txhash={hash}&apikey={apikey}'.format(hash = hash, apikey = '8167G4TUBDFF728UDR2YM6CFC1D9CJ8X9C'))
    data = r.json()
    print(data)
    if 'error' in data:
        return False
    val = int(data['result']['value'], 16)
    owed = convert(value)
    print(val, owed)
    if data['result']['to'] == to:
        if val >= owed:
            return True
    else:
        return False

def convert(amount):
    return Web3.to_wei(amount, 'ether')
bot.run('MTA5NzY0MzQzNzQyNTE2ODQ1NA.GLqNE0.IIBZz0lLyYNc_IBIp5JEhcwsS6tEwelHP_p3VI')

