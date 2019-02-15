import discord

class ShipCard:
    def sidewinder():
        em = discord.Embed(
             title='**Ship Overview - Sidewinder Mk. I**',
             description="""The beginner\'s ship that\'s not good at anything in particular. 
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `32 000 Cr`
                            Hardpoints: `2x Small`
                            Top Speed: `220 m/s`
                            Boost Speed: `321 m/s`
                            Agility: `160`
                            Cargo Capacity: `4T`
                            Unladen Jump Range: `7,56 Ly`
                            ```Its primary use should be for data delivery missions and occasionally combat. Upgrade to higher tier ships is highly recommended.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/JB8bIGL.png'
        )
        await client.send_message(message.channel, embed=em)

    def eagle():
        em = discord.Embed(
             title='**Ship Overview - Eagle Mk. II**',
             description="""The cheapest combat focused ship, fast and packing a little bit of a punch. Doesn\'t stay alive for long.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `44 800 Cr`
                            Hardpoints: `3x Small`
                            Top Speed: `240 m/s`
                            Boost Speed: `350 m/s`
                            Agility: `178`
                            Cargo Capacity: `2T`
                            Unladen Jump Range: `8,47 Ly`
                            ```Made for combat, and terrible at everything else. Bounty hunting is an option as well as assassination missions.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/6vIyepf.png'
        )
        await client.send_message(message.channel, embed=em)

    def hauler():
        em = discord.Embed(
             title='**Ship Overview - Hauler**',
             description="""The first step for aspiring traders. Surprisingly better at exploring rather than trading.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `52 720 Cr`
                            Hardpoints: `1x Small`
                            Top Speed: `200 m/s`
                            Boost Speed: `305 m/s`
                            Agility: `144`
                            Cargo Capacity: `8T`
                            Unladen Jump Range: `9,87 Ly`
                            ```Decent at trading with the maximum of 22T carried at a time. Combat is not an option, but it can be quite useful for exploration.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/NfNL45G.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def adder():
        em = discord.Embed(
             title='**Ship Overview - Adder**',
             description="""The first multipurpose ship and the cheapest option for Multi-Crew.
                            It requires a **small** pad to land, which means it can land anywhere.
                            Buying cost: `87 808 Cr`
                            Hardpoints: `2x Small, 1x Medium`
                            Top Speed: `220 m/s`
                            Boost Speed: `320 m/s`
                            Agility: `144`
                            Cargo Capacity: `6T`
                            Unladen Jump Range: `9,12 Ly`
                            ```A direct upgrade of the Hauler, it does everything better. It can even go into combat and defend itself, as well as being the cheapest viable exploration vessel.```""",
             color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/REfDYLB.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def ieagle():
        em = discord.Embed(
            title='**Ship Overview - Imperial Eagle**',
            description="""An improved Eagle with better firepower.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `110 825 Cr`
                           Hardpoints: `2x Small, 1x Medium`
                           Top Speed: `302 m/s`
                           Boost Speed: `403 m/s`
                           Agility: `145`
                           Cargo Capacity: `2T`
                           Unladen Jump Range: `8,22 Ly`
                           ```Featuring better firepower and speed than the Eagle, at the cost of a trip to Imperial space and earning a rank. Trading and exploring are not an option.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/0ETb9mN.png'
        )
        await client.send_message(message.channel, embed=em)

    def viper3():
        em = discord.Embed(
            title='**Ship Overview - Viper Mk. III**',
            description="""A combat oriented vessel with small bits of versatility. 
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `142 931 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `310 m/s`
                           Boost Speed: `388 m/s`
                           Agility: `135`
                           Cargo Capacity: `4T`
                           Unladen Jump Range: `6,92 Ly`
                           ```While not as agile as the Eagles, the Viper Mk. III is tankier and can take on tougher enemies. While non-combat activities aren\'t optimal, they are still a possibility.```""",
            color=0xff7700,
        )
        em.set_image(
             url='https://imgur.com/0vPA1tS.png'
        )
        await client.send_message(message.channel, embed=em)

    def cobra3():
        em = discord.Embed(
            title='**Ship Overview - Cobra Mk. III**',
            description="""A multipurpose ship that won\'t hold you back, also with Multi-Crew.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `379 718 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `282 m/s`
                           Boost Speed: `402 m/s`
                           Agility: `140`
                           Cargo Capacity: `18T`
                           Unladen Jump Range: `10,46 Ly`
                           ```The ship is great for combat, trading, exploring, and even mining.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/1OODhnZ.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def viper4():
        em = discord.Embed(
            title='**Ship Overview - Viper Mk. IV**',
            description="""Viper III\'s tougher and more versatile brother.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `437 930 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `271 m/s`
                           Boost Speed: `342 m/s`
                           Agility: `140`
                           Cargo Capacity: `18T`
                           Unladen Jump Range: `10,36 Ly`
                           ```Decent at everything, but best at combat. It can!t do exploration too well, though.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/Cai03ei.png'
        )        
        await client.send_message(message.channel, embed=em)

    def dbscout():
        em = discord.Embed(
            title='**Ship Overview - Diamondback Scout**',
            description="""The first ship in the line of explorers.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `564 329 Cr`
                           Hardpoints: `2x Small, 2x Medium`
                           Top Speed: `283 m/s`
                           Boost Speed: `384 m/s`
                           Agility: `150`
                           Cargo Capacity: `0T`
                           Unladen Jump Range: `11,35 Ly`
                           ```Surprisingly good at combat with excellent heat management, but even better as an early exploration ship.```""",
            color=0xff7700
        )
        em.set_image(
            url='https://imgur.com/xDzltVR.png'
        )
        await client.send_message(message.channel, embed=em)

    def cobra4():
        em = discord.Embed(
            title='**Ship Overview - Cobra Mk. IV **',
            description="""A pre-order exclusive multipurpose vessel.
                           It requires a **small** pad to land, which means it can land anywhere.
                           Buying cost: `764 720 Cr`
                           Hardpoints: `3x Small, 2x Medium`
                           Top Speed: `200 m/s`
                           Boost Speed: `299 m/s`
                           Agility: `1525`
                           Cargo Capacity: `34T`
                           Unladen Jump Range: `9,37 Ly`
                           ```Trades mobility for durability when compared to Comba Mk. III, it is better in terms of internals and cargo capacity, but lacks in jump range.```""",
            color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/FrJDu7K.png'
        )
        await client.send_message(message.channel, embed=em)

    def type6():
        em = discord.Embed(
              title='**Ship Overview - Type-6 Transporter**',
              description="""The first dedicated freighter-type vessel.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `1 045 945 Cr`
                             Hardpoints: `2x Small`
                             Top Speed: `223 m/s`
                             Boost Speed: `355 m/s`
                             Agility: `140`
                             Cargo Capacity: `50T`
                             Unladen Jump Range: `12,39 Ly`
                             ```One of the worst ships for combat purposes. On the other hand it excels in trading with the capacity of 112T. Not an ideal explorer, but it works.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/lC4epCE.png'
        )
        await client.send_message(message.channel, embed=em)

    def dolphin():
        em = discord.Embed(
              title='**Ship Overview - Dolphin**',
              description="""An affordable passenger carrier that opens a new set of missions.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `1 337 330 Cr`
                             Hardpoints: `2x Small`
                             Top Speed: `258 m/s`
                             Boost Speed: `361 m/s`
                             Agility: `143`
                             Cargo Capacity: `14T`
                             Unladen Jump Range: `10,67 Ly`
                             ```One of the more cost-effective explorers with good internals and jump range. It can also bring passengers along for long-range trips.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/TrxRcg3.png'
        )
        await client.send_message(message.channel, embed=em)

    def dbexplorer():
        em = discord.Embed(
              title='**Ship Overview - Diamondback Explorer**',
              description="""An excellent explorer as well as a capable fighter.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `1 894 760 Cr`
                             Hardpoints: `2x Medium, 1x Large`
                             Top Speed: `242 m/s`
                             Boost Speed: `316 m/s`
                             Agility: `131`
                             Cargo Capacity: `12T`
                             Unladen Jump Range: `14,15 Ly`
                             ```This ship boasts one of the highest possible jump-ranges in the game for its cost. It is also fully capable of being a combat ship with its Large hardpoint.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/ZqzAQ1s.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def icourier():
        em = discord.Embed(
              title='**Ship Overview - Imperial Courier**',
              description="""A great combat ship, often nicknamed a super Eagle.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `2 542 931 Cr`
                             Hardpoints: `3x Medium`
                             Top Speed: `277 m/s`
                             Boost Speed: `380 m/s`
                             Agility: `138`
                             Cargo Capacity: `12T`
                             Unladen Jump Range: `7,81 Ly`
                             ```A strong and agile combat vessel with one of the best cockpits, not great at exploring or trade however.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/WLeSfHf.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def keelback():
        em = discord.Embed(
              title='**Ship Overview - Keelback**',
              description="""Type-6 modified for combat, it also has a fighter bay.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `3 126 150 Cr`
                             Hardpoints: `2x Small, 2x Medium`
                             Top Speed: `202 m/s`
                             Boost Speed: `303 m/s`
                             Agility: `135`
                             Cargo Capacity: `38T`
                             Unladen Jump Range: `10,94 Ly`
                             ```It doesn't do trading as well as the Type-6, but it can defend itself very well. The first ideal deep core miner.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/8FT9JE1.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def aspscout():
        em = discord.Embed(
              title='**Ship Overview - Asp Scout**',
              description="""A cheaper variant of the Asp Explorer, a decent fighter-explorer hybrid.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `3 961 150 Cr`
                             Hardpoints: `2x Small, 2x Medium`
                             Top Speed: `223 m/s`
                             Boost Speed: `304 m/s`
                             Agility: `160`
                             Cargo Capacity: `16T`
                             Unladen Jump Range: `11,69 Ly`
                             ```It's a decent combat ship and a decent explorer. At the same time, it gets outclassed by the Asp Explorer in everything.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/ZwNXiwl.png'
        )
        await client.send_message(message.channel, embed=em)

    def vulture():
        em = discord.Embed(
              title='**Ship Overview - Vulture**',
              description="""A pure combat ship - deadly and nimble.
                             It requires a **small** pad to land, which means it can land anywhere.
                             Buying cost: `4 925 615 Cr`
                             Hardpoints: `2x Large`
                             Top Speed: `210 m/s`
                             Boost Speed: `340 m/s`
                             Agility: `162`
                             Cargo Capacity: `8T`
                             Unladen Jump Range: `7,93 Ly`
                             ```It has great firepower thanks to its Large hardpoints, but its jump range and power plant hold it back.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/UKOQ3QA.png'
        )
        await client.send_message(message.channel, embed=em)
        
    def aspx():
        em = discord.Embed(
              title='**Ship Overview - Asp Explorer**',
              description="""An explorer's pick - and good for everything else too.
                             It requires a **medium** pad to land, which means it can land anywhere.
                             Buying cost: `6 661 153 Cr`
                             Hardpoints: `4x Small, 2x Medium`
                             Top Speed: `254 m/s`
                             Boost Speed: `345 m/s`
                             Agility: `140`
                             Cargo Capacity: `38T`
                             Unladen Jump Range: `13,12 Ly`
                             ```Exploration is in its name, and it's great. Good at combat as well as mining and trading.```""",
              color=0xff7700,
        )
        em.set_image(
            url='https://imgur.com/rziK2Hb.png'
        )
        await client.send_message(message.channel, embed=em)
