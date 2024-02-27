import re
import random
from pyrogram import filters
from Extractor import app
from config import OWNER_ID, SUDO_USERS
from Extractor.core import script
from Extractor.core.func import subscribe
from pyrogram.types import CallbackQuery, InlineKeyboardMarkup, InlineKeyboardButton
from Extractor.modules.appex_v2 import appex_v2_txt
from Extractor.modules.classplus import classplus_txt
#from Extractor.modules.pw import pw_mobile, pw_token
from Extractor.modules.exampur import exampur_txt
from Extractor.modules.app_exampur import appexampur_txt
from Extractor.modules.careerwill import career_will
from Extractor.modules.khan import khan_login



# ------------------------------------------------------------------------------- #




buttons = InlineKeyboardMarkup([
                [
                  InlineKeyboardButton("ᴍ ᴏ ᴅ ᴇ s", callback_data="modes_")
                ],[
                  InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url="https://t.me/DevsCreations"),
                  InlineKeyboardButton("sᴜᴘᴘᴏʀᴛ", url="https://t.me/DevsOops")
                ],[
                  InlineKeyboardButton("ᴘ ʟ ᴀ ɴ s", callback_data="premium_")
                ]])


modes_button = [[
                  InlineKeyboardButton("ᴄᴜsᴛᴏᴍ", callback_data="custom_"),
                  InlineKeyboardButton("ᴍᴀɴᴜᴀʟ", callback_data="manual_"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="home_")
                ]]


custom_button = [[
                  InlineKeyboardButton("Appex V2", callback_data="v2_"),
                  InlineKeyboardButton("Appex V3", callback_data="v3_"),
                ],[
                  InlineKeyboardButton("𝐁 𝐀 𝐂 𝐊", callback_data="modes_")
                ]]

button1 = [              
                [
                    InlineKeyboardButton("Ssc Maker", callback_data="ss_maker"),   
                    InlineKeyboardButton("Perfect Academy", callback_data="perfect_acc"),
                ],
                [
                    InlineKeyboardButton("Classplus", callback_data="classplus_"),   
                    InlineKeyboardButton("E1 Coaching", callback_data="e1_coaching"),     
                ],
                [
                    InlineKeyboardButton("Samyak", callback_data="samyak_ras"),   
                    InlineKeyboardButton("Vj Education", callback_data="vj_education"),              
                ],
                [
                    InlineKeyboardButton("Gyan Bindu", callback_data="gyan_bindu"),   
                    InlineKeyboardButton("Dhananjay IAS", callback_data="dhananjay_ias"),                   
                ],
                [
                    InlineKeyboardButton("Think Ssc", callback_data="think_ssc"),   
                    InlineKeyboardButton("Ashish Sing Lec.", callback_data="Ashish_lec"),                    
                ],
                [
                    InlineKeyboardButton("Tutors Adda", callback_data="tutors_adda"),   
                    InlineKeyboardButton("Nimisha Bansla", callback_data="nimisha_bansal"),          
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_3"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_1")
                ]
                ]


button2 = [
                [
                    InlineKeyboardButton("Sachin Academy", callback_data="sachin_acc"),   
                    InlineKeyboardButton("Acharya Classes", callback_data="acharya_classes"),
                ],
                [
                    InlineKeyboardButton("Target Plus", callback_data="target_plus"),   
                    InlineKeyboardButton("Rwa", callback_data="rwa_"),
                ],
                [
                    InlineKeyboardButton("Winners", callback_data="winners_"),   
                    InlineKeyboardButton("Ocean Gurukul", callback_data="ocean_gurukul"),     
                ],
                [
                    InlineKeyboardButton("Mg Concept", callback_data="mg_concept"),   
                    InlineKeyboardButton("Yodha", callback_data="yodha_"),              
                ],
                [
                    InlineKeyboardButton("Note Book", callback_data="note_book"),   
                    InlineKeyboardButton("Uc Live", callback_data="uc_live"),      
                ],
                [
                    InlineKeyboardButton("Space IAS", callback_data="space_ias"),   
                    InlineKeyboardButton("Rg Vikramjeet", callback_data="rg_vikramjeet"),       
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="manual_"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_2")
                ]
                ]



