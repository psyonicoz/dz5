with open('file.txt', 'a', encoding='utf-8') as file:
    while True:
        insert = input('Введите построчно данные через Enter, для окончания ввода оставьте и нажмите Enter ')
        file.write(f'{insert}\n')
        if insert == '':
            break
