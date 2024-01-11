import csv

def getPuzzleQuery(id,link,answer):
    s = "INSERT INTO quiz (id, link, answer) VALUES ('{}', '{}', '{}');".format(id,link,answer)
    return s

with open('puzzles.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

puzzles = []

print()
print()

queries = ""

for puzzle in data:
    id = puzzle[0]
    link = puzzle[1]
    answer = puzzle[2]
    if(id == "Puzzle-ID"):
        continue
    else:
        puzzles.append([id,link,answer])
        queries = queries + getPuzzleQuery(id,link,answer)

print(puzzles)
print()
print()
print(queries)
print()
print()