button3 = [              
                [   
                    InlineKeyboardButton("Vidya Bihar", callback_data="vidya_bihar"),
                    InlineKeyboardButton("Aman Sir", callback_data="aman_sir")
                ],
                [   
                    InlineKeyboardButton("Nirman IAS", callback_data="nirman_ias"),
                    InlineKeyboardButton("Permar Ssc", callback_data="permar_ssc")
                ],
                [
                    InlineKeyboardButton("Neo Spark", callback_data="neo_spark"),
                    InlineKeyboardButton("Md Classes", callback_data="md_classes")
                ],
                [   
                    InlineKeyboardButton("Ng Learners", callback_data="ng_learners"),
                    InlineKeyboardButton("Ssc Gurkul", callback_data="ssc_gurukul")
                ],
                [
                    InlineKeyboardButton("Army Study", callback_data="army_study"),
                    InlineKeyboardButton("Sankalp", callback_data="sankalp_")
                ],
                [              
                    InlineKeyboardButton("Target Upsc", callback_data="target_upsc"),
                    InlineKeyboardButton("Gk Cafe", callback_data="gk_cafe")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_1"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_3")
                ]
                ]



button4 = [              
                [   
                    InlineKeyboardButton("Careerwill", callback_data="careerwill_"),
                    InlineKeyboardButton("Khan", callback_data="khan_")
                ],
                [   
                    InlineKeyboardButton("Physics Wallah", callback_data="maintainer_"),
                    InlineKeyboardButton("Exampur", callback_data="exampur_")
                ],
                [
                    InlineKeyboardButton("App Exampur", callback_data="app_exampur"),
                    InlineKeyboardButton("Neet Kakajee", callback_data="neet_kakajee")
                ],
                [   
                    InlineKeyboardButton("Officers Academy", callback_data="officers_acc"),
                    InlineKeyboardButton("Rk Sir", callback_data="rk_sir")
                ],
                [
                    InlineKeyboardButton("Study Mantra", callback_data="study_mantra"),
                    InlineKeyboardButton("Science Fun", callback_data="science_fun")
                ],
                [              
                    InlineKeyboardButton("Grow Academy", callback_data="grow_acc"),
                    InlineKeyboardButton("Goal Yaan", callback_data="goal_yaan")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_2"),
                    InlineKeyboardButton("ʙ ᴀ ᴄ ᴋ", callback_data="modes_"),
                    InlineKeyboardButton("﹥", callback_data="next_4")
                ]
                ]


