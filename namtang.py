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

    await client.change_presence(game=discord.Game(name="위대한 수령동지를 위하여", type=1))

@client.event
async def on_member_join(member):
    role = ""
    for i in member.server.roles:
        if i.name == "린민":
            role = i
            break
    await client.add_roles(member, role)

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
        embed.add_field(name='고위간부', value='수령 : 노휘빈\n군 : 김애용\n 원로 : 김민규\n친족 : 대현', inline=False)
        embed.add_field(name='추가사항', value='빠끄!', inline=False)

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





client.run("NDI0Nzc3MTEwOTE4Mzk3OTU1.XQUjQw.lQZSAtZQI-P_3Ffcf2QQ-cW6KXQ")
