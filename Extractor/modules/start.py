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
                    InlineKeyboardButton("SSC MAKER", callback_data="maintainer_"),   
                    InlineKeyboardButton("Perfect Academy", callback_data="maintainer_"),
                    InlineKeyboardButton("Aman Sir", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("Classplus", callback_data="maintainer_"),   
                    InlineKeyboardButton("E1 Coaching", callback_data="maintainer_"),
                    InlineKeyboardButton("Permar Ssc", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("Samyak Ras", callback_data="maintainer_"),   
                    InlineKeyboardButton("Vj Education", callback_data="maintainer_"),
                    InlineKeyboardButton("Md Classes", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("GYAN BINDU", callback_data="maintainer_"),   
                    InlineKeyboardButton("DHANANJAY IAS", callback_data="maintainer_"),
                    InlineKeyboardButton("SSC GURUKUL", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("Think Ssc", callback_data="maintainer_"),   
                    InlineKeyboardButton("Ashish Singh LC", callback_data="maintainer_"),
                    InlineKeyboardButton("NG LEARNERS", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="home_"),
                    InlineKeyboardButton("⟲ ᴄʟᴏꜱᴇ ⟳", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("⟲ ʙᴀᴄᴋ ⟳", callback_data="help_"),                    
                ]]



# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://telegra.ph/file/9456751a4ca1a346e631f.jpg", caption="**ʜᴇʏ ᴛʜᴇʀᴇ!  ᴜɴʟᴇᴀsʜ ᴛʜᴇ ᴘᴏᴡᴇʀ ᴏғ ᴛʜᴇ ᴜʟᴛɪᴍᴀᴛᴇ ᴄᴏᴜʀsᴇ ᴅᴏᴡɴʟᴏᴀᴅ ᴡɪᴢᴀʀᴅ – ɪ'ᴍ ɴᴏᴛ Jᴜsᴛ ʏᴏᴜʀ ᴀᴠᴇʀᴀɢᴇ ᴠɪᴅᴇᴏ ᴅᴏᴡɴʟᴏᴀᴅᴇʀ ʙᴏᴛ; ɪ'ᴍ ʏᴏᴜʀ ᴠɪᴘ ᴘᴀss ᴛᴏ ɢʀᴀʙʙɪɴɢ ᴏɴʟɪɴᴇ ᴄᴏᴜʀsᴇs ɪɴ sᴛʏʟᴇ!  ʀᴇᴀᴅʏ ᴛᴏ ᴇʟᴇᴠᴀᴛᴇ ʏᴏᴜʀ ʟᴇᴀʀɴɪɴɢ ɢᴀᴍᴇ? ʟᴇᴛ's ᴅɪᴠᴇ ɪɴᴛᴏ ᴛʜᴇ ᴡᴏʀʟᴅ ᴏғ ᴋɴᴏᴡʟᴇᴅɢᴇ ᴛᴏɢᴇᴛʜᴇʀ! 🎓✨**",
                            reply_markup=button)



@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        reply_markup = InlineKeyboardMarkup(button)
        try:
            await query.edit_message_text(
                start_txt.format(query.from_user.mention),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="help_":        
        reply_markup = InlineKeyboardMarkup(course_buttons)
        try:
            await query.edit_message_text(
                help_txt,
                reply_markup=reply_markup
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
