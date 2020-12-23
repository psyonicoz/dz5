lines = 0
with open('file.txt', 'r', encoding='utf-8') as file:
    for line in file:
        words = 0
        for word in line.split():
            words += 1
        print(f'В {lines+1} строке {words} слов')
        lines += 1
