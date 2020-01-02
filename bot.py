from pyrogram import Client, Filters,Emoji
app = Client("mcc",715451,"d2cba6f7bf5d1a45682da5bb9071a307")
k = -1001453099412
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
     mes = client.send_message(k,message.text)
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
      client.edit_message_text(k,int(x[x.index(id)+1]),message.text)
     except FloodWait as e:
      time.sleep(e.x)
app.run()
