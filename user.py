@app.on_message(Filters.command("setf"))
def forward(client, message):
  with open("source.txt" , "w") as file:
   file.write(message.text.split(' ')[1])
   file.close()
   message.reply("done bro ₹₹₹₹ ")
