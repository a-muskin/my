tickets = int(input('Привет, сколько Вам билетов? \n'))
for i in range(tickets):
    age = int(input('Введите возраст гостя: \n'))
    if age < 18:
        print('В возрасте', age, 'вход бесплатный')
        print('---')
    elif 18 <= age <= 25:
        print('В возрасте', age, 'вход 990 руб.')
        print('---')
    else:
        print('В возрасте', age, 'вход 1390 руб.')
        print('---')
