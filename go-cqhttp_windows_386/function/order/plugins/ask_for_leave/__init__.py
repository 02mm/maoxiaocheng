from nonebot import on_natural_language, NLPSession,on_command,CommandSession
import re
from .get_leave import get_leave
import pymysql

__plugin_name__ = '请假系统'
__plugin_usage__ = r"""
唤醒词：'请假：'或'请假:'
请假格式(
请假：
请假时间-11月16日第3大节
请假理由-我妈喊我回家吃饭！)
模板获取命名：请假模板
取消请假命令：取消请假
初次使用需要进行信息登记！
"""

@on_command('leave_template',aliases={'请假模板','请假模版'})
async def leave_template(session: CommandSession):
    template = '请假：\n请假时间-?月?日第?大节\n请假理由-我妈喊我回家吃饭'
    await session.send(template)

@on_command('cancel_leave',aliases='取消请假')
async def cancel_leave(session: CommandSession):
    time = await session.aget(prompt='请输入请假时间，注意格式，使用小写数字，eg：11月17日第3大节')
    qq_number = session.event.get('user_id')
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'SELECT q.time,q.name,p.direction FROM yunzi_seven p,leave_from q WHERE p.`name` = q.`name` AND p.qq_number = "{qq_number}";'
    cursor.execute(sql)
    res = cursor.fetchall()
    flag = 0
    for i in res:
        if time in i[0]:
            sql = f'delete from leave_from where name = "{res[0][1]}" and time = "{time}";'
            cursor.execute(sql)
            db.commit()
            db.close()
            flag = 1
            break
    if flag == 1:
        await session.send('取消请假成功！')
        msg = f'{res[0][1]}取消了{time}的请假！'
        if res[0][2] == '设计':
            await session.bot.send_group_msg(group_id=601428225, message=msg)
        elif res[0][2] == '人工智能':
            await session.bot.send_group_msg(group_id=426338779, message=msg)
        else:
            await session.bot.send_group_msg(group_id=619200432, message=msg)
    else:
        await session.send('研学未请假或未安排研学！')



@on_command('ask_for_leave',patterns={'请假：','请假:'})
# @on_natural_language(keywords={'请假：','请假:'})
async def leave(session: CommandSession):
    # 检查是否信息登记
    qq_number = session.event.get('user_id')
    # print(qq_number)
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
        await session.send('请输入 请假信息登记 进行信息登记后再请假！')
    else:
        content = session.current_arg_text
        # print(content)
        # print('\n\n\n\n')
        mess_type = session.event.get('message_type')
        #判断消息类型，若是群聊则不可请假
        if mess_type == 'group':
            await session.send('请私聊我请假哦！')
        else:
            # 标志数据格式的0 1
            flag = 0
            msg = []
            try:
                msg.append(res[0][1])
                msg.append(res[0][0])
                msg.append(re.findall('请假时间-(\w+)\n', content, re.M)[0])
                msg.append(re.findall('请假理由-(.*)', content,re.M)[0])
            except:
                flag = 1
            print(msg)
            for i in msg:
                if i == [''] or i == []:
                    flag = 1
            if flag == 1:
                await session.send('请假格式错误！')
            else:
                response = f'请假：\n方向-{res[0][1]}\n姓名-{res[0][0]}\n请假时间-{msg[2]}\n请假理由-{msg[3]}'
                result = get_leave(msg)
                response += f'\n本周请假次数-{week_times(res[0][0])}'
                if result == 0:
                    bot = session.bot
                    # 六期极客团
                    if res[0][1] == '设计':
                        await bot.send_group_msg(group_id=601428225,message=response)
                    elif res[0][1] == '人工智能':
                        await bot.send_group_msg(group_id=426338779, message=response)
                    else:
                        await bot.send_group_msg(group_id=619200432, message=response)

                    await session.send('请假成功！')
                elif result == 1:
                    await session.send('七期学员没有你的名字，请联系学长学姐~')
                elif result == 2:
                    await session.send('方向选择错误！')
                elif result == 3:
                    await session.send('请假日期不合法！')
                elif result == 4:
                    await session.send('请假日期不合法，注意要使用小写数字哦！')
                elif result == 5:
                    await session.send('请假时间已经过了哦！请联系学长学姐')
                elif result == 6:
                    await session.send('你已经请过假啦！')


# 查询本周请假次数
def week_times(name):
    db = pymysql.connect(host='43.143.194.132',
                         port=3306,
                         user='maoxiaocheng',
                         passwd='yzc200212.',
                         database='maoxiaocheng')

    cursor = db.cursor()
    sql = f'select * from leave_from where name = "{name}"'
    cursor.execute(sql)
    times = len(cursor.fetchall())
    return times



