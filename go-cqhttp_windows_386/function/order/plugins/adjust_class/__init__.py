from nonebot import on_natural_language, NLPSession,on_command,CommandSession
import re
import pymysql
from .adjust_cla import adjust_cla

__plugin_name__ = '调研学系统'
__plugin_usage__ = r"""
唤醒词：'调研学：'或'调研学:'
调研学格式(
调研学：
调前-11月16日第3大节
调后-11月16日第4大节s
调整理由-吃饭睡觉打豆豆！)
取消研学调整命令：取消研学调整
模板获取命名：调研学模板
初次使用需要进行信息登记！
"""
@on_command('adjust_template',aliases={'调研学模板','调研学模版'})
async def leave_template(session: CommandSession):
    template = '调研学：\n调前-?月?日第?大节\n调后-?月?日第?大节\n调整理由-吃饭睡觉打豆豆！'
    await session.send(template)

@on_command('cancel_leave',aliases='取消研学调整')
async def cancel_adjust(session: CommandSession):
    time = await session.aget(prompt='请输入原研学时间，注意格式，eg：11月17日第3大节')
    qq_number = session.event.get('user_id')
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')
    cursor = db.cursor()
    sql = f'SELECT q.i_time,q.name,p.direction FROM yunzi_seven p,adjust_class q WHERE p.`name` = q.`name` AND p.qq_number = "{qq_number}";'
    cursor.execute(sql)
    res = cursor.fetchall()
    flag = 0
    for i in res:
        if time in i[0]:
            sql = f'delete from adjust_class where name = "{res[0][1]}" and i_time = "{time}";'
            cursor.execute(sql)
            db.commit()
            db.close()
            flag = 1
            break
    if flag == 1:
        await session.send('取消研学调整成功！')
        msg = f'{res[0][1]}取消了原研学时间为{time}的研学调整！'
        if res[0][2] == '设计':
            await session.bot.send_group_msg(group_id=601428225, message=msg)
        elif res[0][2] == '人工智能':
            await session.bot.send_group_msg(group_id=426338779, message=msg)
        else:
            await session.bot.send_group_msg(group_id=619200432, message=msg)
    else:
        await session.send('研学未调整或未安排研学或已经请假！')


@on_command('adjust_class',patterns={'调研学：','调研学:'})
async def leave(session: CommandSession):
    # 检查是否信息登记
    qq_number = session.event.get('user_id')
    # print(qq_number)
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='Dyzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'select * from yunzi_seven where qq_number = "{qq_number}"'
    cursor.execute(sql)
    res = cursor.fetchall()
    if res == ():
        await session.send('请输入 请假信息登记 进行信息登记后再请假！')
    else:
        content = session.current_arg_text
        mess_type = session.event.get('message_type')
        # 判断消息类型，若是群聊则不可调研学
        if mess_type == 'group':
            await session.send('请私聊我调研学哦！')
        else:
            # 标志数据格式的0 1
            flag = 0
            msg = []
            try:
            # msg.append(re.findall('方向-(.*?)\n', content, re.M))
            # msg.append(re.findall('姓名-(\w+)\n', content, re.M))
                msg.append(res[0][1])
                msg.append(res[0][0])
                msg.append(re.findall('调前-(\w+)\n',content,re.M)[0])
                msg.append(re.findall('调后-(\w+)\n', content, re.M)[0])
                msg.append(re.findall('调整理由-(.*)', content,re.M)[0])
            except:
                flag = 1
            for i in msg:
                if i == [''] or i == []:
                    flag = 1
            # 检查调研学是否在同一天
            print(msg)
            if re.findall('(\d+)月',msg[2])[0] != re.findall('(\d+)月',msg[3])[0]:
                await session.send('只允许调到当天哦，你也可以请假呢！')
            elif re.findall('月(\d+)日',msg[2])[0] != re.findall('月(\d+)日',msg[3])[0]:
                await session.send('只允许调到当天哦，你也可以请假呢！')
            else:
                if flag == 1:
                    await session.send('请假格式错误！')
                else:
                    response = f'调研学：\n方向-{res[0][1]}\n姓名-{res[0][0]}\n请前-{msg[2]}\n调后-{msg[3]}\n调整理由-{msg[4]}'
                    result = adjust_cla(msg)
                    response += f'\n本周调研学次数-{week_times(res[0][0])}'
                    if result == 0:
                        bot = session.bot
                        # 将消息同步到群里
                        if res[0][1] == '设计':
                            await bot.send_group_msg(group_id=601428225, message=response)
                        elif res[0][1] == '人工智能':
                            await bot.send_group_msg(group_id=426338779, message=response)
                        else:
                            await bot.send_group_msg(group_id=619200432, message=response)
                        await session.send('调整成功！')
                    elif result == 1:
                        await session.send('七期学员没有你的名字，请联系学长学姐~')
                    elif result == 2:
                        await session.send('方向选择错误！')
                    elif result == 3:
                        await session.send('格式不规范，请输入 调研学模板 查看格式！')
                    elif result == 4:
                        await session.send('日期不合法，注意要使用小写数字哦！')
                    elif result == 5:
                        await session.send('时间已经过了哦！请联系学长学姐')
                    elif result == 6:
                        await session.send('你已经调过研学啦，可以取消研学调整重新调整哦！')




# 查询本周调研学次数
def week_times(name):
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='	maoxiaocheng',
                         passwd='yzc200212.',
                         database='	maoxiaocheng')

    cursor = db.cursor()
    sql = f'select * from adjust_class where name = "{name}"'
    cursor.execute(sql)
    times = len(cursor.fetchall())
    return times
