import csv

with open('ppp.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

names = []

print()
print()

for person in data:
    s = person[1]
    if(s == "Team Name"):
        continue
    if(len(s)>0):
        ss = s.strip()
        names.append(ss)

print(names)
print(len(names))
