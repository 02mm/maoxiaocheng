from .get_translation import get_translation
from nonebot import on_natural_language, NLPSession


__plugin_name__ = '小毛翻译'
__plugin_usage__ = r"""
多语言翻译：唤醒词为'翻译：'或'翻译:'
例：翻译：你是我的白月光，我是你的地上霜
"""

@on_natural_language(keywords={'翻译：','翻译:'})
async def translation(session: NLPSession):
    # 取得消息的内容，并且去掉首尾的空白符
    words = session.msg_text.strip()
    # 去掉翻译：
    new_words = words[3:]
    translation = await get_translation(new_words)
    # 向用户发送译文
    await session.send(translation)

