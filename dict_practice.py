print()
print('- Привет, рад Вас видеть!')
print()
name = str(input('- Как Вас зовут? \n- Введите свое имя: '))
print()
<<<<<<< HEAD
print('- Очень приятно ' + name.title() + '.' + ' А я - калькулятор процента Python.')
=======
print('- Очень приятно ', name.title(), '.' + ' А я - калькулятор процента Python.')
>>>>>>> 54935e54f4d35c7b856ef3e4c22abb50342b2a7a
print("- Помогу посчитать сумму вот этих банков: \n  ТКБ - 5.6%, СКБ - 5.9%, ВТБ - 4.28% и СБЕР - 4.0%")
print()
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('- Введите сумму которую хотите положить: '))
<<<<<<< HEAD
tkb = per_cent['ТКБ'] * money / 100
skb = per_cent['СКБ'] * money / 100
vtb = per_cent['ВТБ'] * money / 100
sber = per_cent['СБЕР'] * money / 100
=======
tkb: float = per_cent['ТКБ'] * money / 100
skb: float = per_cent['СКБ'] * money / 100
vtb: float = per_cent['ВТБ'] * money / 100
sber: float = per_cent['СБЕР'] * money / 100
>>>>>>> 54935e54f4d35c7b856ef3e4c22abb50342b2a7a
print('- Итак:', 'ТКБ:', tkb, 'CКБ:', skb, 'ВТБ:', vtb, 'CБЕР:', sber)
print()
deposit = max(tkb,skb,vtb,sber)
print('- Максимальная сумма, которую вы можете заработать -',deposit)
print('- И это неплохая сумма, желаю удачи!')



