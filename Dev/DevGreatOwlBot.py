#!/usr/bin/python3

import re
import discord
import requests
from modules.welcome import Welcome
from modules.help import HelpMenus
from modules.sites import Sites
from modules.shortener import Shortener
from modules.ships import ShipCard
from modules.roles import Roles
from modules.ttokresponse import TtokResponse

tokenfile = open('token','r')
TOKEN = tokenfile.readline().rstrip()

client = discord.Client()

lectureHalls = ['general','training-requests','ships-and-outfitting','combat','trading','mining','exploration']

@client.event
async def on_message(message):
    #Don't reply to yourself
    if message.author == client.user:
        return

    #Help response
    if message.content.startswith('!help'):
        HelpMenus.genHelp()

    #Coriolis response
    if message.content.startswith('!coriolis'):
        Sites.coriolis()

    #Fuel Rats response
    if message.content.startswith('!fuelrats'):
        Sites.fuelRats()

    #INARA response
    if message.content.startswith('!inara'):
        Sites.inara()

    #EDDB response
    if message.content.startswith('!eddb'):
        Sites.eddb()

    #EDRefCard response
    if message.content.startswith('!edrefcard'):
        Sites.edRefCard()

    #EDSM response
    if message.content.startswith('!edsm'):
        Sites.edsm()

    #Role help response
    if message.content.startswith('!rolehelp'):
        HelpMenus.roleHelp():

    #Role Assignment PC
    if message.content.startswith('!pc'):
        Roles.pcRole()

    #Role Assignment XB1
    if message.content.startswith('!xb1'):
        Roles.xb1Role()

    #Role Assignment PS4
    if message.content.startswith('!ps4'):
        Role.ps4Role()

    #Coriolis autoshortener
    if all(chunk in message.content for chunk in ('coriolis.io/outfit/', '?code=')):
        Shortener.coriolis()

    #Vopals response
    if message.content.startswith('!vopals'):
        TtokResponse.vopals()

    #Engineering materials
    if message.content.startswith('!materials'):
        TtokResponse.materials()

    #Ship help response
    if message.content.startswith('!shiphelp'):
        HelpMenus.shipHelp()

    #Sidewinder card
    ### Look into making the cards programmatically less space consuming.
    if message.content.startswith('!sidewinder'):
        ShipCard.sidewinder()

    #Eagle card
    if message.content.startswith('!eagle'):
        ShipChard.eagle()
        
    #Hauler card
    if message.content.startswith('!hauler'):
        ShipCard.hauler()
        
    #Adder card
    if message.content.startswith('!adder'):
        ShipCard.adder()
        
    #IEagle card
    if message.content.startswith('!ieagle'):
        ShipCard.ieagle()

    #Viper3 card
    if message.content.startswith('!viper3'):
        ShipCard.viper3()

    #Cobra3 card
    if message.content.startswith('!cobra3'):
        ShipCard.cobra3()
        
    #Viper4 card
    if message.content.startswith('!viper4'):
        ShipCard.viper4()

    #DBS card
    if message.content.startswith('!dbscout'):
        ShipCard.dbscout()

    #Cobra4 card
    if message.content.startswith('!cobra4'):
        ShipCard.cobra4()

    #Type6 card
    if message.content.startswith('!type6'):
        ShipCard.type6()

    #Dolphin card
    if message.content.startswith('!dolphin'):
        ShipCard.dolphin()

    #DBX card
    if message.content.startswith('!dbexplorer'):
        ShipCard.dbexplorer()
        
    #ImpCourier card
    if message.content.startswith('!icourier'):
        ShipCard.icourier()
        
    #Keelback card
    if message.content.startswith('!keelback'):
        ShipCard.keelback()
        
    #ASPS card
    if message.content.startswith('!aspscout'):
        ShipCard.aspscout()

    #Vulture card
    if message.content.startswith('!vulture'):
        ShipCard.vulture()
        
    #ASPX card
    if message.content.startswith('!aspx'):
        ShipCard.aspx()
    
#Welcome new users
@client.event
async def on_member_join(member):
    joinchan = discord.utils.get(member.server.channels, name='cmdr-lounge', type=discord.ChannelType.text)
    chanlist = ''
    for server in client.servers:
        if member.server == server:
            for channel in server.channels:
                if str(channel) in lectureHalls:
                    chanlist += channel.mention + '\n'
    em = discord.Embed(
        title='',
        description='Welcome, CMDR {0.mention}.\nIf you have any questions, use one of these Lecture Halls:\n{1}\nIf, however, you want to become a guide, please mention an Overseer or Admin in this channel to start the process. Enjoy your stay and fly safe CMDR, o7'.format(member,chanlist),
        color=0xff7700
    )
    await client.send_message(joinchan, embed=em)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
