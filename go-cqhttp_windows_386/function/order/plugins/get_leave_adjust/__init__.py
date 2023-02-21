from nonebot import on_command, CommandSession, on_natural_language, NLPSession
import datetime
import re
import pymysql

__plugin_name__ = '查看当前请假学人员和调研学人员'
__plugin_usage__ = r'''
命名：查看请假人员：第？节
返回：1.当天第？节请假人员，2.今明两天天所有请假人员（链接）
命令：查看调研学人员：第？节
返回：1，当天第？节调研学人员，2.调研学表（链接）
'''


# 查看期数，七期不允许使用
def check(qq_number):
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'select * from yunzi_seven where qq_number = "{qq_number}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    if res == ():
        return 1
    else:
        return 0


@on_command('get_leaves', patterns={'查看请假人员：', '查看请假人员:'})
async def get_leaves(session: CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        mes = session.current_arg_text.strip()
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        cla = re.findall('(\d+)', mes)
        if cla == []:
            await session.send('格式错误，注意使用小写数字！')
        else:
            date = f'{month}月{day}日第{cla[0]}大节'
            db = pymysql.connect(
                host='43.143.194.132',
                port=3306,
                user='maoxiaocheng',
                passwd='yzc200212.',
                database='maoxiaocheng'
            )
            cursor = db.cursor()
            sql = f'select * from leave_from where time = "{date}"'
            cursor.execute(sql)
            response = cursor.fetchall()
            ai = '人工智能：'
            java = 'Java：'
            html = '全栈：'
            cpu = 'CPU&OS：'
            design = '设计：'
            serce = '秘书处：'
            for p in response:
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
            link = '更多信息请点击->http://43.143.194.132:5000/'
            contect = f'{date}请假人员：\n'
            contect += f'{ai}\n'
            contect += f'{java}\n'
            contect += f'{html}\n'
            contect += f'{cpu}\n'
            contect += f'{design}\n'
            contect += f'{serce}\n'
            contect += link
            await session.send(contect)


@on_command('get_adjusts', patterns={'查看调研学人员：', '查看调研学人员:'})
async def get_adjust(session: CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        mes = session.current_arg_text.strip()
        month = datetime.datetime.now().month
        day = datetime.datetime.now().day
        cla = re.findall('(\d+)', mes)
        if cla == []:
            await session.send('格式错误，注意使用小写数字！')
        else:
            date = f'{month}月{day}日第{cla[0]}大节'
            db = pymysql.connect(
                host='43.143.194.132',
                port=3306,
                user='maoxiaocheng',
                passwd='yzc200212.',
                database='maoxiaocheng'
            )
            cursor = db.cursor()
            sql = f'select * from adjust_class where i_time = "{date}"'
            cursor.execute(sql)
            response = cursor.fetchall()
            ai = '人工智能：'
            java = 'Java：'
            html = '全栈：'
            cpu = 'CPU&OS：'
            design = '设计：'
            serce = '秘书处：'
            for p in response:
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

            link = '更多信息请点击->http://43.143.194.132:5000/adjust'
            contect = f'{date}调研学人员：\n'
            contect += f'{ai}\n'
            contect += f'{java}\n'
            contect += f'{html}\n'
            contect += f'{cpu}\n'
            contect += f'{design}\n'
            contect += f'{serce}\n'
            contect += link
            await session.send(contect)
