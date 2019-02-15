class HelpMenus:
#    def __init__(self):
    def genHelp():
        em = discord.Embed(
            title='Great Owl Help',
            description="""Help Commands:
                        !help: Displays this help message
                        !rolehelp: Role command help
                        !shiphelp: Ship information help\n
                        Website Link Commands:
                        !coriolis: Coriolis website
                        !eddb: Elite Dangerous Database website
                        !edrefcard: EDRefCard website
                        !edsm: Elite Dangerous Star Map website
                        !inara: INARA website\n
                        Other Commands:
                        !vopals: Our stance on core mining
                        !materials: Spreadsheet for engineering materials and their locations""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)

    def roleHelp():
        em = discord.Embed(
            title='Great Owl Role Help',
            description="""!pc: Add yourself to the PC role
                        !xb1: Add yourself to the Xbox 1 role
                        !ps4: Add yourself to the PS4 role\n
                        If you run a command while already assigned to its role, you will be asked if you wish to be removed from the role.""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)

    def shipHelp():
        em = discord.Embed(
            title='Great Owl Ship Help',
            description="""Information pertaining to each ship listed:
                        !sidewinder: Sidewinder
                        !eagle: Eagle
                        !hauler: Hauler
                        !adder: Adder
                        !ieagle: Imperial Eagle
                        !viper3: Viper Mk.III
                        !cobra3: Cobra Mk.III
                        !viper4: Viper Mk.IV
                        !dbscout: Diamondback Scout
                        !cobra4: Cobra Mk.IV
                        !type6: Type-6 Transporter
                        !dolphin: Dolphin
                        !dbexplorer: Diamondback Explorer
                        !icourier: Imprerial Courier
                        !keelback: Keelback
                        !aspscout: Asp Scout
                        !vulture: Vulture
                        !aspx: Asp Explorer""",
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/7yG4taS.jpg'
        )
        await client.send_message(message.channel, embed=em)
