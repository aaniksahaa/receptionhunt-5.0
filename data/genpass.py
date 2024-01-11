import random
import string

def getRandomPassword(len):
    # get random password pf length 8 with letters, digits, and symbols
    characters = string.ascii_lowercase + string.digits
    password = ''.join(random.choice(characters) for i in range(len))
    return password

for i in range(10):
    print(getRandomPassword(10))