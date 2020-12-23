import re
import json

subj = {}
arr = []
firms_in_plus = 0

with open('firm.txt', 'r') as file:
    for line in file:
        firm, ownership, income, costs = line.split()
        subj[firm] = re.findall(r'[0-9]+', ownership) + re.findall(r'[0-9]+', income) + re.findall(r'[0-9]+', costs)
for key, value in subj.items():
    for id, item in enumerate(value):
        value[id] = int(item)
    subj[key] = value[0] - value[1]
    if subj[key] > 0:
        arr.append(subj[key])
        firms_in_plus += 1
aver_profit = (sum(arr) // firms_in_plus)

av_prof_dict = dict(average_profit=int(aver_profit))
arr_final = [subj, av_prof_dict]

with open('arr_final.json', 'w', encoding='UTF-8') as f:
    content = json.dumps(arr_final, ensure_ascii=False)
    f.write(content)
