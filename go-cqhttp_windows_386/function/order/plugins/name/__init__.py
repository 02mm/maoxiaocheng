from nonebot import on_natural_language, NLPSession, IntentCommand

@on_natural_language(keywords={'名字','你叫什么','你是谁！'})
async def my_name(session: NLPSession):
    await session.send('我叫毛小成，你可以叫我小毛呢~')