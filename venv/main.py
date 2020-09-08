import telebot
import time
import threading
from user import *
from config import TOKEN

bot = telebot.TeleBot(TOKEN)
running = False
answers = {}
notifys = {}
admin = "000000000"#Admin's ID

def convert_time(text):
    times = text.split(':')
    sec = 0
    if times[0] != '':
        sec += int(times[0]) * 3600
    if times[1] and times[1] != '':
        sec += int(times[1]) * 60
    if times[2] and times[2] != '':
        sec += int(times[2])
    return int(sec)

def sender_notify():
    while True:
        time.sleep(1)
        now = time.time()
        for i in notifys:
            for j in range(len(notifys[i])):
                if now >= int(notifys[i][j][0]):
                    bot.send_message(i, f"Напоминаю {str(notifys[i][j][1])}")
                    print(f"Напомнил пользователю {i} про событие: {str(notifys[i][j][1])}")
                    del notifys[i][j]
                    break




@bot.message_handler(content_types=['text'])
def all_messages(msg):
    message = msg.text
    user_id = msg.chat.id
    mess = message.split(" ")
    if str(mess[0]).lower() == "напомни":
        sec = 0
        note = ''
        for i in range(1, len(mess)):
            if sec != 0:
                note += str(mess[i]) + " "
                continue
            if str(mess[i]).find(':') != -1:
                sec += convert_time(mess[i])
                continue
        if sec != 0 and sec > 10 and sec < 90000:
            message = f"таймер \"{note}\" сработает через {int(sec / 60)} минут, {sec % 60} секунд"
            sec += time.time()
            if notifys.get(user_id):
                notifys[user_id].append((int(sec), str(note)))
            else:
                notifys[user_id] = [(int(sec), str(note))]
        else:
            message = "Неверный формат или слишком долго ждать"
    if message == "/start":
        user = User(user_id)
    elif message == "/list":
        if str(user_id) == admin:
            user = User(user_id)
            print(user.get_all_id())
            message = user.get_all_id()
    elif message == "/":
        if str(user_id) == admin:
            print(notifys)
            message = "Смотри в логги"
    bot.send_message(user_id, message)
    return 0

if __name__ == '__main__':
    try:
        thread_polling = threading.Thread(target=bot.polling)
        thread_notyfy = threading.Thread(target=sender_notify)
        thread_notyfy.start()
        thread_polling.start()
    except Exception as e:
        print(e)



