print()
print('- Привет, рад Вас видеть!')
print()
name = str(input('- Как Вас зовут? \n- Введите свое имя: '))
print()
print('- Очень приятно ' + name.title() + '.' + ' А я - калькулятор процента Python.')
print("- Помогу посчитать сумму вот этих банков: \n  ТКБ - 5.6%, СКБ - 5.9%, ВТБ - 4.28% и СБЕР - 4.0%")
print()
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('- Введите сумму которую хотите положить: '))
tkb = per_cent['ТКБ'] * money / 100
skb = per_cent['СКБ'] * money / 100
vtb = per_cent['ВТБ'] * money / 100
sber = per_cent['СБЕР'] * money / 100
print('- Итак:', 'ТКБ:', round(tkb,2), 'CКБ:', round(skb,2), 'ВТБ:', round(vtb,2), 'CБЕР:', round(sber,2))
print()
deposit = max(tkb,skb,vtb,sber)
print('- Максимальная сумма, которую вы можете заработать -',round(deposit,2))
print('- И это неплохая сумма, желаю удачи!')



