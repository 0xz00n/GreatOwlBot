import discord

class Roles:
    def pcRole(discord, client):
        role = discord.utils.get(message.server.roles, name='PC')
        if discord.utils.get(message.author.roles, name='PC'):
            msg = 'You already have the PC role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PC role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the PC role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    def xb1Role(discord, client):
        role = discord.utils.get(message.server.roles, name='XBOX 1')
        if discord.utils.get(message.author.roles, name='XBOX 1'):
            msg = 'You already have the Xbox 1 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the Xbox 1 role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the Xbox 1 role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)

    def ps4Role(discord, client):
        role = discord.utils.get(message.server.roles, name='PS4')
        if discord.utils.get(message.author.roles, name='PS4'):
            msg = 'You already have the PS4 role. Would you like to be removed from that role, CMDR?\n(y/n)'
            await client.send_message(message.channel, msg)
            reply = await client.wait_for_message(timeout=30, author=message.author)
            if reply == None:
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content.lower() == 'y':
                await client.remove_roles(message.author, role)
                await client.send_message(message.channel, 'You have been removed from the PS4 role.')
            elif reply.content.lower() == 'n':
                await client.send_message(message.channel, 'Your roles have not been modified, CMDR')
            elif reply.content != None:
                await client.send_message(message.channel, 'Unrecognized response. Your roles have not been modified, CMDR')
        else:
            msg = 'Adding you to the PS4 role, CMDR.'
            await client.add_roles(message.author, role)
            await client.send_message(message.channel, msg)
