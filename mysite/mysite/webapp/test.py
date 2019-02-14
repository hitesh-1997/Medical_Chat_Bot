import aiml

bot = aiml.Kernel()
bot.learn("std-startup.xml")
bot.respond("load aiml c")
c = 1
while (c):
    print bot.respond("pain")
    c = c-1
    while True:
        print  bot.respond(raw_input("> "),)+ 'asd'
        print 'ans'  + 'uio'
        
    



