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
        
    if message.content.startswith('!실시간검색어') or message.content.startswith('!실검'):
        url = "https://www.naver.com/"
        html = urllib.request.urlopen(url)

        bsObj = bs4.BeautifulSoup(html, "html.parser")
        realTimeSerach1 = bsObj.find('div', {'class': 'ah_roll_area PM_CL_realtimeKeyword_rolling'})
        realTimeSerach2 = realTimeSerach1.find('ul', {'class': 'ah_l'})
        realTimeSerach3 = realTimeSerach2.find_all('li')

        embed = discord.Embed(
            title='네이버 실시간 검색어',
            description='실시간검색어',
            colour=discord.Colour.green()
        )
        for i in range(0, 20):
            realTimeSerach4 = realTimeSerach3[i]
            realTimeSerach5 = realTimeSerach4.find('span', {'class': 'ah_k'})
            realTimeSerach = realTimeSerach5.text.replace(' ', '')
            realURL = 'https://search.naver.com/search.naver?ie=utf8&query=' + realTimeSerach
            print(realTimeSerach)
            embed.add_field(name=str(i + 1) + '위', value='\n' + '[%s](<%s>)' % (realTimeSerach, realURL),
                            inline=False)  # [텍스트](<링크>) 형식으로 적으면 텍스트 하이퍼링크 만들어집니다

        await client.send_message(message.channel, embed=embed)

    if message.content.startswith('!영화순위'):
        # http://ticket2.movie.daum.net/movie/movieranklist.aspx
        i1 = 0  # 랭킹 string값
        embed = discord.Embed(
            title="영화순위",
            description="영화순위입니다.",
            colour=discord.Color.red()
        )
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'http://ticket2.movie.daum.net/movie/movieranklist.aspx'
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        moviechartBase = bsObj.find('div', {'class': 'main_detail'})
        moviechart1 = moviechartBase.find('ul', {'class': 'list_boxthumb'})
        moviechart2 = moviechart1.find_all('li')

        for i in range(0, 20):
            i1 = i1 + 1
            stri1 = str(i1)  # i1은 영화랭킹을 나타내는데 사용됩니다
            print()
            print(i)
            print()
            moviechartLi1 = moviechart2[i]  # ------------------------- 1등랭킹 영화---------------------------
            moviechartLi1Div = moviechartLi1.find('div', {'class': 'desc_boxthumb'})  # 영화박스 나타내는 Div
            moviechartLi1MovieName1 = moviechartLi1Div.find('strong', {'class': 'tit_join'})
            moviechartLi1MovieName = moviechartLi1MovieName1.text.strip()  # 영화 제목
            print(moviechartLi1MovieName)

            moviechartLi1Ratting1 = moviechartLi1Div.find('div', {'class': 'raking_grade'})
            moviechartLi1Ratting2 = moviechartLi1Ratting1.find('em', {'class': 'emph_grade'})
            moviechartLi1Ratting = moviechartLi1Ratting2.text.strip()  # 영화 평점
            print(moviechartLi1Ratting)

            moviechartLi1openDay1 = moviechartLi1Div.find('dl', {'class': 'list_state'})
            moviechartLi1openDay2 = moviechartLi1openDay1.find_all('dd')  # 개봉날짜, 예매율 두개포함한 dd임
            moviechartLi1openDay3 = moviechartLi1openDay2[0]
            moviechartLi1Yerating1 = moviechartLi1openDay2[1]
            moviechartLi1openDay = moviechartLi1openDay3.text.strip()  # 개봉날짜
            print(moviechartLi1openDay)
            moviechartLi1Yerating = moviechartLi1Yerating1.text.strip()  # 예매율 ,랭킹변동
            print(moviechartLi1Yerating)  # ------------------------- 1등랭킹 영화---------------------------
            print()
            embed.add_field(name='---------------랭킹' + stri1 + '위---------------',
                            value='\n영화제목 : ' + moviechartLi1MovieName + '\n영화평점 : ' + moviechartLi1Ratting + '점' + '\n개봉날짜 : ' + moviechartLi1openDay + '\n예매율,랭킹변동 : ' + moviechartLi1Yerating,
                            inline=False)  # 영화랭킹

        await client.send_message(message.channel, embed=embed)





client.run("NDI0Nzc3MTEwOTE4Mzk3OTU1.XQUjQw.lQZSAtZQI-P_3Ffcf2QQ-cW6KXQ")
