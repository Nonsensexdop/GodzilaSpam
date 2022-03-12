async def gifspam(e, smex):
    try:
        await e.client(
            functions.messages.SaveGifRequest(
                id=types.InputDocument(
                    id=sandy.media.document.id,
                    access_hash=smex.media.document.access_hash,
                    file_reference=smex.media.document.file_reference,
                ),
                unsave=True,
            )
        )
    except Exception:
        pass

import asyncio
import base64
import os
from telethon import events
from telethon import functions, types
from telethon.tl.functions.messages import ImportChatInviteRequest as Get
from SpamX import omfo, omfo2, omfo3, omfo4, omfo5 , omfo6, omfo7, omfo8, omfo9, omfo10, omfo11, omfo12, omfo13, omfo14, omfo15, omfo16, omfo17, omfo18, omfo19, omfo20, omfo21, omfo22, omfo23, omfo24, omfo25, omfo26, omfo27, omfo28, omfo29, omfo30, omfo31, omfo32, omfo33, omfo34, omfo35, omfo36, omfo37, omfo38, omfo39, omfo40, SUDO_USERS
from .. import CMD_HNDLR as hl
from resources.data import SpamX


# spam

@omfo.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo2.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo3.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo4.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo5.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo6.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo7.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo8.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo9.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo10.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo11.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo12.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo13.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo14.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo15.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo16.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo17.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo18.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo19.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
@omfo20.on(events.NewMessage(incoming=True, pattern=r"\%sspam(?: |$)(.*)" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗦𝗽𝗮𝗺\n\nCommand:\n\n.spam <count> <message to spam>\n\n.spam <count> <reply to a message>\n\nCount must be a integer."
    error = "Spam Module can only be used till 100 count. For bigger spams use BigSpam."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        SpamX = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(SpamX) == 2:
            message = str(SpamX[1])
            counter = int(SpamX[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        elif e.reply_to_msg_id and smex.media:
            counter = int(SpamX[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            for _ in range(counter):
                smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                await gifspam(e, smex)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(SpamX[0])
            if counter > 100:
                return await e.reply(error, parse_mode=None, link_preview=None)
            await asyncio.wait([e.respond(message) for i in range(counter)])
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)


#bigspam

@omfo.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo2.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo3.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo4.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo5.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo6.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo7.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo8.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo9.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo10.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo11.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo12.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo13.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo14.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo15.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo16.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo17.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo18.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo19.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
@omfo20.on(events.NewMessage(incoming=True, pattern=r"\%sbigspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗕𝗶𝗴𝗦𝗽𝗮𝗺\n\nCommand:\n\n.bigspam <count> <message to spam>\n\n.bigspam <count> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        spamx = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 1)
        smex = await e.get_reply_message()
        if len(spamx) == 2:
            message = str(spamx[1])
            counter = int(spamx[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.1)
        elif e.reply_to_msg_id and smex.media:  
            counter = int(spamx[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex) 
                await asyncio.sleep(0.1)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(spamx[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )

#delayspam

@omfo.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo2.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo3.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo4.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo5.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo6.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo7.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo8.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo9.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo10.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo11.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo12.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo13.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo14.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo15.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo16.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo17.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo18.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo19.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
@omfo20.on(events.NewMessage(incoming=True, pattern=r"\%sdelayspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = 𝗗𝗲𝗹𝗮𝘆𝗦𝗽𝗮𝗺\n\nCommand:\n\n.delayspam <sleep time> <count> <message to spam>\n\n.delayspam <sleep time> <count> <reply to a message>\n\nCount and Sleeptime must be a integer."     
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None)
        smex = await e.get_reply_message()
        SpamX = "".join(e.text.split(maxsplit=1)[1:]).split(" ", 2)
        SpamXsexy = SpamX[1:]
        if len(SpamXsexy) == 2:
            message = str(SpamXsexy[1])
            counter = int(SpamXsexy[0])
            sleeptime = float(SpamX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    if e.reply_to_msg_id:
                        await smex.reply(message)
                    else:
                        await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.media:
            counter = int(SpamXsexy[0])
            sleeptime = float(SpamX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "document"):
                    smex = await e.client.send_file(e.chat_id, smex, caption=smex.text)
                    await gifspam(e, smex)
                await asyncio.sleep(sleeptime)
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            counter = int(SpamXsexy[0])
            sleeptime = float(SpamX[0])
            for _ in range(counter):
                async with e.client.action(e.chat_id, "typing"):
                    await e.client.send_message(e.chat_id, message)
                    await asyncio.sleep(sleeptime)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None)

#abuse

@omfo.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo2.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo3.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo4.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo5.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo6.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo7.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo8.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo9.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo10.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo11.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo12.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo13.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo14.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo15.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo16.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo17.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo18.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo19.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
@omfo20.on(events.NewMessage(incoming=True, pattern=r"\%sdmspam" % hl))
async def spam(e):
    usage = "𝗠𝗼𝗱𝘂𝗹𝗲 𝗡𝗮𝗺𝗲 = **DM Spam**\n\nCommand:\n\n.dmspam <count> <username> <message to spam>\n\n.dmspam <count> <username> <reply to a message>\n\nCount must be a integer."
    if e.sender_id in SUDO_USERS:
        if e.text[0].isalpha() and e.text[0] in ("/", "#", "@", "!"):
            return await e.reply(usage, parse_mode=None, link_preview=None )
        spamx = ("".join(e.text.split(maxsplit=1)[1:])).split(" ", 2)
        SpamXsexy = spamx[1:]
        smex = await e.get_reply_message()
        if len(SpamXsexy) == 2:
            user = str(SpamXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in SpamX:
                text = f"I can't Dm To SpamX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"O BHAII O YE ALREADY SUDO USER HE CHUTIYO BLA KAM N 😒😒"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                message = str(SpamXsexy[1])
                counter = int(spamx[0])
                await e.reply("⚜️DM Spam Started On Targeted Nigga⚜️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        elif e.reply_to_msg_id and smex.media:
            user = str(SpamXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in SpamX:
                text = f"I can't Dm To SpamX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"O BHAII O YE ALREADY SUDO USER HE CHUTIYO BLA KAM N 😒😒"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:           
                 counter = int(spamx[0])
                 await e.reply("⚜️DM Spam Started On Targeted Nigga⚜️")
                 for _ in range(counter):
                     async with e.client.action(g, "document"):
                        smex = await e.client.send_file(g, smex, caption=smex.text)
                        await gifspam(e, smex) 
                        await asyncio.sleep(0.3)  
        elif e.reply_to_msg_id and smex.text:
            message = smex.text
            user = str(SpamXsexy[0])
            a = await e.client.get_entity(user)
            g = a.id
            if int(g) in SpamX:
                text = f"I can't Dm To SpamX's Owner"
                await e.reply(text, parse_mode=None, link_preview=None )
            elif int(g) in SUDO_USERS:
                text = f"O BHAII O YE ALREADY SUDO USER HE CHUTIYO BLA KAM N 😒😒"
                await e.reply(text, parse_mode=None, link_preview=None )
            else:
                counter = int(spamx[0])
                await e.reply("⚜️DM Spam Started On Targeted Nigga⚜️")
                for _ in range(counter):
                    async with e.client.action(g, "typing"):
                        await e.client.send_message(g, message)
                        await asyncio.sleep(0.3)
        else:
            await e.reply(usage, parse_mode=None, link_preview=None )
