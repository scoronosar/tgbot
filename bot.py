import telebot # сама библиотека telebot
import time # необходим для cрока /mute и автоматического размута после срока мута
import random
import openai
openai.api_key = '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'
bot = telebot.TeleBot("6300333526:AAHSM9qd0V9cT6qOnRHULwiR9bKtF9GtWlw") # в TOKEN мы вводим непосредственно сам полученный токен.
stats = {}
marrypos = [1 , 3 , 5 , 7 , 9]
marrypos1 = [0 , 2 , 4, 6 , 8]
kids = []
boy = [
    'абсос',
    'аваз',
    'АЛЕКСАНДР',
    'серГЕЙ',
    'Василий',
    'арвидик',
    'олег',
    'абибос',
    'Эгей',
    'миста',
    'али',
    'ким пак чимин',
    'эвернасрал',
    'маленький педик',
    'сын пидорасов',
    'аналик',
    'маленькихуй',
    'негрик',
    'рабик',
    'гитлер'
]
bad_words = ['расстрелять', 'ссылка', 'лох', 'олег', 'алек', 'израиль' , 'нахуй' , 'хуй', 'заебал' , 'китайский' , 'ебет']
married = []

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Я бот который ебёт масрура. Напиши /help, чтобы узнать, что я умею.")

@bot.message_handler(commands=['help'])
def help(message):
    bot.reply_to(message, "/kick - кикнуть пользователя\n/mute - замутить пользователя на определенное время\n/unmute - размутить пользователя\n/stats - показать статистику чата\n/selfstat - показать свою статистику")

@bot.message_handler(commands=['marry', 'брак'])
def marry(message):
    if (message.reply_to_message.from_user.username not in married) and (message.from_user.first_name not in married):
        married.append(message.from_user.first_name)
        married.append(message.reply_to_message.from_user.first_name)
        bot.send_message(message.chat.id, f"Поздравляем молодожён, {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} теперь официально поженились")
    else:
        bot.send_message(message.chat.id, 'брак не может быть заключён так как одна из сторон уже находится в браке')

@bot.message_handler(commands=['married', 'браки'])
def marrie(message):
    for i in range (0,len(married),2):
        bot.send_message(message.chat.id, f"{married[i]} and {married[i+1]}")

@bot.message_handler(commands=['fuck_wife', 'выебать_жену'])
def fuck_wife(message):
    if (message.from_user.first_name in married) and (message.reply_to_message.from_user.first_name in married):
        index1 = married.index(message.from_user.first_name)
        index2 = married.index(message.reply_to_message.from_user.first_name)
        if (index1 in marrypos) and (index2 in marrypos1):
            if index1-index2 == 1:
                a = random.randint(1,10)
                if a == 5: 
                    b = random.randint(1,len(boy))
                    bot.send_message(message.chat.id, f"Поздровляем {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} с мальчиком")
                elif a == 8:
                    b = random.randint(1,len(boy))
                    bot.send_message(message.chat.id, f"Поздровляем {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} с девочкой")   
                else:
                    bot.send_message(message.chat.id, f"видимо {message.from_user.first_name} не так сильно старался")
            else:
                bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} не является вашей женой")
        elif (index2 in marrypos) and (index1 in marrypos1):
            if index2-index1 == 1:
                married.pop(index1)
                married.pop(index2-1)
                bot.send_message(message.chat.id, f"Как бы сложно это бы не было но факт есть факт, {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} теперь официально растались 💔")  


@bot.message_handler(commands=['divorce', 'развод'])
def divorc(message):
    if (message.from_user.first_name in married) and (message.reply_to_message.from_user.first_name in married):
        index1 = married.index(message.from_user.first_name)
        index2 = married.index(message.reply_to_message.from_user.first_name)
        if (index1 in marrypos) and (index2 in marrypos1):
            if index1-index2 == 1:
                married.pop(index1)
                married.pop(index2)
                bot.send_message(message.chat.id, f"Как бы сложно это бы не было но факт есть факт, {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} теперь официально растались 💔")
            else:
                bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} не является вашей женой")
        elif (index2 in marrypos) and (index1 in marrypos1):
            if index2-index1 == 1:
                married.pop(index1)
                married.pop(index2-1)
                bot.send_message(message.chat.id, f"Как бы сложно это бы не было но факт есть факт, {message.reply_to_message.from_user.first_name} и {message.from_user.first_name} теперь официально растались 💔")
            else:
                bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} не является вашей женой")
        else:
            bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} не является вашей женой")    
    else:
        bot.send_message(message.chat.id, f"{message.reply_to_message.from_user.first_name} не является вашей женой")           

