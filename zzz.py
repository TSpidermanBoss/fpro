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
         message.reply("**Ball " + str(q)+ "🎾" + ": " + v + "**")
         f = float(f) + float(1)
         s = float(s) + float(1)
        if r == x:
         message.reply("**Ball " + str(q) + "🎾: " + x.replace("2","2⃣ Double 2⃣").replace("3","3⃣ Three 3⃣").replace("4","4⃣ Four 4⃣").replace("6","6⃣ Six Gya Six 6⃣").replace("1","1⃣ Single 1⃣").replace("0","🅾 Dot Ball 🅾")+ "**")
         q = (float(q)*1000 + float(0.1)*1000)/1000
         s = float(s) + float(r)
         f = float(f) + float(r)
        if r == y:
         l = random.choice(["🚾 Run out 🚾","🚾 Catch out 🚾","🚾 Wicket 🚾"])
         message.reply("**Ball " + str(q) + "🎾" + ": " + l + "**")
         q = (float(q)*1000 + float(0.1)*1000)/1000
         p = float(p) + float(1)
         time.sleep(2)
         message.reply("**" + str(s).replace('.0','') + '/' + str(p).replace('.0','') + '🚾**')
        if ".7" in str(q):
         q = (float(str(q).replace(".7",""))*1000 + float(1.1)*1000)/1000
         time.sleep(2)
         message.reply('**' + str(q).replace('.1','') + ' 𝕆𝕍𝔼ℝ '  + str(s).replace('.0','') + '/' + str(p).replace('.0','') + """ 🅾🅾
	 
	 𝕊𝕔𝕠𝕣𝕖 𝕥𝕙𝕚𝕤 𝕠𝕧𝕖𝕣 : """ + str(f).replace('.0','') +  """ 🏏🏏
	 
	 𝕊𝕥𝕣𝕚𝕜𝕖 ℝ𝕒𝕥𝕖 : """ + str(round((s/(float(str(q).replace('.1',''))*6))*100,2)) + "**")  
         f = float(0)
        if str(p).replace('.0','') == update.message.text.split(" ")[2]:
           time.sleep(2)
           message.reply("🚩🚩 𝕋𝔼𝔸𝕄 𝔸𝕃𝕃 𝕆𝕌𝕋 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
           break
        if str(q).replace('.1','') == update.message.text.split(" ")[1]:
          time.sleep(2)
          message.reply("🚩🚩 𝔾𝔸𝕄𝔼 𝕆𝕍𝔼ℝ 🚩🚩")
          break
        time.sleep(3) 
