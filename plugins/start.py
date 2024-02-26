import os
import pymongo
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
import time
from pyrogram import Client, filters
from pyrogram.types import ( InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
import humanize
from helper.progress import humanbytes

from helper.database import botdata, insert ,find_one,used_limit,usertype,uploadlimit,addpredata,total_rename,total_size
from pyrogram.file_id import FileId
from helper.database import daily as daily_
from helper.date import add_date ,check_expi

import datetime
from datetime import date as date_



CHANNEL = int(os.environ.get("CHANNEL",""))
STRING = os.environ.get("STRING","")
log_channel = int(os.environ.get("LOG_CHANNEL",""))
token = os.environ.get('TOKEN','')
botid = token.split(':')[0]



#Part of Day --------------------
currentTime = datetime.datetime.now()

if currentTime.hour < 12:
        wish = "Good morning."
elif 12 <= currentTime.hour < 12:
        wish = 'Good afternoon.'
else:
        wish = 'Good evening.'

#-------------------------------

@Client.on_message(filters.private & filters.command(["start"]))
async def start(client,message):
        old = insert(int(message.chat.id))
        try:
            id = message.text.split(' ')[1]
        except:
            await message.reply_text(text =f"""
👋 Salom {message.from_user.first_name } !

📂 Men 4GB gacha bo'lgan Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
🎬 Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
        
        """,reply_to_message_id = message.id ,  
        reply_markup=InlineKeyboardMarkup(
         [[ InlineKeyboardButton("🎥 Kinolar Olami HD" ,url="https://t.me/Kinolar_OlamiHD") ], 
        [InlineKeyboardButton("🎬 Premyera Kinolar", url="https://t.me/+WLX8n5s-WzRCJcok") ]  ]))
            return
        if id:
            if old == True:
                try:
                    await client.send_message(id,"Your Frind Alredy Using Our Bot")
                    await message.reply_text(text =f"""
👋 Salom {message.from_user.first_name } !

📂 Men 4GB gacha bo'lgan Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
🎬 Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
        """,reply_to_message_id = message.id ,  
        reply_markup=InlineKeyboardMarkup(
         [[ InlineKeyboardButton("🎥 Kinolar Olami HD" ,url="https://t.me/Kinolar_OlamiHD") ], 
        [InlineKeyboardButton("🎬 Premyera Kinolar", url="https://t.me/+WLX8n5s-WzRCJcok") ]  ]))
                except:
                     return
            else:
                 await client.send_message(id,"Tabrik! Siz 100MB yutib oldingiz.")
                 _user_= find_one(int(id))
                 limit = _user_["uploadlimit"]
                 new_limit = limit + 104857600
                 uploadlimit(int(id),new_limit)
                 await message.reply_text(text =f"""
👋 Salom {message.from_user.first_name } !

📂 Men 4GB gacha bo'lgan Telegram fayllarni nomini o'zgartirib va videoga pechat qo'yib beradigan botman! 
🎬 Menga Fayl/Video/Audio yuboring va uni qayta nomlang✍️
        
        """,reply_to_message_id = message.id ,  
        reply_markup=InlineKeyboardMarkup(
         [[ InlineKeyboardButton("🎥 Kinolar Olami HD" ,url="https://t.me/Kinolar_OlamiHD") ], 
        [InlineKeyboardButton("🎬 Premyera Kinolar", url="https://t.me/+WLX8n5s-WzRCJcok") ]  ]))




@Client.on_message(filters.private &( filters.document | filters.audio | filters.video ))
async def send_doc(client,message):
       update_channel = CHANNEL
       user_id = message.from_user.id
       if update_channel :
               try:
                       await client.get_chat_member(update_channel, user_id)
               except UserNotParticipant:
                       await message.reply_text(text =f"""🤖 @RENAMERGO_BOT 👇

❗️Botdan foydalanishda davom etish uchun guruhga a'zo bo'lishingiz kerak✅️""",
                       reply_to_message_id = message.id,
                       reply_markup = InlineKeyboardMarkup(
                       [ [ InlineKeyboardButton("✅ Obuna | Subscription | Подписка" ,url="https://t.me/RenamerGo_News") ]   ]))
                       return

       botdata(int(botid))
       bot_data = find_one(int(botid))
       prrename = bot_data['total_rename']
       prsize = bot_data['total_size']
       user_deta = find_one(user_id)
       try:
               used_date = user_deta["date"]
               buy_date= user_deta["prexdate"]
               daily = user_deta["daily"]
       except:
           await message.reply_text("Botni ishlatish uchun qayta /start tugmasini bosing.")
           return


       c_time = time.time()

       if buy_date==None:
           LIMIT = 300
       else:
           LIMIT = 10
       then = used_date+ LIMIT
       left = round(then - c_time)
       conversion = datetime.timedelta(seconds=left)
       ltime = str(conversion)
       if left > 0:                   
               await message.reply_text(f"<pre>Kechirasiz men faqat SIZ uchun emasman.\nFlood nazorati faol shuning uchun kuting {ltime}</pre>",reply_to_message_id = message.id)
       else:
                       # Forward a single message
                       await client.forward_messages(log_channel, message.from_user.id, message.id)
                       await client.send_message(log_channel,f"User Id :- {user_id}")                       
                       media = await client.get_messages(message.chat.id,message.id)
                       file = media.document or media.video or media.audio 
                       dcid = FileId.decode(file.file_id).dc_id
                       filename = file.file_name
                       value = 104857600
                       used_ = find_one(message.from_user.id)
                       used = used_["used_limit"]
                       limit = used_["uploadlimit"]
                       expi = daily - int(time.mktime(time.strptime(str(date_.today()), '%Y-%m-%d')))
                       if expi != 0:
                               today = date_.today()
                               pattern = '%Y-%m-%d'
                               epcho = int(time.mktime(time.strptime(str(today), pattern)))
                               daily_(message.from_user.id,epcho)
                               used_limit(message.from_user.id,0)                                             
                       remain = limit - used
                       if remain < int(file.file_size):
                           await message.reply_text(f"❗Kechirasiz! Men {humanbytes(limit)}dan katta fayllarni sizga yubora olmayman.\nAniqlangan fayl hajmi {humanbytes(file.file_size)}\nKunlik foydalanilgan limit {humanbytes(used)}",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("💸 Tarif sotib olish",callback_data = "upgrades")]]))
                           return
                       if value < file.file_size:
                           if STRING:
                               if buy_date==None:
                                   await message.reply_text(f" Siz {humanbytes(limit)} dan ko'p yuklay olmaysiz.\nKunlik foydalanilgan limit {humanbytes(used)}",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("💸 Tarif sotib olish",callback_data = "upgrades")]]))
                                   return
                               pre_check = check_expi(buy_date)
                               if pre_check == True:
                                   await message.reply_text(f"""<i>Ushbu faylni nima qilmoqchisiz?</i>\n<b>Fayl Nomi</b>: {filename}\n<b>Fayl Hajmi</b>: {humanize.naturalsize(file.file_size)}\n<b>DC ID</b>: {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup([[ InlineKeyboardButton("Qayta nomlash 📝",callback_data = "rename"),InlineKeyboardButton("Bekor qilish ✖️",callback_data = "cancel")  ]]))
                                   total_rename(int(botid),prrename)
                                   total_size(int(botid),prsize,file.file_size)
                               else:
                                   await message.reply_text(f"Nimadir xato ketdi! Admin bilan bog'laning!!! ",quote=True) #Sizning ta'rifingiz {buy_date}da tugaydi!
                                   return
                           else:
                                         await message.reply_text("2GB dan katta faylni yuklay olmayman ")
                                         return
                       else:
                           filesize = humanize.naturalsize(file.file_size)
                           fileid = file.file_id
                           total_rename(int(botid),prrename)
                           total_size(int(botid),prsize,file.file_size)
                           await message.reply_text(f"""<i>Ushbu faylni nima qilmoqchisiz?</i>\n<b>Fayl Nomi</b>: {filename}\n<b>Fayl Hajmi</b>: {filesize}\n<b>DC ID</b>: {dcid}""",reply_to_message_id = message.id,reply_markup = InlineKeyboardMarkup(
                       [[ InlineKeyboardButton("Qayta nomlash 📝",callback_data = "rename"),
                       InlineKeyboardButton("Bekor qilish ✖️",callback_data = "cancel")  ]]))
