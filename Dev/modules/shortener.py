class Shortener:
    def coriolis():
	msg = message.content
        url = re.findall(r'(https?://\S+)', msg)[0]
        r = requests.post(
            'https://s.orbis.zone/api.php',
            files = {
                'action': (None, 'shorturl'),
                'url': (None, url),
                'format': (None, 'json')
            },
            headers = {
                'referer': url,
                'origin': 'https://coriolis.io'
            }
        )
        response = r.json()
        await client.send_message(message.channel, "I've edited your message, {0.author.mention}:\n{1}".format(message, msg.replace(url, response['shorturl'])))
        await client.delete_message(message)
