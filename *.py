@bot.command(pass_context = True)
async def changeLI(msg):
    with open("levelir.json", 'r',encoding="utf-8") as ir:   
        irasuto = json.load(ir)
        if irasuto.get(str(msg.message.author.id)) == None:
            irasuto[str(msg.message.author.id)] = 2
            embed = discord.Embed(title="背景を変更しました!", description="", color=0xfcc800)
            embed.set_image(url="https://cdn.discordapp.com/attachments/527676696481103882/533889358692876333/bkg.png")
            msg2 = await bot.say(embed=embed)
        else:
            userir = irasuto[str(msg.message.author.id)]
            if userir == 4:
                irasuto[str(msg.message.author.id)] = 1
                embed = discord.Embed(title="背景を変更しました!", description="", color=0xfcc800)
                embed.set_image(url="https://cdn.discordapp.com/attachments/514788807439286293/533886139581464595/icon11.png")
                msg2 = await bot.say(embed=embed)
            if userir == 1:
                irasuto[str(msg.message.author.id)] = 2
                embed = discord.Embed(title="背景を変更しました!", description="", color=0xfcc800)
                embed.set_image(url="https://cdn.discordapp.com/attachments/527676696481103882/533889358692876333/bkg.png")
                msg2 = await bot.say(embed=embed)
            if userir == 2:
                irasuto[str(msg.message.author.id)] = 3
                embed = discord.Embed(title="背景を変更しました!", description="", color=0xfcc800)
                embed.set_image(url="https://cdn.discordapp.com/attachments/513704392004993050/534008298685595649/g4583.png")
                msg2 = await bot.say(embed=embed)
            if userir == 3:
                irasuto[str(msg.message.author.id)] = 4
                embed = discord.Embed(title="背景を変更しました!", description="", color=0xfcc800)
                embed.set_image(url="https://cdn.discordapp.com/attachments/497983550625153024/534320078188183572/unknown.png")
                msg2 = await bot.say(embed=embed)
        with open("levelir.json", 'w') as wdr:
            json.dump(irasuto, wdr)
        sleep(5)
        await bot.delete_message(msg2)
        await bot.say("背景を設定しました。")
