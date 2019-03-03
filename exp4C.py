text = "7562000074315f377334775f625f376e337455727230665f6234336300216531"
pw = ""
for i in range(0,len(text),8):
    pw+= text[i+6:i+8] + text[i+4:i+6] + text[i+2:i+4] + text[i:i+2]
print(pw)
print(pw.decode("hex"))
