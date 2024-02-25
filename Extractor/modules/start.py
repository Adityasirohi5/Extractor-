import re
import random
from pyrogram import filters
from Extractor import app
from Extractor.core import script
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton



# ------------------------------------------------------------------------------- #

buttons = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍᴏᴅᴇs", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ]])


modes_button = [[
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]]


course_button = [              
                [
                    InlineKeyboardButton("ssᴄ ᴍᴀᴋᴇʀ", callback_data="ss_maker"),   
                    InlineKeyboardButton("ᴘᴇʀғᴇᴄᴛ ᴀᴄᴀᴅᴇᴍʏ", callback_data="perfect_acc"),
                ],
                [
                    InlineKeyboardButton("ᴄʟᴀssᴘʟᴜs", callback_data="classplus_"),   
                    InlineKeyboardButton("ᴇ1 ᴄᴏᴀᴄʜɪɴɢ", callback_data="e1_coaching"),     
                ],
                [
                    InlineKeyboardButton("sᴀᴍʏᴀᴋ ʀᴀs", callback_data="samyak_ras"),   
                    InlineKeyboardButton("ᴠᴊ ᴇᴅᴜᴄᴀᴛɪᴏɴ", callback_data="vj_education"),              
                ],
                [
                    InlineKeyboardButton("ɢʏᴀɴ ʙɪɴᴅᴜ", callback_data="gyan_bindu"),   
                    InlineKeyboardButton("ᴅʜᴀɴᴀɴᴊᴀʏ ɪᴀs", callback_data="dhananjay_ias"),                   
                ],
                [
                    InlineKeyboardButton("ᴛʜɪɴᴋ ssᴄ", callback_data="think_ssc"),   
                    InlineKeyboardButton("ᴀsʜɪsʜ sɪɴɢ ʟᴇᴄ.", callback_data="Ashish_lec"),                    
                ],
                [
                    InlineKeyboardButton("ᴛᴜᴛᴏʀs ᴀᴅᴅᴀ", callback_data="tutors_adda"),   
                    InlineKeyboardButton("ɴɪᴍɪsʜᴀ ʙᴀɴsᴀʟ", callback_data="nimisha_bansal"),          
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_3"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_1")
                ]
                ]


course_button1 = [
                [
                    InlineKeyboardButton("sᴀᴄʜɪɴ ᴀᴄᴀᴅᴇᴍʏ", callback_data="sachin_acc"),   
                    InlineKeyboardButton("ᴀᴄʜᴀʀʏᴀ ᴄʟᴀssᴇs", callback_data="acharya_classes"),
                ],
                [
                    InlineKeyboardButton("ᴛᴀʀɢᴇᴛ ᴘʟᴜs", callback_data="target_plus"),   
                    InlineKeyboardButton("ʀᴡᴀ", callback_data="rwa_"),
                ],
                [
                    InlineKeyboardButton("ᴡɪɴɴᴇʀs", callback_data="winners_"),   
                    InlineKeyboardButton("ᴏᴄᴇᴀɴ ɢᴜʀᴜᴋᴜʟ", callback_data="ocean_gurukul"),     
                ],
                [
                    InlineKeyboardButton("ᴍɢ ᴄᴏɴᴄᴇᴘᴛ", callback_data="mg_concept"),   
                    InlineKeyboardButton("ʏᴏᴅʜᴀ", callback_data="yodha_"),              
                ],
                [
                    InlineKeyboardButton("ɴᴏᴛᴇ ʙᴏᴏᴋ", callback_data="note_book"),   
                    InlineKeyboardButton("ᴜᴄ ʟɪᴠᴇ", callback_data="uc_live"),      
                ],
                [
                    InlineKeyboardButton("sᴘᴀᴄᴇ ɪᴀs", callback_data="space_ias"),   
                    InlineKeyboardButton("ʀɢ ᴠɪᴋʀᴀᴍᴊᴇᴇᴛ", callback_data="rg_vikramjeet"),       
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="manual_"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_2")
                ]
                ]



course_button2 = [              
                [   
                    InlineKeyboardButton("ᴠɪᴅʏᴀ ʙɪʜᴀʀ", callback_data="vidya_bihar"),
                    InlineKeyboardButton("ᴀᴍᴀɴ sɪʀ", callback_data="aman_sir")
                ],
                [   
                    InlineKeyboardButton("ɴɪʀᴍᴀɴ ɪᴀs", callback_data="nirman_ias"),
                    InlineKeyboardButton("ᴘᴇʀᴍᴀʀ ssᴄ", callback_data="permar_ssc")
                ],
                [
                    InlineKeyboardButton("ɴᴇᴏ sᴘᴀʀᴋ", callback_data="neo_spark"),
                    InlineKeyboardButton("ᴍᴅ ᴄʟᴀssᴇs", callback_data="md_classes")
                ],
                [   
                    InlineKeyboardButton("ɴɢ ʟᴇᴀʀɴᴇʀs", callback_data="ng_learners"),
                    InlineKeyboardButton("ssᴄ ɢᴜʀᴜᴋᴜʟ", callback_data="ssc_gurukul")
                ],
                [
                    InlineKeyboardButton("ᴀʀᴍʏ sᴛᴜᴅʏ ʟɪᴠᴇ", callback_data="army_study"),
                    InlineKeyboardButton("sᴀɴᴋᴀʟᴘ", callback_data="sankalp_")
                ],
                [              
                    InlineKeyboardButton("ᴛᴀʀɢᴇᴛ ᴜᴘsᴄ", callback_data="target_upsc"),
                    InlineKeyboardButton("ɢᴋ ᴄᴀғᴇ", callback_data="gk_cafe")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_1"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_3")
                ]
                ]



