class Welcome:
    def response():
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