button5 = [              
                [   
                    InlineKeyboardButton("Anil Sir iti", callback_data="anilsir_iti"),
                    InlineKeyboardButton("Education Adda", callback_data="education_adda")
                ],
                [   
                    InlineKeyboardButton("Achievers Academy", callback_data="achievers_acc"),
                    InlineKeyboardButton("Cammando Academy", callback_data="commando_acc")
                ],
                [
                    InlineKeyboardButton("Soon", callback_data="maintainer_"),
                    InlineKeyboardButton("Soon", callback_data="maintainer_")
                ],
                [   
                    InlineKeyboardButton("Soon", callback_data="maintainer_"),
                    InlineKeyboardButton("Soon", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("Soon", callback_data="maintainer_"),
                    InlineKeyboardButton("Soon", callback_data="maintainer_")
                ],
                [              
                    InlineKeyboardButton("Soon", callback_data="maintainer_"),
                    InlineKeyboardButton("Soon", callback_data="maintainer_")
                ],
                [
                    InlineKeyboardButton("﹤", callback_data="next_3"),
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
  join = await subscribe(_,message)
  if join ==1:
    return
  await message.reply_photo(photo=random.choice(script.IMG), 
                            caption=script.START_TXT.format(message.from_user.mention),
                            reply_markup=buttons)








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
        reply_markup = InlineKeyboardMarkup(custom_button)
        await query.message.edit_text(
              script.CUSTOM_TXT,
              reply_markup=reply_markup
            )
        
     
    elif query.data=="manual_":        
        reply_markup = InlineKeyboardMarkup(button1)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

    elif query.data=="v2_": 
        api = await app.ask(query.message.chat.id, text="**SEND APPX API\n\n✅ Example:\ntcsexamzoneapi.classx.co.in**")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
        await appex_v2_txt(app, query.message, api_txt, name)

    elif query.data=="v3_": 
        api = await app.ask(query.message.chat.id, text="**SEND APPX API\n\n✅ Example:\ntcsexamzoneapi.classx.co.in**")
        api_txt = api.text
        name = api_txt.split('.')[0].replace("api", "") if api else api_txt.split('.')[0]
#        await appex_v3_txt(app, query.message, api_txt, name)
      
    elif query.data=="next_1":        
        reply_markup = InlineKeyboardMarkup(button2)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_2":        
        reply_markup = InlineKeyboardMarkup(button3)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )
      
    elif query.data=="next_3":        
        reply_markup = InlineKeyboardMarkup(button4)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

    elif query.data=="next_4":        
        reply_markup = InlineKeyboardMarkup(button5)
        await query.message.edit_text(
              script.MANUAL_TXT,
              reply_markup=reply_markup
            )

          
        
    elif query.data=="maintainer_":     
        await query.answer(("sᴏᴏɴ.... \n ʙᴏᴛ ᴜɴᴅᴇʀ ɪɴ ᴍᴀɪɴᴛᴀɪɴᴀɴᴄᴇ "), show_alert=True)


    elif query.data=="careerwill_":
        await career_will(app, query.message)
  
    elif query.data=="khan_":
        await khan_login(app, query.message)

    elif query.data=="ss_maker":     
        api = "sscmakerexampreparationapi.classx.co.in"
        name = "SSC Makers"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="perfect_acc":     
        api = "perfectionacademyapi.appx.co.in"
        name = "Perfection Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="e1_coaching":     
        api = "e1coachingcenterapi.classx.co.in"
        name = "e1 coaching"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="samyak_ras":     
        api = "samyakapi.classx.co.in"
        name = "Samyak"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="vj_education":     
        api = "vjeducationapi.appx.co.in"
        name = "VJ Education"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="gyan_bindu":     
        api = "gyanbinduapi.appx.co.in"
        name = "Gyan Bindu"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="dhananjay_ias":     
        api = "dhananjayiasacademyapi.classx.co.in"
        name = "Dhananjay IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="think_ssc":     
        api = "thinksscapi.classx.co.in"
        name = "Think SSC"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="Ashish_lec":     
        api = "ashishsinghlecturesapi.classx.co.in"
        name = "Ashish Singh"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="tutors_adda":     
        api = "tutorsaddaapi.classx.co.in"
        name = "Tutors Adda"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="nimisha_bansal":     
        api = "nimishabansalapi.appx.co.in"
        name = "Nimisha Bansal"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="sachin_acc":     
        api = "sachinacademyapi.classx.co.in"
        name = "Sachin Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="acharya_classes":     
        api = "acharyaclassesapi.classx.co.in"
        name = "Acharya Classes"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="target_plus":     
        api = "targetpluscoachingapi.classx.co.in"
        name = "Target Plus Coaching"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="rwa_":   
        api = "rozgarapinew.teachx.in"
        name = "Rojgar with Ankit"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="winners_":     
        api = "winnersinstituteapi.classx.co.in"
        name = "Winners"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ocean_gurukul":     
        api = "oceangurukulsapi.classx.co.in"
        name = "Ocean Gurukul"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="mg_concept":     
        api = "mgconceptapi.classx.co.in"
        name = "MG Concept"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="yodha_":     
        api = "yodhaappapi.classx.co.in"
        name = "Yodha"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="note_book":     
        api = "notebookapi.classx.co.in"
        name = "Note Book"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="uc_live":     
        api = "ucliveapi.classx.co.in"
        name = "UC LIVE"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="space_ias":     
        api = "spaceiasapi.classx.co.in"
        name = "Space IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="rg_vikramjeet":     
        api = "rgvikramjeetapi.classx.co.in"
        name = "RG Vikramjeet"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="vidya_bihar":     
        api = "vidyabiharapi.teachx.in"
        name = "Vidya Vihar"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="aman_sir":     
        api = "amansirenglishapi.classx.co.in"
        name = "Aman Sir English"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="nirman_ias":     
        api = "nirmaniasapi.classx.co.in"
        name = "Nirman IAS"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="permar_ssc":     
        api = "parmaracademyapi.classx.co.in"
        name = "Parmar Academy"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="neo_spark":     
        api = "neosparkapi.classx.co.in"
        name = "Neo Spark"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="md_classes":     
        api = "mdclassesapi.classx.co.in"
        name = "MD Classes"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ng_learners":     
        api = "nglearnersapi.classx.co.in"
        name = "NG Learners"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="ssc_gurukul":     
        api = "ssggurukulapi.appx.co.in"
        name = "SSC Gurukul"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="army_study":     
        api = "armystudyliveclassesapi.classx.co.in"
        name = "Army Study Live"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="sankalp_":     
        api = "sankalpclassesapi.classx.co.in"
        name = "Sankalp"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="target_upsc":     
        api = "targetupscapi.classx.co.in"
        name = "Target UPSC"
        await appex_txt(app, query.message, api, name)
      
    elif query.data=="gk_cafe":     
        api = "gkcafeapi.classx.co.in"
        name = "GK Cafe"
        await appex_txt(app, query.message, api, name)

    elif query.data == 'officers_acc':
        api = "theofficersacademyapi.classx.co.in"
        name = "Officers Academy"
        await appex_txt(app, query.message, api, name)

    elif query.data == 'rk_sir':
        api = "rksirofficialapi.classx.co.in"
        name = "Rk Sir Official"
        await appex_txt(app, query.message, api, name) 
      
    elif query.data == 'study_mantra':
        api = "studymantraapi.classx.co.in"
        name = "Study Mantra"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'science_fun':
        api = "sciencefunapi.classx.co.in"
        name = "Science Fun"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'grow_acc':
        api = "growacademyapi.classx.co.in"
        name = "Grow Academy"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'goal_yaan':
        api = "goalyaanapi.appx.co.in"
        name = "Goal Yaan"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'anilsir_iti':
        api = "anilsiritiapi.classx.co.in"
        name = "Anil Sir Iti"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'education_adda':
        api = "educationaddaplusapi.classx.co.in"
        name = "Education Adda Plus"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'achievers_acc':
        api = "achieversacademyapi.classx.co.in"
        name = "Achievers Academy"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'commando_acc':
        api = "commandoacademyapi.appx.co.in"
        name = "Commando Academy"
        await appex_txt(app, query.message, api, name) 


    elif query.data == 'exampur_':
        await exampur_txt(app, query.message)

    elif query.data == 'neet_kakajee':
        api = "neetkakajeeapi.classx.co.in"
        name = "Neet Kaka JEE"
        await appex_txt(app, query.message, api, name) 

    elif query.data == 'app_exampur':
        await appexampur_txt(app, query.message)
  
    elif query.data=="classplus_":          
        await classplus_txt(app, query.message)
  
#    elif query.data == 'pw_':
#        await query.message.reply_text(
#            "**CHHOSE FROM BELOW **",
#            reply_markup=InlineKeyboardMarkup([
#                [
#                    InlineKeyboardButton("Mobile No.", callback_data='mobile_'),
#                    InlineKeyboardButton("Token", callback_data='token_'),
#                ]]))

#    elif query.data == 'mobile_':
#        await pw_mobile(app, query.message)

#    elif query.data == 'token_':
#        await pw_token(app, query.message)
        







  

    elif query.data == "give_trial":
            user_id = query.from_user.id
       #     has_free_trial = await db.check_trial_status(user_id)
            if has_free_trial:
                await query.answer("🚸 ʏᴏᴜ'ᴠᴇ ᴀʟʀᴇᴀᴅʏ ᴄʟᴀɪᴍᴇᴅ ʏᴏᴜʀ ꜰʀᴇᴇ ᴛʀɪᴀʟ ᴏɴᴄᴇ !\n\n📌 ᴄʜᴇᴄᴋᴏᴜᴛ ᴏᴜʀ ᴘʟᴀɴꜱ ʙʏ : /plans", show_alert=True)
                return
            else: 
          #     await db.give_free_trial(user_id)
                await query.answer("🥳 ᴄᴏɴɢʀᴀᴛᴜʟᴀᴛɪᴏɴꜱ\n\n🎉 ʏᴏᴜ ᴄᴀɴ ᴜsᴇ ꜰʀᴇᴇ ᴛʀᴀɪʟ ꜰᴏʀ <u>5 ᴍɪɴᴜᴛᴇs</u> ꜰʀᴏᴍ ɴᴏᴡ !", show_alert=True)
                

  
    elif query.data == "premium_":
            button = [[
              InlineKeyboardButton(' ʙʀᴏɴᴢᴇ ', callback_data='bronze_'),
              InlineKeyboardButton(' ꜱɪʟᴠᴇʀ ', callback_data='silver_')
            ],[
              InlineKeyboardButton(' ɢᴏʟᴅ ', callback_data='gold_'),
              InlineKeyboardButton(' ᴏᴛʜᴇʀ ', callback_data='other_')
            ],[            
              InlineKeyboardButton(' ʙ ᴀ ᴄ ᴋ ', callback_data='home_')
            ]]
        
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.PLANS_TXT,
             reply_markup=reply_markup
            )
            
    
          
    elif query.data == "bronze_":
            button = [[
              InlineKeyboardButton('🔐 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', callback_data='purchase')
            ],[
              InlineKeyboardButton('⋞', callback_data='other_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='silver_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.BRONZE_TXT,
             reply_markup=reply_markup             
            )

    elif query.data == "silver_":
            button = [[
              InlineKeyboardButton('🔐 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', callback_data='purchase_')
            ],[
              InlineKeyboardButton('⋞', callback_data='bronze_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='gold_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.SILVER_TXT,
             reply_markup=reply_markup             
            )
            
    elif query.data == "gold_":
            button = [[
              InlineKeyboardButton('🔐 ʙᴜʏ ᴘʀᴇᴍɪᴜᴍ', callback_data='purchase')
            ],[
              InlineKeyboardButton('⋞', callback_data='silver_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='other_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.GOLD_TXT,
             reply_markup=reply_markup
            )
      
    elif query.data == "other_":
            button = [[
              InlineKeyboardButton('☎️ ᴄᴏɴᴛᴀᴄᴛ ', user_id=int(OWNER_ID))
            ],[
              InlineKeyboardButton('⋞', callback_data='gold_'),
              InlineKeyboardButton('ʙ ᴀ ᴄ ᴋ', callback_data='premium_'),
              InlineKeyboardButton('⋟', callback_data='bronze_')
            ]]
      
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.OTHER_TXT,
             reply_markup=reply_markup         
            )

    elif query.data == "purchase_":
            button = [[
                          InlineKeyboardButton('ᴘᴀʏᴍᴇɴᴛ ꜱᴄʀᴇᴇɴꜱʜᴏᴛ', user_id=int(OWNER_ID))

                      ],[
                          InlineKeyboardButton('𝐁 𝐀 𝐂 𝐊', callback_data='premium_')
                      ]]
          
            reply_markup = InlineKeyboardMarkup(button)
            await query.message.edit_text(
             text=script.PAYMENT_TXT,
             reply_markup=reply_markup,           
            )

  

  

    elif query.data=="close_data":
        await query.message.delete()
        await query.message.reply_to_message.delete()



