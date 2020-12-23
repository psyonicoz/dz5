with open('sum_file.txt', 'w', encoding='utf-8') as file:
    insert = input('Введите числа через пробел ')
    file.write(f'{insert}')
    summ = 0
    for i in insert.split(' '):
        summ += int(i)
    print(f'Сумма введенных чисел: {summ}')
