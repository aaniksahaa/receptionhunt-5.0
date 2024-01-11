import numpy as np
import random
import string
import csv


def getQuery(name,pwd,token):
    s = "INSERT INTO \"user\" (name, pwd, token, level_completed, last_time, role) VALUES ('{}', '{}', '{}', 0, '2022-12-13T12:52:38.220219'::timestamp, 'TEAM') RETURNING \"user\".id;".format(name,pwd,token)
    return s


def getRandomPassword(len):
    # get random password pf length 8 with letters, digits, and symbols
    characters = "ABCDEFGHJKLMNPQRSTUVWXYZ" + "23457"
    password = ''.join(random.choice(characters) for i in range(len))
    return password


names = ['LaAu', 'Unga Bunga', 'Downvote', 'Team Dominix', 'Enigma', 'ZERO', 'Patagobi', 'upvote', 'Team_Serpentix101', 'Interlude', 'Team-OO7', 'Black Pearl', 'RepliCunts', 'Survey Corps', 'Tan_9ty', 'Pointers', 'Blitz Hunters', 'LuTHA']


easy = 5
hard = 5
physical = 2
N = 18
passlen = 6

queries = ""
lines = []
header1 = ['Team Name','Password']
header2 = ['Team Name','Password','Puzzle Order']
rows = []
allrows = []

print()
print()
print()

for i in range(N):
    e = np.random.permutation(easy)
    h = np.random.permutation(hard)
    p = np.random.permutation(physical)
    s = ""
    ee = 0
    hh = 0
    for j in range(1):
        s = s + chr(ord('A')+e[ee])
        s = s + chr(ord('F')+h[hh])
        ee += 1
        hh += 1

    if(i%2 == 0):
        s = s + chr(ord('P')+p[0])
        s = s + chr(ord('A')+e[ee])
        ee += 1
    else:
        s = s + chr(ord('A')+e[ee])
        ee += 1
        s = s + chr(ord('P')+p[0])

    s = s + chr(ord('F')+h[hh])
    hh += 1
    for j in range(1):
        s = s + chr(ord('A')+e[ee])
        s = s + chr(ord('F')+h[hh])
        ee += 1
        hh += 1

    if(i%2 == 0):
        s = s + chr(ord('P')+p[1])
        s = s + chr(ord('A')+e[ee])
        ee += 1
    else:
        s = s + chr(ord('A')+e[ee])
        ee += 1
        s = s + chr(ord('P')+p[1])

    s = s + chr(ord('F')+h[hh])
    hh += 1

    for j in range(1):
        s = s + chr(ord('A')+e[ee])
        s = s + chr(ord('F')+h[hh])
        ee += 1
        hh += 1

    puzzles = s
    teamname = names[i]
    password = getRandomPassword(6)
    namepass = "Team: " + teamname + " Password: " + password
    details = "Team: " + teamname + " Password: " + password + " Puzzle Order: " + puzzles
    query = getQuery(teamname,password,puzzles)
    print(details)
    queries += query
    lines.append(details)
    rows.append([teamname,password])
    allrows.append([teamname,password,puzzles])

print()
print()
print()
print(queries)

with open('teamlist.txt', 'w') as f:
    for line in lines:
        f.write(line)
        f.write('\n')

with open('teamlist-query.txt', 'w') as f:
    f.write(queries)

with open('credentials.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header1)
    for row in rows:
        writer.writerow(row)

with open('team-details.csv', 'w', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(header2)
    for row in allrows:
        writer.writerow(row)

print()
print()
print()

    