@bot.message_handler(commands=['kick'])
def kick_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно кикнуть администратора.")
        else:
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} был кикнут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите кикнуть.")

@bot.message_handler(commands=['masrur', 'масрур'])
def welcome(message):
    mesg = bot.send_message(message.chat.id,'вы включили masrurgpt ')
    bot.register_next_step_handler(mesg,chatgpt)


def chatgpt(message):
    response = openai.Completion.create(
        model = 'text-davinci-003',
        prompt = message.text,
        temperature = 0.5,
        max_tokens = 1000,
        top_p = 1.0,
        frequency_penalty = 0.5,
        presence_penalty = 0.5
    )
    gpt_text = response['choices'][0]['text']
    bot.send_message(message.chat.id, gpt_text)


@bot.message_handler(commands=['mute'])
def mute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        user_status = bot.get_chat_member(chat_id, user_id).status
        if user_status == 'administrator' or user_status == 'creator':
            bot.reply_to(message, "Невозможно замутить администратора.")
        else:
            duration = 60 # Значение по умолчанию - 1 минута
            args = message.text.split()[1:]
            if args:
                try:
                    duration = int(args[0])
                except ValueError:
                    bot.reply_to(message, "Неправильный формат времени.")
                    return
                if duration < 1:
                    bot.reply_to(message, "Время должно быть положительным числом.")
                    return
                if duration > 1440:
                    bot.reply_to(message, "Максимальное время - 1 день.")
                    return
            bot.restrict_chat_member(chat_id, user_id, until_date=time.time()+duration*60)
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} замучен на {duration} минут.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите замутить.")

@bot.message_handler(commands=['unmute'])
def unmute_user(message):
    if message.reply_to_message:
        chat_id = message.chat.id
        user_id = message.reply_to_message.from_user.id
        bot.restrict_chat_member(chat_id, user_id, can_send_messages=True, can_send_media_messages=True, can_send_other_messages=True, can_add_web_page_previews=True)
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.username} размучен.")
    else:
        bot.reply_to(message, "Эта команда должна быть использована в ответ на сообщение пользователя, которого вы хотите размутить.")

@bot.message_handler(commands=['stats'])
def chat_stats(message):
    chat_id = message.chat.id
    if chat_id not in stats:
        bot.reply_to(message, "Статистика чата пуста.")
    else:
        total_messages = stats[chat_id]['total_messages']
        unique_users = len(stats[chat_id]['users'])
        bot.reply_to(message, f"Статистика чата:\nВсего сообщений: {total_messages}\nУникальных пользователей: {unique_users}")

@bot.message_handler(commands=['mention', 'упомянуть'])
def mention(message):
    bot.send_message(message.chat.id, "@CurlyFromMSU @kataki_kamitu_kashi @alkash3001 @anxxlrw @T1murxgod @just_madd @Sie_Johan @vxmever")

@bot.message_handler(commands=['selfstat'])
def user_stats(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    username = message.from_user.username
    if chat_id not in stats:
        bot.reply_to(message, "Статистика чата пуста.")
    else:
        if user_id not in stats[chat_id]['users']:
            bot.reply_to(message, "Вы еще не отправляли сообщений в этом чате.")
        else:
            user_messages = stats[chat_id]['users'][user_id]['messages']
            total_messages = stats[chat_id]['total_messages']
            percentage = round(user_messages / total_messages * 100, 2)
            bot.reply_to(message, f"Статистика для пользователя @{username}:\nВсего сообщений: {user_messages}\nПроцент от общего количества сообщений: {percentage}%")


@bot.message_handler()
def fuck(message):
    if message.text.lower() == 'fuck' or message.text.lower() == 'выебать':
        a = random.randint(1,3) 
        if a == 1:
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был износилован")
        elif a == 2:
            bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был износилован в жопу")
        elif a == 3:
            bot.reply_to(message, f"{message.reply_to_message.from_user.first_name} не повезло его кострировали и вебали его же пенисом")
    elif message.text.lower() == "fuck easy" or message.text.lower() == "выебать слабо":
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был износилован")
    elif message.text.lower() == "fuck medium" or message.text.lower() == "выебать средне":
        bot.reply_to(message, f"Пользователь {message.reply_to_message.from_user.first_name} был износилован в жопу")
    elif message.text.lower() == 'fuck hard' or message.text.lower() == 'выебать жестко':
        bot.reply_to(message, f"{message.reply_to_message.from_user.first_name} не повезло его кострировали и вебали его же пенисом")

bot.polling(none_stop=True) #обязательная для работы бота часть