course_button3 = [              
                [   
                    InlineKeyboardButton("ᴄᴀʀᴇᴇʀᴡɪʟʟ", callback_data="maintainer_"),
                    InlineKeyboardButton("ᴋʜᴀɴ", callback_data="maintainer_")
                ],
                [   
                    InlineKeyboardButton("ᴘʜʏsɪᴄs ᴡᴀʟʟᴀʜ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [   
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [              
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_"),
                    InlineKeyboardButton("sᴏᴏɴ", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_2"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="manual_")
                ]
                ]




back_button  = [[
                    InlineKeyboardButton("ʙᴀᴄᴋ", callback_data="modes_"),                    
                ]]



# ------------------------------------------------------------------------------- #




@app.on_message(filters.command("start"))
async def start(_,message):
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=buttons)








#@app.on_callback_query(re.compile(r"^(home_|modes_|custom_|manual_|maintainer_|close_data|next_1|next_2|next_3.+)$"))
@app.on_callback_query()
async def handle_callback(_, query):

    if query.data=="home_":        
        
        await query.message.edit_text(
              script.START_TXT.format(query.from_user.mention),
              reply_markup=buttons
            )
        
    elif query.data=="modes_":        
        reply_markup = InlineKeyboardMarkup(modes_button)
        await query.message.edit_text(
              script.MODES_TXT,
              reply_markup=reply_markup)
        
        
    elif query.data=="custom_":        
        reply_markup = InlineKeyboardMarkup(back_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
        
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(course_button)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_1":        
        reply_markup = InlineKeyboardMarkup(course_button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_2":        
        reply_markup = InlineKeyboardMarkup(course_button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_3":        
        reply_markup = InlineKeyboardMarkup(course_button3)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

          
        
    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)



  
  
    elif query.data=="ss_maker":     
        await query.answer((script.SSC_MAKER_TXT), show_alert=True)
    elif query.data=="perfect_acc":     
        await query.answer((script.PERFECT_ACADEMY_TXT), show_alert=True)
    elif query.data=="classplus_":     
        await query.answer((script.CLASSPLUS_TXT), show_alert=True)
    elif query.data=="e1_coaching":     
        await query.answer((script.E1_COACHING_TXT), show_alert=True)
    elif query.data=="samyak_ras":     
        await query.answer((script.SAMYAK_RAS_TXT), show_alert=True)
    elif query.data=="vj_education":     
        await query.answer((script.VJ_EDUCATION_TXT), show_alert=True)
    elif query.data=="gyan_bindu":     
        await query.answer((script.GYAN_BINDU_TXT), show_alert=True)
    elif query.data=="dhananjay_ias":     
        await query.answer((script.DHANANJAY_TXT), show_alert=True)
    elif query.data=="think_ssc":     
        await query.answer((script.THINK_SSC_TXT), show_alert=True)
    elif query.data=="Ashish_lec":     
        await query.answer((script.ASHISH_SING_LEC_TXT), show_alert=True)
    elif query.data=="tutors_adda":     
        await query.answer((script.TUTORS_ADDA_TXT), show_alert=True)
    elif query.data=="nimisha_bansal":     
        await query.answer((script.NIMISHA_BANSAL_TXT), show_alert=True)
    elif query.data=="sachin_acc":     
        await query.answer((script.SACHIN_ACADEMY_TXT), show_alert=True)
    elif query.data=="acharya_classes":     
        await query.answer((script.ACHARYA_CLASSES_TXT), show_alert=True)
    elif query.data=="target_plus":     
        await query.answer((script.TARGET_PLUS_TXT), show_alert=True)
    elif query.data=="rwa_":     
        await query.answer((script.RWA_TXT), show_alert=True)
    elif query.data=="winners_":     
        await query.answer((script.WINNERS_TXT), show_alert=True)
    elif query.data=="ocean_gurukul":     
        await query.answer((script.OCEAN_GURUKUL_TXT), show_alert=True)
    elif query.data=="mg_concept":     
        await query.answer((script.MG_CONCEPT_TXT), show_alert=True)
    elif query.data=="yodha_":     
        await query.answer((script.YODHA_TXT), show_alert=True)
 
    elif query.data=="note_book":     
        await query.answer((script.NOTE_BOOK_TXT), show_alert=True)
    elif query.data=="uc_live":     
        await query.answer((script.UC_LIVE_TXT), show_alert=True)
    elif query.data=="space_ias":     
        await query.answer((script.SPACE_IAS_TXT), show_alert=True)
    elif query.data=="rg_vikramjeet":     
        await query.answer((script.RG_VIKRAMJEET_TXT), show_alert=True)
    elif query.data=="vidya_bihar":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="aman_sir":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="nirman_ias":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="permar_ssc":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="neo_spark":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="md_classes":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="ng_learners":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="ssc_gurukul":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="army_study":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="sankalp_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="target_upsc":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    elif query.data=="gk_cafe":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)
    






    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()



