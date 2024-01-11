import csv

with open('participants.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

handles = []

print()
print()

for person in data:
    s = person[0]
    if(s == "LIGHTOJ HANDLE"):
        continue
    if(len(s)>0):
        ss = s.strip()
        handles.append(ss)

print(handles)
print(len(handles))

lis = ""
n = len(handles)
for i in range(n-1):
    lis += handles[i]
    lis += '\n'
lis += handles[n-1]
print(lis)

with open('hh.txt', 'w') as f:
    f.write(lis)

    