from pyrogram import filters
from Extractor import app
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ʜᴇʟᴘ", callback_data="help_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


course_buttons = [              
                [
                    InlineKeyboardButton("ᴍ", callback_data="m_"),   
                    InlineKeyboardButton("ᴀɪ", callback_data="_"),
                    InlineKeyboardButton("ʙᴀss", callback_data="bass_")
                ],
                [
                    InlineKeyboardButton("ʏᴏᴜᴛᴜʙᴇ", callback_data="youtube_"),   
                    InlineKeyboardButton("ᴍɪsᴄ", callback_data="misc_"),
                    InlineKeyboardButton("ʙʀᴏᴀᴅᴄᴀsᴛ", callback_data="broadcast_")
                ],
                [
                    InlineKeyboardButton("ᴄʜᴇᴄᴋᴇʀ", callback_data="checker_"),   
                    InlineKeyboardButton("ᴅᴇᴠs", callback_data="devs_"),
                    InlineKeyboardButton("ɪɴsᴛᴀɢʀᴀᴍ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]


help_txt = """**
**» ˹ᴄʜɪᴢᴜʀᴜ˼ ᴄᴏᴏʟ ᴏʀ ᴇxᴄʟᴜsɪᴠᴇ ғᴇᴀᴛᴜʀᴇs** 
"""
# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/9456751a4ca1a346e631f.jpg", caption="**ʜᴇʏ ᴛʜᴇʀᴇ!  ᴜɴʟᴇᴀsʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴄᴏᴜʀsᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴢᴀʀᴅ – ɪ'ᴍ ɴᴏᴛ Jᴜsᴛ ʏᴏᴜʀ ᴀᴠᴇʀᴀɢᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ; ɪ'ᴍ ʏᴏᴜʀ ᴠɪᴘ ᴘᴀss ᴛᴏ ɢʀᴀʙʙɪɴɢ ᴏɴʟɪɴᴇ ᴄᴏᴜʀsᴇs ɪɴ sᴛʏʟᴇ!  ʀᴇᴀᴅʏ ᴛᴏ ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟᴇᴀʀɴɪɴɢ ɢᴀᴍᴇ? ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ ᴛᴏɢᴇᴛʜᴇʀ! 🎓✨**",
                            reply_markup=button)



@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=button
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(chizuru_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=course_buttons
            )
        except MessageNotModified:
            pass

# ------------------------------------------------------------------------------- #

    elif query.data=="maintainer_":
            await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)

  
# ------------------------------------------------------------------------------- #
 
    elif query.data=="close_data":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass
