import re

subj = {}

with open('dict_file.txt', 'r') as file:
    for line in file:
        subject, lecture, practice, lab = line.split()
        subj[subject] = re.findall(r'[0-9]+', lecture) + re.findall(r'[0-9]+', practice) + re.findall(r'[0-9]+', lab)
for key, value in subj.items():
    for id, item in enumerate(value):
        value[id] = int(item)
    subj[key] = sum(value)
print(subj)
