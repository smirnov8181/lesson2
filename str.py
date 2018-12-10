a = input('Первая строка: ')
b = input('Вторая строка: ')



def some_func(one, two):
	if not type(one) == str or type(two) == str:
		return 0
	elif one == two:
		return 1
	elif len(one) > len(two):
		return 2
	elif two == 'learn':
		return 3
	elif len(two) > len(one):
		return 4

hey_hey = some_func(a, b)
print(hey_hey)
