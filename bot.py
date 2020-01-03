from pyrogram import Client, Filters,Emoji
app = Client("122",1115222,"b5d91575831ac4ffb32d6bcc8056f722")
botid = 912776251
cnal = -1001359197349
@app.on_message( Filters.text & ~Filters.edited & Filters.channel)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
    f = False
    words = ['dekho','TRUST','join','fix','😱','😳','👆','👇','☝️','https://','😂','🤔','pass','chase','link','suno','member','❓','loss','audio','open',"report",'paid','contact','baazigar','market','load','whatsapp','book','bhai','🐴','only','chut','tennis','teen','lavde','chutiya','bc','kya','line','LUND','WICKET LU','?','loda','telegram','chor',"kama","lakh",' id','स',"kitna"]
    for word in words:
     if word.casefold() in message.text.casefold():
      return
    mes = client.send_message(cnal,message.text)
    fie = open("idss.txt","a")
    fie.write(" " + str(message.message_id) + " " + str(mes.message_id))
    fie.close()   
@app.on_message( Filters.text & Filters.edited & Filters.channel)
def forward(client, message):
 fil = open("source.txt" , "r")
 lins = fil.readlines()
 fil.close()
 for t in lins:
  if int(t) == message.chat.id:
   file = open("idss.txt" , "r")
   lines = file.readlines()
   file.close()
   for line in lines:
    x = line.split()
    id = str(message.message_id)
    if id in x:
     try:
      client.edit_message_text(cnal,int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
      time.sleep(e.x)
@app.on_message(Filters.command("setsorc") & Filters.user(botid))
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 14:
   with open("source.txt","w") as file:
    file.write(message.text.split(' ')[1])
    file.close()
  message.reply("done bro ₹₹₹₹ ")
@app.on_message(Filters.command("join") & Filters.user(botid))
def forward(client, message):
 if len(message.text.split(' ')) > 1:
  if len(message.text.split(' ')[1]) == 44:
   client.join_chat(message.text.split(' ')[1])
app.run()
