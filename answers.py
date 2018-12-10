answers = {
	'привет': 'Привет!',
	'как дела?': 'Отлично!',
	'пока': 'Увидимся!'
}

def get_answer(question, answers):
    return answers.get(question)

def ask_user(answers):
    try:
        while True:
            user_input = input('Скажи что-нибудь: ')
            answer = get_answer(user_input, answers)
            print(answer)

            if user_input == 'пока':
                break
    except KeyboardInterrupt:
        print('Возвращайтесь ещё!')


ask_user(answers)