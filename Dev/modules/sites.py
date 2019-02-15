class Sites:
    def coriolis():
        em = discord.Embed(
            title='Coriolis EDCD Edition',
            url='https://coriolis.io',
            description='A ship builder, outfitting and comparison tool for Elite Dangerous',
            color=0xff7700
        )
        em.add_field(
            name='Note', value='***Please use the s.orbis built-in short link when sharing builds! [Link icon on top right of coriolis page]***'
        )
        em.set_image(
            url='https://coriolis.io/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    def fuelRats():
        em = discord.Embed(
            title='The Fuel Rats',
            url='https://fuelrats.com',
            description='The Fuel Rats are Elite: Dangerous\'s premier emergency refueling service. Fueling the galaxy, one ship at a time, since 3301.',
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/XHCgDTo.png'
        )
        await client.send_message(message.channel, embed=em)

    def inara():
        em = discord.Embed(
            title='INARA - Elite:Dangerous companion',
            url='https://inara.cz',
            description='The companion site for Elite:Dangerous. Market data, CMDR\'s logs, logbooks, wings, galleries, powerplay, engineers, crafting, galaxy info, news and more...',
            color=0xff7700
        )
        em.set_image(
            url='https://inara.cz/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    def eddb():
        em = discord.Embed(
            title='Elite: Dangerous Database - EDDB',
            url='https://eddb.io',
            description='A site about systems, bodies, stations, commodities, materials and trade routes in Elite: Dangerous.',
            color=0xff7700
        )
        em.set_image(
            url='https://eddb.io/mstile-144x144.png'
        )
        await client.send_message(message.channel, embed=em)

    def edRefCard():
        em = discord.Embed(
            title='EDRefCard',
            url='https://edrefcard.info',
            description='Create and optionally publish a graphical reference card for your Elite: Dangerous keyboard and controller bindings.',
            color=0xff7700
        )
        em.set_image(
            url='https://i.imgur.com/qO578Mn.jpg'
        )
        await client.send_message(message.channel, embed=em)

    def edsm():
        em = discord.Embed(
            title='EDSM - Elite Dangerous Star Map',
            url='https://edsm.net',
            description='The Galactic Positioning System of Elite: Dangerous at your service.',
            color=0xff7700
        )
        em.set_image(
            url='https://www.edsm.net/img/favicons/mstile-144x144.png'
        ) 
        await client.send_message(message.channel, embed=em)
