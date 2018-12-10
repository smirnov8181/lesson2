def get_summ():
	try:
		num_one = int(input('Первое число: '))
		num_two = int(input('Второе число: '))
		result = num_one + num_two
		print(result)

	except ValueError:
		print('Давайте только целые числа будем вводить')


get_summ()
