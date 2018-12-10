
from time import gmtime, strftime, localtime

answers = {'Как дела?': 'Хорошо!', 'Что делаешь?': 'Программирую', 'И зачем тебе это?': 'Не знаю'}

def ask_user():
	while True:
		user_say = input('Спроси меня о чём-то?:  ')
		if user_say == 'Как дела?':	
			print('Хорошо!')
		elif user_say == 'Сколько времени?':
			print(strftime('%H:%M:%S', localtime()))
		elif user_say in answers:
			print('{}'.format(answers[user_say]))
		    
		else:
			print('Не знаю ответ на это: {}'.format(user_say))

ask_user()



