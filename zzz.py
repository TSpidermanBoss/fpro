import logging
import telegram
import time
import random
from telegram import ParseMode
from telegram.ext import MessageHandler, Filters, Updater
from telegram.ext import CommandHandler
updater = Updater(token='1179939004:AAFb61k5P_tjBY1fZkA47LcnhmXPcW-3XcA')
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

def toss(bot,update):
   member = update.effective_message.chat.get_member(update.effective_message.from_user.id)
   if member.status == "administrator" or member.status=='creator':
      x = random.choice(['💫 Result : Head', '💫 Result :Tail '])
      y = random.choice(['💫 Result : Head', '💫 Result :Tail ','💫 Result : Head','💫 Result :Tail '])
      z = random.choice(['💫 Result :Tail ','💫 Result : Head','💫 Result :Tail ', '💫 Result : Head'])
      r = random.choice([x,z,y])
      a = update.message.reply_text("*" + r  + "*",parse_mode=telegram.ParseMode.MARKDOWN)

def show(bot,update):
  member = update.effective_message.chat.get_member(update.effective_message.from_user.id)
  if member.status == "administrator" or member.status=='creator':
   if len(update.effective_message.text.split(' ')) > 1:
     z = ["2♠️","3♠️","4♠️","5♠️","6♠️","7♠️","8♠️","9♠️","10♠️","𝔸♠️","ℚ♠️","𝕁♠️","𝕂♠️","2♣️","3♣️","4♣️","5♣️","6♣️","7♣️","8♣️","9♣️","10♣️","𝔸♣️","ℚ♣️","𝕁♣️","𝕂♣️","2♥️","3♥️","4♥️","5♥️","6♥️","7♥️","8♥️","9♥️","10♥️","𝔸♥️","ℚ♥️","𝕁♥️","𝕂♥️","2♦️","3♦️","4♦️","5♦️","6♦️","7♦️","8♦️","9♦️","10♦️","𝔸♦️","ℚ♦️","𝕁♦️","𝕂♦️"]
     a = random.choice(z)
     z.remove(a)
     b = random.choice(z)
     z.remove(b)
     c = random.choice(z)
     z.remove(c)
     d = random.choice(z)
     z.remove(d)
     e = random.choice(z)
     z.remove(e)
     f = random.choice(z)           
     update.message.reply_text("*Player " + update.message.text.split(" ")[1]+ """ Cards:

  """  + a  + "    "+ b + "     " + c + "*", parse_mode=ParseMode.MARKDOWN )	
     update.message.reply_text("*Player " + update.message.text.split(" ")[2]+ """ Cards:

  """  + d + "     "+ e + "     " + f + "*", parse_mode=ParseMode.MARKDOWN )
   else:
        update.message.reply_text('Please write username {without @} after command!')
		
