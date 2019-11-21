from telegram.ext import Updater, Filters, CommandHandler, MessageHandler

from config import TG_TOKEN, TG_API_URL

import re

def start(update, context):
	context.bot.send_message(
		chat_id = update.effective_chat.id,
		text = 'Привет! Я могу посчитать Ваш индекс массы тела. Введите, разделяя пробелом, свой вес в килограммах и рост в сантиметрах. Например: 107 170'
		)

def answer(update, context):
	t = 'Либо нормально вводите, либо я буду плакатц и резать вены на ногах.'
	msg = update.message.text
	if bool(re.match('[0-9]+ [0-9]+', msg)):
		mass, height = msg.split()
		mass = float(mass)
		height = float(height)
		ind = round(10000 * mass / height / height, 2)
		if ind <= 16:
			t = 'Ваш ИМТ:' + str(ind) + ' кг/м^2. Это считается выраженным дефицитом массы тела.'
		if ind > 16 and ind <= 18.5:
			t = 'Ваш ИМТ:' + str(ind) + ' кг/м^2. Это считается дефицитом массы тела.'
		if ind > 18.5 and ind < 25:
			t = 'Ваш ИМТ:'+ str(ind) + ' кг/м^2. Это считается нормой.'
		if ind >= 25 and ind <= 30:
			t = 'Ваш ИМТ:'+ str(ind) + ' кг/м^2. Это считается предожирением.'
		if ind > 30 and ind <= 35:
			t = 'Ваш ИМТ:'+ str(ind) + ' кг/м^2. Это считается ожирением.'
		if ind > 35 and ind <= 40:
			t = 'Ваш ИМТ:'+ str(ind) + ' кг/м^2. Это считается резким ожирением.'
		if ind > 40:
			t = 'Ваш ИМТ:'+ str(ind) + ' кг/м^2. Это считается очень резким ожирением.'
	context.bot.send_message(
        chat_id = update.effective_chat.id,
        text = t
    )


def main():
    updater = Updater(
        token = TG_TOKEN, #telegram token
        base_url = TG_API_URL, #just a rkn blockade bypass link
        use_context = True
    )

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(Filters.text, answer)

    updater.dispatcher.add_handler(start_handler)
    updater.dispatcher.add_handler(message_handler)

    updater.start_polling()

if __name__ == '__main__':
    main()
