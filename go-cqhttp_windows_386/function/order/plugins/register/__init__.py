from nonebot import on_command,CommandSession
import pymysql

__plugin_name__ = '请假系统-信息登记及修改'
__plugin_usage__ = r"""
命令：请假信息登记
返回登记成功或修改成功即可！
"""


# 获取qq号和对应的名字，如果进行修改，删除另一条，数据库中每人的qq号只存在一个，防止非法操作，减少损失
@on_command('info_register',aliases={'请假信息登记'})
async def infor(session: CommandSession):
    msg_type = session.event.get('message_type')
    if msg_type == 'group':
        await session.send('请私聊我进行信息登记哦！')
    else:
        infor = await session.aget(prompt='请输入你的姓名，请勿输入他人名字，发现后会有相应处罚哦！如果不小心输错，请重新登记。')
        db = pymysql.connect(host='43.143.194.132',
                             port=3306,
                             user='maoxiaocheng',
                             passwd='yzc200212.',
                             database='maoxiaocheng')

        cursor = db.cursor()
        sql = f'SELECT direction FROM yunzi_seven WHERE name="{infor}";'
        cursor.execute(sql)
        flag_name = cursor.fetchall()
        qq_number = session.event.get('user_id')
        sql = f'SELECT direction FROM yunzi_seven WHERE qq_number="{qq_number}";'
        cursor.execute(sql)
        flag_qq = cursor.fetchall()
        if flag_name == ():
            await session.send('七期学院表中没有你的名字，请联系学长学姐！')
        elif flag_qq != ():
            sql = f'UPDATE yunzi_seven set qq_number = "" WHERE qq_number = "{qq_number}";'
            cursor.execute(sql)
            db.commit()
            sql = f'UPDATE yunzi_seven set qq_number = "{qq_number}" WHERE `name` = "{infor}";'
            cursor.execute(sql)
            db.commit()
            db.close()
            await session.send('信息修改成功！')
        else:
            sql = f'UPDATE yunzi_seven set qq_number = "{qq_number}" WHERE `name` = "{infor}";'
            cursor.execute(sql)
            db.commit()
            db.close()
            await session.send('信息登记成功！')

