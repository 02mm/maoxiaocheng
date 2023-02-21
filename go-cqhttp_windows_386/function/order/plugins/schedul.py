from apscheduler.schedulers.blocking import BlockingScheduler
from nonebot import get_bot,scheduler
import requests
import datetime
import pymysql
import time


#每天晚上8点发送天气预报
@scheduler.scheduled_job('cron',year = '*',month = '*',day = '*',hour = 20)
async def weather():
    url = 'https://restapi.amap.com/v3/weather/weatherInfo?key=f69823a7011d73cb2b2778391a3490f0&city=140702&extensions=all&output=JSON'
    response = requests.get(url)
    result = response.json()
    weatherr = result['forecasts'][0]['casts'][1]
    print(weatherr)
    print(type(weatherr))
    res = f'小毛天气预报：\n明日周{weatherr["week"]},{weatherr["date"]}\n白天{weatherr["dayweather"]},温度{weatherr["daytemp"]}℃,风向' \
          f'{weatherr["daywind"]},风力{weatherr["daypower"]}。\n晚上{weatherr["nightweather"]},温度{weatherr["nighttemp"]}℃,风向' \
          f'{weatherr["nightwind"]},风力{weatherr["nightpower"]}。\n宝子们要注意温度变化，增减衣物哦！'
    if '雨' in weatherr['dayweather'] or '雨' in weatherr['nightweather']:
        res += '\n明日可能下雨，带伞出行以防万一哦！'
    bot = get_bot()
    # 七期学员群
    await bot.send_group_msg(group_id=917513084,message=res)
    time.sleep(3)
    # 六期极客团
    await bot.send_group_msg(group_id=619200432,message=res)
    time.sleep(3)
    # 七期人工智能方向
    await bot.send_group_msg(group_id=799256556,message=res)
    time.sleep(3)
    # 七期全栈方向
    await bot.send_group_msg(group_id=807069181, message=res)
    time.sleep(3)
    # 七期Java方向
    await bot.send_group_msg(group_id=807510253, message=res)
    time.sleep(3)
    # 七期CPU&OS方向
    await bot.send_group_msg(group_id=812976742, message=res)
    time.sleep(3)
    # 七期设计方向
    await bot.send_group_msg(group_id=750056963, message=res)
    time.sleep(3)
    # 七期秘书处方向
    await bot.send_group_msg(group_id=201159730, message=res)
    time.sleep(3)
    # me
    await bot.send_private_msg(user_id=2910711781, message='主人，天气预报推送完毕，请过目！')


#研学开始时发送请假和调研学人员信息
@scheduler.scheduled_job('cron',day_of_week = 'mon-fri',hour='7-17')
async def send_leave_adjust():
    date = datetime.datetime.now()
    month = date.month
    day = date.day
    hour = date.hour
    cla = {8:1,10:2,15:3,16:4}
    if hour/2 == 1 or hour == 12:
        print('pass')
    else:
        Date = f'{month}月{day}日第{cla[hour]}大节'
        db = pymysql.connect(host='localhost',
                             port=3306,
                             user='maoxiaocheng',
                             passwd='D7eMTbfeATXMh8xr',
                             database='maoxiaocheng')

        cursor = db.cursor()
        sql = f'select * from leave_from where time = "{Date}"'
        cursor.execute(sql)
        res = cursor.fetchall()
        sql = f'select * from adjust_class where i_time = "{Date}"'
        cursor.execute(sql)
        res_2 = cursor.fetchall()
        ai = '人工智能：'
        AI = '人工智能：'
        java = 'Java：'
        JAVA = 'Java：'
        html = '全栈：'
        HTML = '全栈：'
        cpu = 'CPU&OS：'
        CPU = 'CPU&OS：'
        design = '设计：'
        DESIGN = '设计：'
        serce = '秘书处：'
        SERCE = '秘书处：'
        for p in res:
            if p[0] == '人工智能':
                ai += f'{p[1]},'
            elif p[0] == 'Java':
                java += f'{p[1]},'
            elif p[0] == '秘书处':
                serce += f'{p[1]},'
            elif p[0] == 'CPU&OS':
                cpu += f'{p[1]},'
            elif p[0] == '设计':
                design += f'{p[1]},'
            else:
                html += f'{p[1]},'
        link = '更多信息请点击{http:}'
        contect = f'{Date}请假人员：\n'
        contect += f'{ai}\n'
        contect += f'{java}\n'
        contect += f'{html}\n'
        contect += f'{cpu}\n'
        contect += f'{design}\n'
        contect += f'{serce}\n'
        contect += link
        for p in res_2:
            if p[0] == '人工智能':
                AI += f'{p[1]},'
            elif p[0] == 'Java':
                JAVA += f'{p[1]},'
            elif p[0] == '秘书处':
                SERCE += f'{p[1]},'
            elif p[0] == 'CPU&OS':
                CPU += f'{p[1]},'
            elif p[0] == '设计':
                DESIGN += f'{p[1]},'
            else:
                HTML += f'{p[1]},'
        contect += '\n调研学人员：\n'
        contect += f'{AI}\n'
        contect += f'{JAVA}\n'
        contect += f'{HTML}\n'
        contect += f'{CPU}\n'
        contect += f'{DESIGN}\n'
        contect += f'{SERCE}\n'
        contect += '更多信息请点击{http:}'
        bot = get_bot()
        # 六期极客团
        await bot.send_group_msg(group_id=619200432,message=contect)
        time.sleep(3)
        await bot.send_private_msg(user_id=2910711781, message='主人，请假和调研学信息推送完毕，请过目！')

# 每周日晚上6点清理数据库
@scheduler.scheduled_job('cron',day_of_week = 'sun',hour = '18')
async def clear_data():
    db = pymysql.connect(host='localhost',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='D7eMTbfeATXMh8xr',
                         database='maoxiaocheng')

    cursor = db.cursor()
    cursor.execute('truncate table leave_from')
    db.commit()
    cursor.execute('truncate table adjust_class')
    db.commit()
    db.close()
    bot = get_bot()
    await bot.send_private_msg(user_id=2910711781, message='主人，数据库清理完毕啦！')