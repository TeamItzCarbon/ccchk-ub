from ubb import Ubot
from telethon import version, events
from platform import python_version



@Ubot.on(events.NewMessage(pattern=r'\.mummy'))
async def amialive(event):
    me = await Ubot.get_me()
    await event.edit(f'''
**Teri Mummy Meri Hoja!**
**Telethon version:** `{version.__version__}`
**Python version:** `{python_version()}`
**Master:** [{me.first_name}](tg://user?id={me.id})
''') 
    
    
@Ubot.on(events.NewMessage(pattern=r'\.help'))
async def helper(event):
    await event.edit(f'''
**Dont Fear help is here!**
• .mummy <chk ubot is up or not>.
• .st <cc|mm|yy|csc> to chk cards.
• .paste <to unpack openbullet/storm configs or paste codes> .
• .tr <translate replied msg> to eng ex reply .tr en
• .ip <chk ip fraud score>
• .bin <chk bininfo>
• .eval <py codes>
''')
