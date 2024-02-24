from pyrogram import filters
from Extractor import app
from Extractor.core import script
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


modes_button = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_")
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]])


course_buttons = [              
                [
                    InlineKeyboardButton("ssᴄ ᴍᴀᴋᴇʀ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴘᴇʀғᴇᴄᴛ ᴀᴄᴀᴅᴇᴍʏ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴀᴍᴀɴ sɪʀ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ᴄʟᴀssᴘʟᴜs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴇ1 ᴄᴏᴀᴄʜɪɴɢ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴘᴇʀᴍᴀʀ ssᴄ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("sᴀᴍʏᴀᴋ ʀᴀs", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴠᴊ ᴇᴅᴜᴄᴀᴛɪᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴍᴅ ᴄʟᴀssᴇs", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ɢʏᴀɴ ʙɪɴᴅᴜ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴅʜᴀɴᴀɴᴊᴀʏ ɪᴀs", callback_data="maintainer_"),
                    InlineKeyboardButton("ssᴄ ɢᴜʀᴜᴋᴜʟ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ᴛʜɪɴᴋ ssᴄ", callback_data="maintainer_"),   
                    InlineKeyboardButton("ᴀsʜɪsʜ sɪɴɢ ʟᴇᴄ.", callback_data="maintainer_"),
                    InlineKeyboardButton("ɴɢ ʟᴇᴀʀɴᴇʀs", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),
                    InlineKeyboardButton("ᴄʟᴏꜱᴇ", callback_data="close_data")
                ]
                ]


back_buttons  = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),                    
                ]]



# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo="https://graph.org/file/dbd48ba7093582ab20063.jpg", 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=button)




@app.on_callback_query()
async def cb_handler(client, query):
    if query.data=="home_":
        buttons = [[
                       InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                  ],[
                       InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                       InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                  ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
              script.START_TXT.format(query.from_user.mention),
              reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

# ------------------------------------------------------------------------------- #
        
    elif query.data=="modes_":        
        reply_markup = InlineKeyboardMarkup(modes_button)
        try:
            await query.edit_message_text("modessssss",reply_markup=reply_markup)
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(back_button)
        try:
            await query.edit_message_text(
                "custommm",
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass


# ------------------------------------------------------------------------------- #
        
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(course_buttons)
        try:
            await query.message.edit_text(
                script.MANUAL_TXT,
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
