import time

import telebot

bot = telebot.TeleBot("5893079574:AAH4dsEBz2d6OsPWJwy4R30sCVoU48JhXq4", parse_mode=None)


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id,  "Howdy, how are you doing?")


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if "how" in message.text.lower() and "you" in message.text.lower():
        bot.send_message(message.chat.id, "Fine, thank you")
    elif "name" in message.text.lower():
        bot.send_message(message.chat.id, "My name is DSA")
    elif message.text=="count":
        for i in range(5,0,-1):
            bot.send_message(message.chat.id, f"Counting... {i}")
            time.sleep(0.5)
        bot.send_message(message.chat.id, "Go")

    elif "titanic" in message.text.lower():
        f=open("titanic.csv")
        name=message.text.lower().split()[1]
        line_number=0
        found=False
        for line in f:
            line_number+=1
            if line_number==1:
                continue
            line=line.strip()
            fields=line.split(",")
            survived=int(fields[1])
            if name.lower() in line.lower():
                bot.send_message(message.chat.id, f"Found {fields[3]}, {fields[4]}")
                found=True
                if survived==1:
                    bot.send_message(message.chat.id, "Survived! Yes!")
                else:
                    bot.send_message(message.chat.id, "Oh No! I am sorry")

        if not found:
            bot.send_message(message.chat.id, "This person is not found")
        f.close()
    else:
        bot.send_message(message.chat.id, "Bye, i don't understand you")








print("Bot started")
bot.infinity_polling()
print("Bot stopped")