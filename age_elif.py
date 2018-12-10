user_age = int(input('Сколько вам лет?'))

def user_def(age):
    if age < 7:
        answer = "детский сад"
    elif age >= 7:
        answer = "школа"
    elif age >= 18:
        answer = "университет"
    elif age > 23:
        answer = "работать уже пора, детка"
    return(answer)

hey_hey = user_def(user_age)
print(hey_hey)