import telebot
import random
from telebot import types


def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(content_types=['text'])
    def send_text(message):
        if message.text.lower() == '/start':
            bot.send_message(
                message.from_user.id,
                f"Приветствую, {message.from_user.first_name}! "
                f"Я Ваш бот-гороскоп"
                f"\n"
                f'\n Выберете свой знак зодиака из приведённого ниже списка, и я предскажу сегодняшнюю судьбу✨"'
                )

            keyboard = types.InlineKeyboardMarkup()
            key_oven = types.InlineKeyboardButton(text='♈ Овен ♈', callback_data='zodiac')
            keyboard.add(key_oven)
            key_telec = types.InlineKeyboardButton(text='♉ Телец ♉', callback_data='zodiac')
            keyboard.add(key_telec)
            key_bliznecy = types.InlineKeyboardButton(text='♊ Близнецы ♊', callback_data='zodiac')
            keyboard.add(key_bliznecy)
            key_rak = types.InlineKeyboardButton(text='♋ Рак ♋', callback_data='zodiac')
            keyboard.add(key_rak)
            key_lev = types.InlineKeyboardButton(text='♌ Лев ♌', callback_data='zodiac')
            keyboard.add(key_lev)
            key_deva = types.InlineKeyboardButton(text='♍ Дева ♍', callback_data='zodiac')
            keyboard.add(key_deva)
            key_vesy = types.InlineKeyboardButton(text='♎ Весы ♎', callback_data='zodiac')
            keyboard.add(key_vesy)
            key_scorpion = types.InlineKeyboardButton(text='♏ Скорпион ♏', callback_data='zodiac')
            keyboard.add(key_scorpion)
            key_strelec = types.InlineKeyboardButton(text='♐ Стрелец ♐', callback_data='zodiac')
            keyboard.add(key_strelec)
            key_kozerog = types.InlineKeyboardButton(text='♑ Козерог ♑', callback_data='zodiac')
            keyboard.add(key_kozerog)
            key_vodoley = types.InlineKeyboardButton(text='♒ Водолей ♒', callback_data='zodiac')
            keyboard.add(key_vodoley)
            key_ryby = types.InlineKeyboardButton(text='♓ Рыбы ♓', callback_data='zodiac')
            keyboard.add(key_ryby)

            bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)

            @bot.callback_query_handler(func=lambda call: call.data == 'zodiac')
            def callback_worker(call):
                # Если нажали на одну из 12 кнопок — выводим гороскоп
                # Формируем гороскоп
                msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(
                    second_add) + ' ' + random.choice(third)
                # Отправляем текст в Телеграм
                bot.send_message(call.message.chat.id, msg)

        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши /start")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")

    bot.polling()


first = ['Сегодняшний день пройдёт хорошо.', 'Сегодня не стоит рисковать, необнуманный поступок не приведёт к хорошим последсвиям.', 'Сегодня прекрасный день для того, чтобы решиться на смелый поступок!', 'Сегодня будьте осторожны, потому что могут произойти непривычные для вас веши.', 'Лучшее время для того, чтобы начать новые дела или разобраться со старыми.', 'Сегодня  лучше ничего не откладывать на завтра и разобраться с накопившимися делами.', 'Новый день - новые начинания! Не сдерживайте вашу фантазию, сегодя она вам пригодится!', 'Сегодня будьте осторожны, неожиданные обстоятельства сегодня вас окружат.']

second = ['Но помните, что лучше сегодня не забывать про', 'Если в планах на сегодня много дел, заранее подумайте про', 'Если вы сегодня нацелены выполнить множество дел, должны помнить про', 'Если у вас сегдня продуктивный день, вспомните про', 'Если у вас сегдня день лени, вспомните про', 'Если вы уже беспокоитесь на счёт завтрашнего, успокойтесь и подумайте про', 'Помните, что нужно следить и не забывать про']

second_add = ['отношения с друзьями и близкими.', 'работу и деловые вопросы, которые могут так некстати помешать планам.', 'себя и своё здоровье, иначе к вечеру возможен полный раздрай.', 'бытовые вопросы: уборка, ремонт, полить цветы или приготовить вкусный обед. Этот день лучше посвятить дому.', 'отдых, чтобы не умереть от усталости, лучше посветить этот день самому себе.', 'родителей, может лучше сегодняшний день побыть с ними.', 'родствеников, некоторые из них давно вас не видели. Было бы не плохоБ если бы вы созвонились.']

third = ['Готовьтесь! Сегодня могут произойти неприятные веши. Но они вас не потревожать, если вы будете к ним готовы.', 'Сегодня удача предала вас. Расчитывайте только на себя и приходите на встречи заранее.', 'Даже если влияние ретроградного Меркурия портит вам настроение и ваши дела на сегодня, то постарайтесь не унывать и доделать всё до конца.', 'Не нужно бояться сесегодня ничего. Удача до вечера на вашей стороне.', 'Если сегодня вы с кем то познакомитесь, то проявите участие в новом общении, и тогда эта встреча предвещает вам приятные хлопоты.', 'Главное верьте в себя и не унывайте, а не надейтесь на сверхъестественные силы.', 'Ваш день в первую очередь зависит только от вас, поэтому не дайте его испортить его другим. ']

print('Партия +миска рис и кошкажена')
telegram_bot('6370382072:AAHXCZQHT25fQbfoX4EbHnchoBzbk7UAVc8')
