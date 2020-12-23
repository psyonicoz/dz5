with open('employees.txt', 'r', encoding='utf-8') as file:
    workers = {}
    for line in file:
        key, value = line.split()
        workers[key] = int(value)
        if int(value) < 20000:
            print(f'{key}')
aver_salary = (sum(workers.values()) / len(workers))
print(f'Средняя зарплата: {aver_salary}')
