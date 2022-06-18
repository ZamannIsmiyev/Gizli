from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

from config import BOT_USERNAME, BOT_NAME as bot
from helpers.filters import command, other_filters2
# EfsaneMusicVaves tarafından düzenlendi. 

@Client.on_message(command(["start", f"start@{BOT_USERNAME}"]))
async def start(_, message: Message):
                await message.reply_photo(
                "https://te.legra.ph/file/d152f7de679af47d5eec5.jpg" ,
                caption=(f"""**Salam {message.from_user.mention} 🎵\nMən {bot}!\nSəsli söhbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yetkisi verib, Asistanı qrupa əlavə edin.\n\nHostessim👉  [Aysmeh](https://t.me/Akameiyy)**"""),
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/akameiyy_bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Akameiyyy_asisstant"
                    ),
                    InlineKeyboardButton(
                        "Söhbət Qrupum 😍", url="https://t.me/WerabliAnlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🍷", url=f"https://t.me/WerabliAnlarr"
                    )
                ]
                
           ]
        ),
    )
  


@Client.on_message(command(["bilgi", f"bilgi@{BOT_USERNAME}"]))
async def bilgi(_, message: Message):
      await message.reply_text(" ❗ Qeyd:\n Botun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️:\n- Mesaj silmə yetkisi,\n- Bağlantı ilə dəvət etmə yetkisi,\n- Səsli səhbəti yönətmə yetkisi.", 
      reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "🔴 İstifatəçi Əmrləri", callback_data="hərkəs")
                 ],[                     
                     InlineKeyboardButton(
                         "⚫ Admin  Əmrləri", callback_data="admin")
                 ],[
                     InlineKeyboardButton(
                         "Geri 🔄", callback_data="cbstart")
                 ],[
                     InlineKeyboardButton(
                         "Hostessim 😍", url="https://t.me/Akameiyy")
                 ]
             ]
         )
    )


@Client.on_callback_query(filters.regex("cbbilgi"))
async def cbbilgi(_, query: CallbackQuery):
    await query.edit_message_text(" ❗ Qeyd:\nBotun aktiv işləməsi üçün bu üç yetki vermək lazımdır ⬇️\n- Mesaj silmə yetkisi.\n- Bağlantı ilə dəvət etmə yetkisi.\n- Səsli söhbəti yönətmə yetkisi.", 
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton(
            "✨ Hərkəs üçün əmrlər", callback_data ="hərkəs")
        ],
        [
          InlineKeyboardButton(
            "🍷 Admin əmrləri",callback_data ="admin")
        ],
        [
          InlineKeyboardButton(
            "🔄 Geri", callback_data="cbstart")
        ],
        [
          InlineKeyboardButton(
            "Hostessim 😍", url="https://t.me/Akameiyy")
        ]
      ]
     ))


@Client.on_callback_query(filters.regex("herkes"))
async def herkes(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun hərkəs üçün əmr menyusu 😉\n\n ▶️ /play - Musiqi oxutmaq üçün youtube url'sinə vəya musiqi dosyasına yanıt verin\n ▶️ /play <song name> - İstədiyiniz musiqi oxut\n 🔴 \n 🎵 /song <song name> - İstədiyiniz musiqi sürətli bir şəkildə axtarın\n 🎵 /vbul - İstədiyiniz videoları sürətli bir şəkildə axtarın\n 🔍 /video <query> - Youtube'da olan videoları axtarın\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Hostessim 😍", url="https://t.me/Akameiyy")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("admin"))
async def admin(_, query: CallbackQuery):
    await query.edit_message_text(f"""<b>Salam {query.from_user.mention}!\nBu botun adminlər üçün əmr menyusu 🤩\n\n ▶️ /resume - Musiqi oxutmağa davam et\n ⏸️ /durdur - Oxuyan musiqini dayandır\n 🔄 /atla - Sıraya alınmış musiqiyə keç\n ⏹ /skip - Musiqi oxumanı dayandır\n 🔼 /promote - Botun sadəcə yönətici üçün olan əmrlərini istifadə üçün istifadəçiyə yetki ver\n 🔽 /demote - Botun yönətici əmrlərini istifadə edən istifadəçinin yetkisini al\n\n ⚪ /asistan - Musiqi asistanı qrupunuza qoşulur.\n\n</b>""",
    reply_markup=InlineKeyboardMarkup(
             [
                 [
                     InlineKeyboardButton(
                         "Hostessim 😍", url="https://t.me/Akameiyy")
                 ],
                 [
                     InlineKeyboardButton(
                         "️🔄 Geri", callback_data="cbbilgi")
                 ] 
             ]
         )
         )


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(f"""**Salam {query.from_user.mention} 🎵\nMən {bot}!\nSəsli sohbətlərdə musiqi oxuyan botam. Ban yetkisiz, Səs yönətim yetki verib, Asistanı qrupa əlavə edin.\n\nHostessim👉  [Aysmeh](https://t.me/Akameiyy)**""",
         reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "➕ ❰ Məni Qrupa Əlavə Et ❱ ➕", url=f"https://t.me/akameiyy_Bot?startgroup=true"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🔊 Asistan", url="https://t.me/Akameiyyy_asisstant"
                    ),
                    InlineKeyboardButton(
                        "Söhbət Qrupum 🙈", url="https://t.me/WerabliAnlar"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "🧩 Əmrlər" , callback_data= "cbbilgi"
                    ),
                    InlineKeyboardButton(
                        "Rəsmi Kanal 🍷", url=f"https://t.me/WerabliAnlarr"
                    )
                ]
                
           ]
        ),
    )
