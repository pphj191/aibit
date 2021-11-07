import telegram
bot = telegram.Bot ( token = '2136028119:AAHsCZhog6EjbNeyP-UwQrZHpgQTrkanjaw')

def send(text):    
    bot.sendMessage(chat_id = 1822676454 , text=text)

# for i in bot.getUpdates():
#     print(i.message)
def receive(text):
    pass

if __name__=="__main__":
    send("Hi my name")