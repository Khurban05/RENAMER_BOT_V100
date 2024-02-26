"""lokaman"""
from pyrogram.types import (InlineKeyboardButton, InlineKeyboardMarkup,ForceReply)
from pyrogram import Client , filters

@Client.on_callback_query(filters.regex('upgrades'))
async def upgrade(bot,update):
        text = """Tariflar✅

Bepul                |Mini💫
Kunlik limit: 100MB  |Kunlik limit: 5GB
Narxi: Bepul.        |Narxi: 1.5$/oy

Lite✨              |VIP⚡
Kunlik limit: 15GB  |Kunlik limit: 50GB
Narxi: 4$/oy        |Narxi: 7$/oy


Premium 👑             
Kunlik limit: 150GB 
Narxi: 15💲/oy 
 
To'lov usullari: HUMO💳  | UZCARD💳 |  VISA💳
 
Ta'rif sotib olmoqchi bo'lsangiz admin bilan bog'laning.
4Gbgacha faylni yuklash uchun Telegram Premium va undan tashqari bot ishlashi uchun server kerak. Bizni to'g'ri tushundingiz degan umiddamiz🙂"""
        keybord = InlineKeyboardMarkup([[ 
                                InlineKeyboardButton("Administrator",url = "https://t.me/Coder_MYP")], 
                                [InlineKeyboardButton("Bekor qilish",callback_data = "cancel")  ]])
        await update.message.edit(text = text,reply_markup = keybord)


@Client.on_message(filters.private & filters.command(["upgrade"]))
async def upgradecm(bot,message):
        text = """Tariflar✅

Bepul                |Mini💫
Kunlik limit: 100MB  |Kunlik limit: 5GB
Narxi: Bepul.        |Narxi: 1.5$/oy

Lite✨              |VIP⚡
Kunlik limit: 15GB  |Kunlik limit: 50GB
Narxi: 4$/oy        |Narxi: 7$/oy

Premium 👑             
Kunlik limit: 150GB 
Narxi: 15💲/oy 
 
To'lov usullari: HUMO💳  | UZCARD💳 |  VISA💳
 
Ta'rif sotib olmoqchi bo'lsangiz admin bilan bog'laning.
4Gbgacha faylni yuklash uchun Telegram Premium va undan tashqari bot ishlashi uchun server kerak. Bizni to'g'ri tushundingiz degan umiddamiz🙂"""
        keybord = InlineKeyboardMarkup([[ 
                                InlineKeyboardButton("Administrator",url = "https://t.me/Coder_MYP")],                   [InlineKeyboardButton("VISA💳",url = "https://t.me/Coder_MYP")],[InlineKeyboardButton("Bekor qilish",callback_data = "cancel")  ]])
        await message.reply_text(text = text,reply_markup = keybord)