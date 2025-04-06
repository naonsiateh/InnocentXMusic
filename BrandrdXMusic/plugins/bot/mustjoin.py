
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
from BrandrdXMusic import app

#--------------------------

MUST_JOIN = "AlteregoHub"
#------------------------
@app.on_message(filters.incoming & filters.private, group=-1)
async def must_join_channel(app: Client, msg: Message):
    if not MUST_JOIN:
        return
    try:
        try:
            await app.get_chat_member(MUST_JOIN, msg.from_user.id)
        except UserNotParticipant:
            if MUST_JOIN.isalpha():
                link = "https://t.me/" + MUST_JOIN
            else:
                chat_info = await app.get_chat(MUST_JOIN)
                link = chat_info.invite_link
            try:
                await msg.reply_photo(
                    photo="https://files.catbox.moe/mim7yt.jpg", caption=f"๏ Menurut database saya, kamu belum bergabung dengan [๏ AlteregoHub ๏]({link}). Jika kamu ingin menggunakan saya, maka bergabunglah dengan [๏ AlteregoHub ๏]({link}) dan memulai saya kembali!  ",
                    reply_markup=InlineKeyboardMarkup(
                        [
                            [
                                InlineKeyboardButton("๏ Join AlterHub ๏", url=link),
                            ]
                        ]
                    )
                )
                await msg.stop_propagation()
            except ChatWriteForbidden:
                pass
    except ChatAdminRequired:
        print(f"๏Jadikan saya admin di obrolan must_join ๏: {MUST_JOIN} !")
