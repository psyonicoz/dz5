with open('numbers_list.txt', 'r', encoding='utf-8') as file:
    for i in file:
        with open('one_two111.txt', 'a', encoding='utf-8') as file_rus:
            if '1' in i:
                x = i.replace('One', 'Один')
            elif '2' in i:
                x = i.replace('Two', 'Два')
            elif '3' in i:
                x = i.replace('Three', 'Три')
            elif '4' in i:
                x = i.replace('Four', 'Четыре')
            elif '5' in i:
                x = i.replace('Five', 'Пять')
            file_rus.write(x)
