import os, logging, asyncio

from telegraph import upload_file

from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("TOKEN")
decodebot = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

moment_worker = []


#start
@decodebot.on(events.NewMessage(pattern="^/kontolgaceng$"))
async def start(event):
  await event.reply("^ _ ^ Hai, Selamat Datang di TAG Menu Bantuan Bot\nSaya dapat menandai 15.000 Anggota di Grup dan 300 Anggota Di Saluran.\nPerlu Bantuan /help ",
                    buttons=(
                      [
                         Button.url('📣 UPDATES', 'https://t.me/sintureveryday'), 
                         Button.url('⭐SUPPORT', 'https://t.me/pantekyks'), 
                      ], 
                      [
                        Button.url('➕  Tambahkan Saya Ke Group Anda', 'https://t.me/OukeenMusicBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#help
@decodebot.on(events.NewMessage(pattern="^/idiotanjing$"))
async def help(event):
  helptext = "**Menu Bantuan Bot Bantuan Tag**\n\nPerintah: /all \n Anda dapat menggunakan perintah ini dengan teks yang ingin Anda sampaikan kepada orang lain. \n`Contoh: /all Selamat pagi!` \nAnda dapat menggunakan perintah ini sebagai jawaban. pesan apa pun Bot akan menandai pengguna untuk membalas Pesan
  await event.reply(helptext,
                    buttons=(
                      [
                         Button.url('📣 UPDATES', 'https://t.me/sintureveryday'), 
                         Button.url('⭐SUPPORT', 'https://t.me/pantekyks'), 
                      ], 
                      [
                        Button.url('➕ TAMBAH SAYA KE GROUP MU', 'https://t.me/OukeenMusicBot?startgroup=true'),   
                      ]
                   ), 
                    link_preview=False
                   )

#Wah bhaiya full ignorebazzi

#bsdk credit de dena verna maa chod dege

#tag
@decodebot.on(events.NewMessage(pattern="^/tagall|/call|/tall|/all|#all|@all?(.*)"))
async def mentionall(event):
  global moment_worker
  if event.is_private:
    return await event.respond("Gunakan Ini Di Group Atau Channel Anda")
  
  admins = []
  async for admin in decodebot.iter_participants(event.chat_id, filter=ChannelParticipantsAdmins):
    admins.append(admin.id)
  if not event.sender_id in admins:
    return await event.respond("Hanya Admin Yang Dapat Menggunakan Ini.")
  
  if event.pattern_match.group(1):
    mode = "text_on_cmd"
    msg = event.pattern_match.group(1)
  elif event.reply_to_msg_id:
    mode = "text_on_reply"
    msg = event.reply_to_msg_id
    if msg == None:
        return await event.respond("Saya tidak dapat Menyebut Anggota untuk Postingan Lama!")
  elif event.pattern_match.group(1) and event.reply_to_msg_id:
    return await event.respond("Beri saya bisa Argumen. Contoh: `/tag Hei, Dimana kamu`")
  else:
    return await event.respond("Balas Pesan atau Berikan Beberapa Teks Untuk Disebutkan!")
    
  if mode == "text_on_cmd":
    moment_worker.append(event.chat_id)
    usrnum = 0
    usrtxt = ""
    async for usr in decodebot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped!")
        return
      if usrnum == 5:
        await decodebot.send_message(event.chat_id, f"{usrtxt}\n\n{msg}")
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""
        
  
  if mode == "text_on_reply":
    moment_worker.append(event.chat_id)
 
    usrnum = 0
    usrtxt = ""
    async for usr in decodebot.iter_participants(event.chat_id):
      usrnum += 1
      usrtxt += f"[{usr.first_name}](tg://user?id={usr.id}) "
      if event.chat_id not in moment_worker:
        await event.respond("Stopped")
        return
      if usrnum == 5:
        await decodebot.send_message(event.chat_id, usrtxt, reply_to=msg)
        await asyncio.sleep(2)
        usrnum = 0
        usrtxt = ""


# Cancle 

@decodebot.on(events.NewMessage(pattern="^/cancel$"))
async def cancel_spam(event):
  if not event.chat_id in spam_chats:
    return await event.respond('__There is no proccess on going...__')
  else:
    try:
      spam_chats.remove(event.chat_id)
    except:
      pass
    return await event.respond('**__Stoped__**\n\n**__Powered By:__ @sintureveryday**')




print("Started Successfully Join Support")
print("¯\_(ツ)_/¯ Need Help? Usaha Kontol")
decodebot.run_until_disconnected()
