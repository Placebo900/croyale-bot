import telebot
from royale import CRoyale, cache

bot = telebot.TeleBot('') # write token

@bot.message_handler(commands=['start', 'help'])
def start(message):
    with open('instruction_help', 'r') as f:
        bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['currentwar'])
def cur_war(message):
    list_msg = message.text.split()
    if len(list_msg) < 2:
        bot.send_message(message.chat.id, "Не написан тэг клана. Напиши /player <тэг клана>")
    elif list_msg[1][0] != '#':
        bot.send_message(message.chat.id, "Невалидный тэг клана. Чтобы было норм напиши так: #<тэг>")
    else:
        cache.c_tag = '%23' + list_msg[1][1:]
        cache.action = 'analyze_current_cw'
        try:
            cache.call_func()
        except:
            bot.send_message('Что-то не то ты ввёл дядя')
        with open('analyze_current_cw', 'r') as f:
            bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['pastwar'])
def cur_war(message):
    list_msg = message.text.split()
    if len(list_msg) < 2:
        bot.send_message(message.chat.id, "Не написан тэг клана. Напиши /player <тэг клана>")
    elif list_msg[1][0] != '#':
        bot.send_message(message.chat.id, "Невалидный тэг клана. Чтобы было норм напиши так: #<тэг>")
    else:
        cache.c_tag = '%23' + list_msg[1][1:]
        cache.action = 'analyze_cw'
        if len(list_msg) == 3:
            try:
                cache.call_func(min_fames=int(list_msg[2]))
            except:
                bot.send_message('Что-то не то ты ввёл дядя')    
        else:
            cache.call_func()
        with open('analyze_cw', 'r') as f:
            bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['donations'])
def donates(message):
    list_msg = message.text.split()
    if len(list_msg) < 2:
        bot.send_message(message.chat.id, "Не написан тэг клана. Напиши /player <тэг клана>")
    elif list_msg[1][0] != '#':
        bot.send_message(message.chat.id, "Невалидный тэг клана. Чтобы было норм напиши так: #<тэг>")
    else:
        cache.c_tag = '%23' + list_msg[1][1:]
        cache.action = 'analyze_donates'
        if len(list_msg) == 3:
            try:
                cache.call_func(min_donates=int(list_msg[2]))
            except:
                bot.send_message('Что-то не то ты ввёл дядя')
        else:
            try:
                cache.call_func()
            except:
                bot.send_message('Что-то не то ты ввёл дядя')
        with open('analyze_donates', 'r') as f:
            bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['player'])
def donates(message):
    list_msg = message.text.split()
    if len(list_msg) < 2:
        bot.send_message(message.chat.id, "Не написан тэг игрока. Напиши /player <тэг игрока>")
    elif list_msg[1][0] != '#':
        bot.send_message(message.chat.id, "Невалидный тэг игрока. Чтобы было норм напиши так: #<тэг>")
    else:
        cache.p_tag = '%23' + list_msg[1][1:]
        cache.action = 'analyze_player'
        try:
            cache.call_func()
        except:
            bot.send_message('Что-то не то ты ввёл дядя')
        with open('analyze_player', 'r') as f:
            bot.send_message(message.chat.id, f.read())

@bot.message_handler(commands=['chests'])
def donates(message):
    list_msg = message.text.split()
    if len(list_msg) < 2:
        bot.send_message(message.chat.id, "Не написан тэг игрока. Напиши /player <тэг игрока>")
    elif list_msg[1][0] != '#':
        bot.send_message(message.chat.id, "Невалидный тэг игрока. Чтобы было норм напиши так: #<тэг>")
    else:
        cache.p_tag = '%23' + list_msg[1][1:]
        cache.action = 'analyze_chests'
        try:
            cache.call_func()
        except:
            bot.send_message('Что-то не то ты ввёл дядя')
        with open('analyze_chests', 'r') as f:
            bot.send_message(message.chat.id, f.read())

bot.infinity_polling()
