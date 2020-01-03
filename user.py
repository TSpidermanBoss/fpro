from pyrogram import Client, Filters
import time
from pyrogram.errors import FloodWait
bot = "912776251:AAHfk6nLsg3jivB6IXT-RnLXY3kKkaJsG0A"
u = 1056623492
cnal = -1001359197349
app = Client(session_name="rr",api_id=814511,api_hash="44462f0f278503255d5cc30941b617a9",bot_token = bot)                                                                                
@app.on_message(Filters.chat(cnal) & ~ Filters.edited)
def main(client, message):
 fil = open("des.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
   mes = client.send_message(int(t),message.text.markdown)
   fie = open("idsd.txt","a")
   fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
   fie.close()
@app.on_message(Filters.chat(cnal) & Filters.edited)
def main(client, message):
 fil = open("des.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
   files = open("ids.txt" , "r")
   d = files.readlines()
   files.close()
   for c in d:
    x = c.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(int(t),int(x[x.index(id)+1]),message.text.markdown)
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command('clear') & Filters.user(491634139))
def forward(client, message):
  with open("idsd.txt","w") as fie:
   fie.write("001 002")
   fie.close()
  with open("idss.txt","w") as fie:
   fie.write("001 002")
   fie.close()
   message.reply("☢️ Done, Editing data cleared ✅✅")
@app.on_message(Filters.command("setsorc"))
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
   client.send_message(u,message.text.markdown)
   message.reply("Command Successful! ")
 else:
  message.reply("Invalid destination")
@app.on_message(Filters.command("setdes"))
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
   with open("des.txt","w") as file:
    file.write(message.text.split(' ')[1])
    file.close()
    message.reply("Command Successful! Make bot admin in destination")
 else:
  message.reply("Invalid destination")
@app.on_message(Filters.command("join"))
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 44:
   client.send_message(u,message.text.markdown)
   message.reply("Command Successful! ")
 else:
  message.reply("Invalid Link")


app.run()
