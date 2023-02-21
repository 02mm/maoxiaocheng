from nonebot import on_command,CommandSession
import pymysql
import re

__plugin_name__ = '云顶工作簿'
__plugin_usage__ = r"""
添加功能：
参数-> 1.名称 2.链接
唤醒词-> 添加云顶工作簿
根据引导输入参数即可！
删除功能：
参数-> 名称
唤醒词-> 删除云顶工作簿
根据引导输入参数即可！
查询功能：
命令-> 查看云顶工作簿 / 查看云顶工作簿-名称
eg: 云顶工作簿查看-云麓签到系统
"""

#查看期数，七期不允许使用
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



@on_command('yd_work',aliases={'添加云顶工作簿'})
async def go_work(session:CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        name = await session.aget(prompt='请输入工作簿名称（不可修改，输错联系管理员！）')
        link = await session.aget(prompt='请输入链接（不可修改，输错联系管理员！）')
        # 验证数据合法性
        if len(name) > 50 or len(link) > 1000:
            await session.send('名称或链接太长')
        else:
            db = pymysql.connect(host='43.143.194.132',
                                 port=3306,
                                 user='maoxiaocheng',
                                 passwd='yzc200212.',
                                 database='maoxiaocheng')

            cursor = db.cursor()
            sql = f'insert into yd_work (work_name,work_link) value ("{name.strip()}","{link}")'
            cursor.execute(sql)
            db.commit()
            db.close()
            await session.send('添加成功！')
            # 发送通知到群里
            await session.bot.send_group_msg(group_id=619200432, message=f'工作簿更新通知！\n名称：{name}\n链接：{link}\n输入：查看云顶工作簿 进行查看')

@on_command('look_yd_works',aliases={'查看云顶工作簿','查看云顶工作薄'})
async def get_all_work(session:CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        db = pymysql.connect(host='43.143.194.132',
                             port=3306,
                             user='maoxiaocheng',
                             passwd='yzc200212.',
                             database='maoxiaocheng')

        cursor = db.cursor()
        sql = 'select * from yd_work'
        cursor.execute(sql)
        works = cursor.fetchall()
        response = ''
        message = session.event.get('message')
        # print(message)
        # print(session.current_arg_text)
        # print(type(session.current_arg_text))
        if '薄' in str(message):
            # print('okok')
            response += '是工作簿，不是工作薄，下次记住哦！\n'
        for p in works:
            response += p[0]
            response += '：'
            response += p[1]
            response += '\n'
        await session.send(response)

@on_command('look_yd_work',patterns={'查看云顶工作簿-','查看云顶工作薄-'})
async def get_work(session:CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        db = pymysql.connect(host='43.143.194.132',
                             port=3306,
                             user='maoxiaocheng',
                             passwd='yzc200212.',
                             database='maoxiaocheng')

        cursor = db.cursor()
        message = session.event.get('message')
        # print(message)
        # print(type(message))
        # print('\n\n\n')
        work_name = re.findall('-(.*)',str(message))
        sql = f'select work_link from yd_work where work_name = "{work_name[0]}"'
        cursor.execute(sql)
        work_link = cursor.fetchall()
        response = ''
        if '薄' in str(message):
            response += '是工作簿，不是工作薄，下次记住哦！\n'
        response += work_name[0]
        response += '：'
        response += work_link[0][0]
        # group = session.event.get('g')
        await session.send(response)

@on_command('drop_yd_work',aliases={'删除云顶工作簿','删除云顶工作薄'})
async def drop_work(session:CommandSession):
    qq_number = session.event.get('user_id')
    if check(qq_number) == 0:
        await session.send('只有学长学姐才可以使用哦！')
    else:
        work_name = await session.aget(prompt='请输入工作簿名称')
        db = pymysql.connect(host='43.143.194.132',
                             port=3306,
                             user='maoxiaocheng',
                             passwd='yzc200212.',
                             database='maoxiaocheng')

        cursor = db.cursor()
        sql = f'select * from yd_work where work_name = "{work_name.strip()}"'
        cursor.execute(sql)
        res = cursor.fetchall()
        if res == ():
            await session.send('该工作簿不存在')
        else:
            sql = f'delete from yd_work where work_name = "{work_name}"'
            cursor.execute(sql)
            db.commit()
            db.close()
            await session.send('删除成功！')