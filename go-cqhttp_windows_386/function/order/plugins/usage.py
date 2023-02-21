import nonebot
from nonebot import on_command, CommandSession


@on_command('usage', patterns=['用户手册', '使用帮助', '使用方法'])
async def _(session: CommandSession):
    # 获取设置了名称的插件列表
    plugins = list(filter(lambda p: p.name, nonebot.get_loaded_plugins()))

    mune = '小毛现在支持的功能有：\n\n'
    res = []
    for p in range(len(plugins)):
        row = []
        row.append(p+1)
        row.append(plugins[p].name)
        row.append(plugins[p].usage)
        res.append(row)
    for p in res:
        mune += str(p[0])
        mune += ':'
        mune += p[1]
        mune += '\n'

    mune += '更多功能敬请开发！'
    await session.send(mune)
    id = await session.aget(prompt='请输入你想查询功能前的数字！')
    fun = res[int(id)-1][2]
    await session.send(fun)
    while(1):
        choice = await session.aget(prompt='输入0结束查询，继续查询输入功能前的数字！')
        if int(choice) == 0:
            break
        fun = res[int(choice)-1][2]
        await session.send(fun)
    await session.send('退出用户手册')
