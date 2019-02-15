class TtokResponse:
    def vopals():
	em = discord.Embed(
            title='Void Opal Mining',
            description='The Tower of Knowledge doesn\'t prohibit the discussion or practice of lucrative deep-core mining. However, it shouldn\'t come off as the absolute one-and-only way of making Credits ingame. We value enjoyment over Credits at any and all costs.'
                        ' Always let others find what they enjoy the most.',
            color=0xff7700,
        )
        em.set_image(
             url='http://remlok-industries.fr/wp-content/uploads/2017/10/ED-FX17-Mining.jpg'
        )

        await client.send_message(message.channel, embed=em)

    def materials():
	em = discord.Embed(
             title='Engineering Materials Spreadsheet',
             url='https://docs.google.com/spreadsheets/d/1Mp7l0bSnMp_G7xWUm75M-XuihDfTdi27rm-vB9K8AX0/edit?usp=sharing',
             description='A spreadsheet containing all materials required for engineering and how/where to get them.',
             color=0xff7700,
        )
        em.set_image(
             url='https://yt3.ggpht.com/a-/AAuE7mDaBvvb0xSIVhahkb9hnhQwqOnjmYE50OPxew=s288-mo-c-c0xffffffff-rj-k-no'
        )

        await client.send_message(message.channel, embed=em)
