import telebot
import config
import dbworker

bot = telebot.TeleBot(config.token)
available_sign = ["козерог", "водолей", "рыбы", "овен", "телец", "близнецы", "рак", "лев", "дева", "весы", "скорпион", "стрелец"]
winx =['лейла', 'стела', 'муза', 'флора', 'техна', 'блум', 'не люблю винкс']
token = '5048990230:AAH2MovxsbqssKT6kMMdbNf01R6S_B0idRc'
bot = telebot.TeleBot(token)



@bot.message_handler(commands=["cancel"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "не хочешь развлекух - как хочешь, переходи в /menu")
    dbworker.set_state(message.chat.id, config.States. S_START.value)


@bot.message_handler(commands=["reset"])
def cmd_reset(message):
    bot.send_message(message.chat.id, "ну что это такое.. минус 10 очков за такое надо...\n представляйся ещё раз")
    dbworker.set_state(message.chat.id, config.States.STATE_FIRST_NUM.value)

# Начало диалога
@bot.message_handler(commands=['love'])
def cmd_start(message):
    bot.send_message(message.chat.id, "смело! но если захочешь выйти из этого режима - /cancel поможет\nначать заполнять заново - /reset\nкак к тебе обращаться?")
    dbworker.set_state(message.chat.id, config.States.STATE_FIRST_NUM.value)

# По команде /reset будем сбрасывать состояния, возвращаясь к началу диалога


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_FIRST_NUM.value)
def user_entering_name(message):
    if not message.text.isalpha():
        bot.send_message(message.chat.id, "не дури меня! не очень на имя похоже! давай из буковок")
        return
    else:
        bot.send_message(message.chat.id, "хорошо, теперь твой знак зодиака...")
        dbworker.set_state(message.chat.id, config.States.STATE_SECOND_NUM.value)


@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_SECOND_NUM.value)
def user_entering_sign(message):
    # А вот тут сделаем проверку
    if message.text.lower() not in available_sign:
        bot.send_message(message.chat.id, "ну давай, честно, выбери зз! из всего 12, ты справишься!")
        return
    else:
        if message.text.lower() == 'овен' or message.text.lower() =='лев' or message.text.lower() =='рыбы':
            bot.send_message(message.chat.id, "нууу, шансов у нас мало, но глянем, что дальше!")
        if message.text.lower() == 'рак' or message.text.lower() == 'водолей' or message.text.lower() == 'весы':
            bot.send_message(message.chat.id, "уже кайфую")
        if message.text.lower() == 'козерог':
            bot.send_message(message.chat.id, "это мой!!! ладно, видимо твой тоже")

        keyboard = telebot.types.ReplyKeyboardMarkup(True)
        for fairy in winx:
            keyboard.add(fairy)
        bot.send_message(message.chat.id, "последний шаг! выбери люимую фею винкс", reply_markup=keyboard)
        dbworker.set_state(message.chat.id, config.States.STATE_THIRD_NUM.value)

@bot.message_handler(func=lambda message: dbworker.get_current_state(message.chat.id) == config.States.STATE_THIRD_NUM.value)
def user_fairy(message):
    if message.text.lower() not in winx:
        bot.send_message(message.chat.id, "знаю, сложно,но феечку надо выбрать")
        return
    else:
        bot.send_message(message.chat.id, "мммм, интересненько")
        dbworker.set_state(message.chat.id, config.States.S_START.value)
        bot.send_message(message.chat.id, "это конец тестика, подведём результаты! хммммммммм")
        if message.text.lower() == 'не люблю винкс':
            bot.send_message(message.chat.id, "сори, но если ты не любишь винкс - то это сразу 0%")
        else:
            bot.send_message(message.chat.id, "ты самый крутой перец, независимо от ответов! переходи в /menu")


@bot.message_handler(commands=['start'])
def stt_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    buttons = ["/menu"]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, 'Привет, молодёжь! Ну или как у вас принято говорить - привет-медвед, молодёжь!', reply_markup=keyboard)

@bot.message_handler(commands=['menu'])
def start_message(message):
    keyboard = telebot.types.ReplyKeyboardMarkup(True)
    buttons = ["анекдот", "пока", "/test", "/love"]
    keyboard.add(*buttons)
    bot.send_message(message.chat.id, ' Хочешь попрощаться - нажми "пока"\nХочешь интерактива - нажми "/test"\nХочешь пройти тест на крутость - нажми "/love"\nНу и анекдот, думаю, понятно) ', reply_markup=keyboard)


@bot.message_handler(commands=['test'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='вероника-голубика', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='вероника-ежевика', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='вероника-облепиха', callback_data=3))
    bot.send_message(message.chat.id, text="ииинтерактивчик! какую Веронику хочешь увидеть?", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text.lower() == 'анекдот':
        bot.send_message(message.chat.id, 'Анекдот №186:\nКолобок повесился')
    elif message.text.lower() == 'пока':
        bot.send_message(message.chat.id, 'Досвидули, досвидули, досвидули-дули-дули!')
    elif message.text.lower() == 'песню!':
        bot.send_message(message.chat.id, 'ху ху, ну держи, повайбь')
        bot.send_message(message.chat.id, 'https://open.spotify.com/track/7EkWXAI1wn8Ii883ecd9xr?si=51LCrMbFTSyESuTgHBoCGg&utm_source=copy-link')
    else:
        bot.send_message(message.chat.id, 'не понимаю, о чём ты')

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):
    if call.data == '1':
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1mxv16SxLnSrX22nboqguxc06M0kBFv_G/view?usp=drivesdk')
    elif call.data == '2':
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1CzNb6C_7WHeeXkol0QQ5hZzs03c9-Srd/view?usp=drivesdk')
    elif call.data == '3':
        bot.send_photo(call.message.chat.id, 'https://drive.google.com/file/d/1ZQY9LXfqjOpDgGD8pqpoJDOhprPXe2FX/view?usp=drivesdk')

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)

bot.polling()
