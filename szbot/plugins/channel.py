import os
from pyrogram import filters
from szbot import sz as rose
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, InputMediaPhoto
from requests import get
import datetime
import pytz

picmetxt = """
**Now You can Create your Image Useing Me!**

✪ Pic me : Capture Your Profile Picture.
✪ Hq logo : Create your own hq logo.
✪ Logo : create your own logo.
✪ Wallpaper : Get some new wallpapers.

Send To Inbox Automatically You must start
[This Bot](https://t.me/szimagebot)

@szimagebot |User : {} 
"""

picmebtns = InlineKeyboardMarkup(
            [       
                [
                    InlineKeyboardButton("Pic me", callback_data="picme me"),
                    InlineKeyboardButton("Hq logo", callback_data="picme hql") 
                ],
                [
                    InlineKeyboardButton("Logo", callback_data="picme new"),
                    InlineKeyboardButton("Wallpaper", callback_data="picme wall")           
                ],   
            ]
        )

pm = """
logo Genarated Successfully✅
࿂ **Generated By** : [Image Tool Bot](https://t.me/szimagebot)
࿂ **Requestor** :. {}
࿂ **Powered By **  : [szteambots](https://t.me/szteambots)
"""


@rose.on_message(filters.command("addchannel"))
async def sendthepicme(_, message):
    try:
        text = message.text.split(None, 1)[1]
        CHANNEL = text
        picmetxt = """
**Now You can Create your Image Useing Me!**

✪ Pic me : Capture Your Profile Picture.
✪ Hq logo : Create your own hq logo.
✪ Logo : create your own logo.
✪ Wallpaper : Get some new wallpapers.

Send To Inbox Automatically You must start
[This Bot](https://t.me/szimagebot)
"""
        await rose.send_photo(chat_id=CHANNEL,photo="https://telegra.ph/file/77e05e0b5bd6a60eb5ca9.jpg",caption=picmetxt, reply_markup=picmebtns)
    except Exception as e:
            await rose.send_message(message.from_user.id,"Please make sure sz image bot is promoted as admin in your channel.")
            print(str(e))

TIME_ZONE = "Asia/colombo"

@rose.on_callback_query(filters.regex("picme"))
async def mylogo(_, query):
    mode = query.data.split()[1].strip()
    picmetext = picmetxt.format(query.from_user.mention)
    if mode == "me" and query.from_user.photo:
        try:
            await query.answer("Capture started...Creating Your dp", show_alert=True)
            photoid = query.from_user.photo.big_file_id  
            photo = await rose.download_media(photoid)
            await query.edit_message_media(InputMediaPhoto(media=photo, caption=picmetext), reply_markup=picmebtns)
            await rose.send_photo(query.from_user.id, photo=photo, caption=pm.format(query.from_user.mention))
            if os.path.exists(photo):os.remove(photo)
        except Exception as e:
            await query.answer("Please start @szimagebot !\n to get your logo")
            print(str(e))
            if os.path.exists(photo):os.remove(photo)  

    if mode == "new" or not query.from_user.photo:
        try:
            await query.answer("Creating Your logo..", show_alert=True)
            lol = get((f"https://single-developers.up.railway.app/logo?name={query.from_user.first_name}").replace(' ','%20')).history[1].url
            await query.edit_message_media(InputMediaPhoto(media=lol, caption=picmetext), reply_markup=picmebtns)
            await rose.send_photo(query.from_user.id, photo=lol, caption=pm.format(query.from_user.mention))
        except Exception as e:
            await query.answer("Please start @szimagebot !\n to get your logo")
            print(str(e))
            if os.path.exists(photo):os.remove(photo)  

    if mode == "wall" or not query.from_user.photo:
        try:
            await query.answer("Creating Your wallpaper..", show_alert=True)
            lol = get((f"https://single-developers.up.railway.app/wallpaper?search={query.from_user.first_name}").replace(' ','%20')).history[1].url
            await query.edit_message_media(InputMediaPhoto(media=lol, caption=picmetext), reply_markup=picmebtns)
            await rose.send_photo(query.from_user.id, photo=lol, caption=pm.format(query.from_user.mention))
        except Exception as e:
            await query.answer("Please start @szimagebot !\n to get your logo")
            print(str(e))
            if os.path.exists(photo):os.remove(photo)  

    if mode == "hql" or not query.from_user.photo:
        try:
            await query.answer("Creating Your logo..", show_alert=True)
            lol = get((f"https://single-developers.up.railway.app/logohq?name={query.from_user.first_name}").replace(' ','%20')).history[1].url
            await query.edit_message_media(InputMediaPhoto(media=lol, caption=picmetext), reply_markup=picmebtns)
            await rose.send_photo(query.from_user.id, photo=lol, caption=pm.format(query.from_user.mention))
        except Exception as e:
            await query.answer("Please start @szimagebot !\n to get your logo")
            print(str(e))
            if os.path.exists(photo):os.remove(photo)  