def ball(bot,update):
   member = update.effective_message.chat.get_member(update.effective_message.from_user.id)
   if member.status == "administrator" or member.status=='creator':
    if len(update.effective_message.text.split(' ')) > 1:
      x = random.choice(["3","2","4","3","2","1","2","3","2","4","6"])
      y = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
      z = random.choice(["🅾 Dot Ball 🅾","🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
      r = random.choice([x,z,x,z,y,x])
      update.message.reply_text("*Ball 0.{} 🎾: ".format(update.message.text.split(' ')[1]) + r.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣")  + "*" ,parse_mode=telegram.ParseMode.MARKDOWN)
    else:
      update.message.reply_text('Please write ball number after command!')

            
def over(bot,update):
   member = update.effective_message.chat.get_member(update.effective_message.from_user.id)
   if member.status == "administrator" or member.status=='creator':
    k = update.effective_message.text.split(' ')
    if len(k) > 1:
      if len(k) <= 2:
       k.insert(2,"10")
      if len(k) <= 3:
       k.insert(3,"1000")
      q = float(0.1)
      p = float(0)
      s = float(0)
      f = float(0)
      while True:
        x = random.choice(["2","1","3","2","1","3","1","2","6","1","4","3","1","6","2","4","3","2","1","2"])
        y = random.choice(['7','8','9'])
        z = random.choice(['11','12','13'])
        r = random.choice([x,x,z,x,z,x,x,y,x,x,x,x])
        if r == z:
         v = random.choice(["🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
         update.message.reply_text("*Ball " + str(q)+ "🎾" + ": " + v + "*",parse_mode=ParseMode.MARKDOWN)
         f = float(f) + float(1)
         s = float(s) + float(1)
        if r == x:
         update.message.reply_text("*Ball " + str(q) + "🎾: " + x.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣").replace("0","🅾 Dot Ball 🅾")+ "*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
         f = float(f) + float(r)
        if r == y:
         l = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
         update.message.reply_text("*Ball " + str(q) + "🎾" + ": " + l + "*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         p = float(p) + float(1)
         time.sleep(2)
         update.message.reply_text("*" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾*',parse_mode=ParseMode.MARKDOWN)
        if ".7" in str(q):
         q = (float(str(q).replace(".7",""))*1000 + float(1.1)*1000)/1000
         time.sleep(2)
         update.message.reply_text('*' + str(q).replace('.1','') + ' 𝕆𝕍𝔼ℝ '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 🅾🅾
	 
	 𝕊𝕔𝕠𝕣𝕖 𝕥𝕙𝕚𝕤 𝕠𝕧𝕖𝕣 : """ + str(f).replace('.0','') +  """ 🏏🏏
	 
	 𝕊𝕥𝕣𝕚𝕜𝕖 ℝ𝕒𝕥𝕖 : """ + str(round((s/(float(str(q).replace('.1',''))*6))*100,2)) + "*",parse_mode=ParseMode.MARKDOWN)  
         f = float(0)
        if int(str(s).replace('.0','')) >= int(k[3]):
          time.sleep(2)
          update.message.reply_text("* 𝕊𝕔𝕠𝕣𝕖 : " + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 📟📟
              
   🏆 𝕋𝕒𝕣𝕘𝕖𝕥 ℂ𝕙𝕒𝕤𝕖𝕕 𝕎𝕠𝕟 🎉* """ , parse_mode=ParseMode.MARKDOWN)
          time.sleep(2)
          update.message.reply_text("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        if str(p).replace('.0','') == k[2]:
           time.sleep(2)
           update.message.reply_text("🚩🚩 𝕋𝔼𝔸𝕄 𝔸𝕃𝕃 𝕆𝕌𝕋 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
           break
        if str(q).replace('.1','') == k[1]:
          time.sleep(2)
          update.message.reply_text("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        time.sleep(3) 
    else:
      update.message.reply_text('Please write over and players number after command! 10 over ex. /over 10 if max wkt is 5 and target is 100 then /over 10 5 100 to perfect results')
    
def superover(bot,update):
   member = update.effective_message.chat.get_member(update.effective_message.from_user.id)
   if member.status == "administrator" or member.status=='creator':
      q = float(0.1)
      p = float(0)
      s = float(0)
      f = float(0)
      while True:
        x = random.choice(["2","1","3","2","1","3","1","2","6","1","4","3","1","6","2","4","3","2","1","2"])
        y = random.choice(['7','8','9'])
        z = random.choice(['11','12','13'])
        r = random.choice([x,x,z,x,z,x,x,y,x,x,x,x])
        if r == z:
         v = random.choice(["🙅‍♂ No Ball 🙅‍♂","🙆‍♂ Wide Ball 🙆‍♂"])
         update.message.reply_text("*Ball " + str(q)+ "🎾" + ": " + v + "*",parse_mode=ParseMode.MARKDOWN)
         f = float(f) + float(1)
         s = float(s) + float(1)
        if r == x:
         update.message.reply_text("*Ball " + str(q) + "🎾: " + x.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣").replace("0","🅾 Dot Ball 🅾")+ "*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
         f = float(f) + float(r)
        if r == y:
         l = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
         update.message.reply_text("*Ball " + str(q) + "🎾" + ": " + l + "*",parse_mode=ParseMode.MARKDOWN)
         q = (float(q)*1000 + float(0.1)*1000)/1000
         p = float(p) + float(1)
         time.sleep(2)
         update.message.reply_text("*" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾*',parse_mode=ParseMode.MARKDOWN)
        if ".7" in str(q):
         q = (float(str(q).replace(".7",""))*1000 + float(1.1)*1000)/1000
         time.sleep(2)
         update.message.reply_text('*' + str(q).replace('.1','') + ' 𝕆𝕍𝔼ℝ '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 🅾🅾
	 
	 𝕊𝕔𝕠𝕣𝕖 𝕥𝕙𝕚𝕤 𝕠𝕧𝕖𝕣 : """ + str(f).replace('.0','') +  """ 🏏🏏
	 
	 𝕊𝕥𝕣𝕚𝕜𝕖 ℝ𝕒𝕥𝕖 : """ + str(round((s/(float(str(q).replace('.1',''))*6))*100,2)) + "*",parse_mode=ParseMode.MARKDOWN)  
         f = float(0)
        if str(p).replace('.0','') == '2':
           time.sleep(2)
           update.message.reply_text("🚩🚩 𝕋𝔼𝔸𝕄 𝔸𝕃𝕃 𝕆𝕌𝕋 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
           break
        if str(q).replace('.1','') == "1":
          time.sleep(2)
          update.message.reply_text("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        time.sleep(3) 
dispatcher = updater.dispatcher
OVER_HANDLER = CommandHandler("over", over)
SOVER_HANDLER = CommandHandler("superover", superover)
TOSS_HANDLER = CommandHandler("toss",toss)
BALL_HANDLER = CommandHandler("ball",ball)
SHOW_HANDLER = CommandHandler("sw",show)
dispatcher.add_handler(SHOW_HANDLER)
dispatcher.add_handler(OVER_HANDLER)
dispatcher.add_handler(SOVER_HANDLER)
dispatcher.add_handler(TOSS_HANDLER)
dispatcher.add_handler(BALL_HANDLER)
updater.start_polling()
