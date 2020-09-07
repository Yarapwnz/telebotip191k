import telebot

bot = telebot.TeleBot("746507398:AAEDwt0YWwuulCL2F3GrWm9FiVRXDQrjSvk")

@bot.message_handler(commands=['start'])
def start_message(message):
    use_markup = telebot.types.ReplyKeyboardMarkup(True)
    use_markup.row('Реквізити')
    use_markup.row('Розклад дзвінків', 'Розклад і особистий кабінет')
    use_markup.row('Дистанційне навчання', 'Відвідування')
    use_markup.row('Пари', 'Викладачі')
    bot.send_message(message.from_user.id,'Хеллоу',reply_markup=use_markup)

@bot.message_handler(content_types=['text'])
def send_text(message):
    if message.text == 'Розклад дзвінків':
        bot.send_message(message.from_user.id, '1 пара - 9:00 - 10:20 \n2 пара - 10:30 - 11:50 \n3 пара - 12:00 - 13:20 \n4 пара - 13:40 - 15:00 \n5 пара - 15:10 - 16:30 ')
    elif message.text == 'Розклад і особистий кабінет':
        bot.send_message(
            message.from_user.id, 'Перейди по посиланню - http://194.44.112.6')
    elif message.text == 'Дистанційне навчання':
        bot.send_message(
            message.from_user.id, 'Перейди по посиланню - http://pz.nung.edu.ua/moodle/')
    elif message.text == 'Відвідування':
        bot.send_message(
            message.from_user.id, 'Перейди по посиланню - https://docs.google.com/spreadsheets/d/1LH1-rZ72c4JiK2E-ZmlOC0IyxeeuDz_eqeWg3fRHDlM/edit?usp=sharing')
    elif message.text == 'Реквізити':
        bot.send_message(
            message.from_user.id, 'Перейди по посиланню - http://nung.edu.ua/department/іпо/реквізити-для-оплати')
    elif message.text == 'Пари':
        bot.send_message(
            message.from_user.id, 'Аналіз до вимог програмного забезпечення - https://t.me/joinchat/DzFo_RiV3cO7AoJtuXvyUg \nІнтелектуальні системи аналізу даних - https://t.me/joinchat/HMyeslUPZgrp1kRPEa9aNg \nПаралельне програмування - https://t.me/joinchat/GZaQJRusl4EpVi4PIGdy_g')
    elif message.text == 'Викладачі':
        bot.send_message(
            message.from_user.id, 'Аналіз вимог до ПЗ - Храбатин Роман Ігорович - +380997003330 - r.khrabatyn@nung.edu.ua \n\nІнтелектуальні системи аналізу даних - Яцишин Микола Миколайович - +380 66 743 99 60 - yatsyshyn@gmail.com \n\nКПЗ - Шекета Василь Іванович - +380 97 337 64 02 - vasylsheketa@gmail.com \n\nЕмпіричні методи програмної інженерії - Незамай Борис Сергійович - +380 96 777 52 11 -\n\nПаралельне програмування - Тимків Дмитро Федорович - 0993639490 \nЧесановський Микола Станіславович - +380 93 065 20 38 \n\nМенеджмент проектів програмного забезпечення - Вовк Роман Богданович - Телеграм: @Vovk_R - r.vovk@nung.edu.ua ')

bot.polling()
