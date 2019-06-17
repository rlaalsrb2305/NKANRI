import discord
import openpyxl
import request
import bs4


client = discord.Client()



@client.event
async def on_ready():
    print("남탕대장 출근!")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    print("이것은 조선관리인 봇의 클라이언트입니다")
    print("본 클라이언트의 저작권은 세콤에게 있습니다")
    print("현재 남탕관리인이 사용할수 있는 명령어는")
    print("!명령어,!변태순위 입니다")
    print("===========")

    await client.change_presence(game=discord.Game(name="위대한 수령동지를 위하여 | !도움말", type=1))

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "린민":
            role = i
            break
    await client.add_roles(member, role)
    fmt = '{0.mention} 동무가 월북했디 모두 축하해주라우!'
    channel = member.server.get_channel("589619364542808065")
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_member_remove(member):
    channel = member.server.get_channel("589619364542808065")
    fmt = '{0.mention} 동무가 탈북했다우 간나새끼..'
    await client.send_message(channel, fmt.format(member, member.server))

@client.event
async def on_message(message):
    if message.author.bot:
        return None

    id = message.author.id
    channel = message.channel

    if message.content.startswith("!도움말"):
        channel = message.channel
        embed = discord.Embed(
            title='도움말',
            description='내래 도움말이오',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='이상이라우')
        embed.add_field(name='!학습', value='내래 이몸을 가르치라우 !학습 [호출단어] [말할단어]', inline=False)
        embed.add_field(name='!기억', value='내래 가르친걸 기억한다우 !기억 [호출단어]', inline=False)
        embed.add_field(name='!역할설정', value='내래 역할을 준다우 !역할설정 [ID] [역할이름]', inline=False)
        embed.add_field(name='!하는일', value='내래 밥값을 하는지 보여준다우', inline=False)
        embed.add_field(name='!정보', value='인-포마이숀을 보여주겠디', inline=False)
        embed.add_field(name='!경고', value='경고를 주겠디 !경고 [ID]', inline=False)
        embed.add_field(name='!확인', value='경고 횟수를 확인해주겠디 !확인 [ID]', inline=False)
        embed.add_field(name='!리셋', value='경고 횟수를 초기화해주겠디 !리셋 [ID]', inline=False)
        embed.set_image(url="https://img3.yna.co.kr/photo/yna/YH/2011/12/23/PYH2011122304620001300_P2.jpg")

        await client.send_message(channel, embed=embed)

    if message.content.startswith("!정보"):
        channel = message.channel
        embed = discord.Embed(
            title='인-포마이숀',
            description='',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='이상이라우')
        embed.add_field(name='제작', value='제작자 : 시바 존나멋진 김민규(ㅈ한민국 기준 16세)\n 마지막 패치 : 갱신귀찮아서 안씀 ㅅㄱ\n 제작 이유 : 위대한 조선 민주주의 노휘빈 공화국의 입주자를 받기 위해서', inline=False)
        embed.add_field(name='제작된 날', value='서기 2019년 6월 15일 11시경', inline=False)
        embed.add_field(name='고위간부', value='수령 : 노휘빈\n군 : 김애용\n 원로 : 김민규\n 친족:대현', inline=False)
        embed.add_field(name='!하는일', value='내래 밥값을 하는지 보여준다우', inline=False)
        embed.set_image(url="https://img3.yna.co.kr/photo/yna/YH/2011/12/23/PYH2011122304620001300_P2.jpg")

        await client.send_message(channel, embed=embed)

    if message.content.startswith("!하는일"):
        channel = message.channel
        embed = discord.Embed(
            title='하는일',
            description='내래 밥값한다우',
            colour=discord.Colour.blue()
        )

        embed.set_footer(text='이상이라우')
        embed.add_field(name='린민 지급', value='신입들에게 린민역할을 지급한다우', inline=False)
        embed.add_field(name='봇', value='이건 모르겠다우 시바꺼', inline=False)
        embed.add_field(name='월북알림', value='월북, 탈북 정보를 알려준다우', inline=False)
        embed.set_image(url="https://img3.yna.co.kr/photo/yna/YH/2011/12/23/PYH2011122304620001300_P2.jpg")

        await client.send_message(channel, embed=embed)


    if message.content.startswith("!학습"):
        file = openpyxl.load_workbook('학습.xlsx')
        sheet = file.active
        learn = message.content.split(" ")
        for i in range(1, 301):
            if sheet["A" + str(i)].value == "-":
                sheet["A" + str(i)].value = learn[1]
                sheet["B" + str(i)].value = learn[2]
                await client.send_message(message.channel, "★ 현재 사용중인 데이터 저장용량 : " + str(i) + "/300 ★")
                break
        file.save("학습.xlsx")

    if message.content.startswith("!기억"):
        file = openpyxl.load_workbook("학습.xlsx")
        sheet = file.active
        memory = message.content.split(" ")
        for i in range(1, 51):
            if sheet["A" + str(i)].value == memory[1]:
                await client.send_message(message.channel, sheet["B" + str(i)].value)
                break
    if message.content.startswith("!역할설정"):
        role = ""
        rolename = message.content.split(" ")
        member = discord.utils.get(client.get_all_members(), id=rolename[1])
        for i in message.server.roles:
            if i.name == rolename[2]:
                role = i
                break
        await client.add_roles(member, role)

    if message.content.startswith("!경고"):
        memid = message.content.split(" ")
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        for i in range(1, 31):
            if str(sheet["A" + str(i)].value) == str(memid[1]):
                sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 1
                break
            if str(sheet["A" + str(i)].value) == "-":
                sheet["A" + str(i)].value = str(memid[1])
                sheet["B" + str(i)].value = 1
                break
        file.save("경고.xlsx")
        await client.send_message(message.channel, "경고를 받았디 주의하기 바란다 현재 누적경고 :" + str(sheet["B" + str(i)].value)+ "회")

    if message.content.startswith("!확인"):
        memid = message.content.split(" ")
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        for i in range(1, 31):
            for i in range(1, 31):
                if str(sheet["A" + str(i)].value) == str(memid[1]):
                    sheet["B" + str(i)].value = int(sheet["B" + str(i)].value) + 0
                    break
        await client.send_message(message.channel, "누적 경고횟수는" + str(sheet["B" + str(i)].value) + "회")

    if message.content.startswith("!리셋"):
        memid = message.content.split(" ")
        file = openpyxl.load_workbook("경고.xlsx")
        sheet = file.active
        for i in range(1, 31):
            if str(sheet["A" + str(i)].value) == str(memid[1]):
                sheet["B" + str(i)].value = 0
                break
        file.save("경고.xlsx")
        await client.send_message(message.channel, "초기화 완료디 누적경고횟수는" + str(sheet["B" + str(i)].value) + "회")




client.run("NDI0Nzc3MTEwOTE4Mzk3OTU1.XQUjQw.lQZSAtZQI-P_3Ffcf2QQ-cW6KXQ")
