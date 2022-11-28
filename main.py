
##INFORMATION##
# -- The Users need player based data.
# -- The User with highest number wins.
# -- The User and Score must save in external file.
# -- The users can not draw.
# -- Neither user can have a negative number.
# -- Game must end after 5 rounds per user.
# -- The game must print the top 10 scores from the database.

"Import Statements"

import os.path
import sqlite3
import random
import sys
import random
from time import sleep
from pathlib import Path
global userOneName
global userTwoName
global score1
global score2

"Database Set Up"
sleep(0.5)
path_to_file = 'Database.db'
path = Path(path_to_file)

if path.is_file():
    print(f'Successfully located your  {path_to_file} file')
else:
    print(f'Could not locate your {path_to_file} file... Making a new one.')

conn = sqlite3.connect('Database.db')
c = conn.cursor()

def create_table(c):

    c.execute("CREATE TABLE IF NOT EXISTS scores(Name TEXT, Score INTEGER, Name2 TEXT, Score2 INTEGER)")
    c.execute("CREATE TABLE IF NOT EXISTS players(Name TEXT, Password TEXT, ID TEXT)")

create_table(c)
"Text Elements"

a = "Welcome to Keira’s interpretation of the 2 User Dice Game.\n\n"
b = "There are very simple instructions:\n"
c = "1. An AI will 2 Die 5 times for a match of 5 rounds\n"
d = "2. You are going to go against another player, you must get the highest score to win\n"
e = "3. If you match scores, you will go to a tiebreaker round\n"
f = "4. If you get an even scored roll, you will get 10 added to your score\n"
g = "5. If you get an odd scored roll, you will get 5 taken from your score\n"


"Number Elements"

even = [2, 4, 6, 8, 10, 12]

yes = ["y","Y","Yes","yes"]
"Intro Elements"

print(a, b, c, d, e, f, g)
for i in range(3):
    sys.stdout.write("Ready? ") # -- This line simply just just writes to the console “Ready? “ 5 times following the rest of the next code
    sys.stdout.write("[{0}]   \r".format('#' * (i+1) + ' ' * (3 - i))) # -- This entire line formats into [#####] (obviously adding 1 # every second until it reaches 5)
    sys.stdout.flush()
    sleep(1)
sys.stdout.write("Let's start the game. ")
start = input("Are you ready to start?")
if start not in yes:
    print("Invalid Answer. Self destructing in")
    sys.stdout.write("3...")
    sys.stdout.flush()
    sleep(1)
    sys.stdout.write("2...")
    sys.stdout.flush()
    sleep(1)
    sys.stdout.write("1...")
    sys.stdout.flush()
    sleep(1)
    os.abort()
"User One Elements"

userOneName = input("What is your username?")
userOnePassword = input("What is your password?")
user11 = input("Repeat your username ")
password11 = input("Repeat your password ")
if password11 != userOnePassword:
    print("Repeat your password Attempt 2.")
    password111 = input(
        "Repeat your password Attempt 3.")
if user11 != userOneName:
    print("Repeat your username Attempt 2.")
    user111 = input(
        "Repeat your username Attempt 3.")

if password11 or password111 == userOnePassword and user11 or user111 == userOneName:
    ranger = range(0, 999999)
    user1ID = random.sample(ranger, 1)
    data = "\n\nPlayer Data: \n{0}\n{1}\n{2}"
    print(data.format(userOneName, userOnePassword, user1ID))
    print(
        "\n",
        "<User One>",
        "\n",
        "Your Username is",
        userOneName,
        "\n",
        "Your chosen password is",
        userOnePassword,
        "\n",
        "Your ID is",
        user1ID,
        "\n",
        "<User One>",
        "\n\n",
    )

"User Two Elements"

userTwoName = input("What is your username? ")
userTwoPassword = input("What is your password? ")
user22 = input("Repeat your username ")
password22 = input("Repeat your password ")
if password22 != userTwoPassword:
    print("Repeat your password Attempt 2.")
    password222 = input(
        "Repeat your password Attempt 3.")
if user22 != userTwoName:
    print("Repeat your username Attempt 2.")
    user222 = input(
        "Repeat your username Attempt 3.")


if password22 or password222 == userTwoPassword and user22 or user222 == userTwoName:
    ranger = range(0, 999999)
    user2ID = random.sample(ranger, 1)
    print(
        "\n",
        "<User Two>",
        "\n",
        "Your Username is",
        userTwoName,
        "\n",
        "Your chosen password is",
        userTwoPassword,
        "\n",
        "Your ID is",
        user2ID,
        "\n",
        "<User Two>",
        "\n\n",
    )

    "Rolling Elements"

    dice1 = int(0)
    dice2 = int(0)
    num = 0
    player = 1
    while player == 1:
        score1 = 0
        for i in range(5):
            f = input("Press Enter to Roll the Dice ")
            num = num+1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1+dice2 in even:
                score1 = score1+10
            else:
                score1 = score1-5
            if score1 < 0:
               score1 = 0

            score1 = score1+dice1+dice2
            roundText1 = "\nUser 1 Scores {1} and {2} on Round {0}. Total score of {3}!\n"
            text = roundText1.format(num, dice1, dice2, score1)
            print(text)

        player = 2
        if num >= 6:
            print("it f*cked up")
            pass
    num = 0
    while player == 2:
        score2 = 0
        for i in range(5):
            f = input("Press Enter to Roll the Dice ")
            num = num+1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == dice2:
                dice3 = random.randint(1, 6)
                score2 = score2+dice1+dice2
            if dice1+dice2 in even:
                score2 = score2+10
            else:
                score2 = score2-5
            if score2 < 0:
               score2 = 0

            score2 = score2+dice1+dice2
            roundText2 = "\nUser 2 Scores {1} and {2} on Round {0}. Total score of {3}!\n"
            text = roundText2.format(num, dice1, dice2, score2)
            print(text)

        player = 0
        if num >= 6:
            print("The code has broken at line 177. Please check.")
            pass

"Sudden Death/Tie Breaker Elements"

if score1 == score2:
    num = num+1
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    dice4 = random.randint(1, 6)
    if dice1 == dice2:
        dice3 = random.randint(1, 6)
        score2 = score2+dice1+dice2
    if dice1+dice2 in even:
        score1 = score1+10
    else:
        score1 = score1-5
    if dice2+dice3 in even:
        score2 = score2+10
    else:
        score2 = score2-5

    roundText2 = "\n TIE BREAKER ROUND SCORES...\n Scores\n{0} {1} AND {2} {3}\n"
    text = roundText2.format(dice1, dice2, dice3, dice4)
    print(text)
    score1 = score1+dice1+dice2
    score2 = score2+dice3+dice4

"SQL Database Elements"
conn = sqlite3.connect('Database.db')
c = conn.cursor()

def add_names(c, conn, userOneName, score1, userTwoName, score2, userOnePassword, user1ID, userTwoPassword,user2ID):

    c.execute('''INSERT INTO scores(name, score, name2, score2)VALUES(?,?,?,?)''',
              (userOneName, score1, userTwoName, score2))
    c.execute('''INSERT INTO players(name, password, id)VALUES(?,?,?)''', userOneName, userOnePassword, user1ID)
    c.execute('''INSERT INTO players(name, password, id)VALUES(?,?,?)''', userTwoName, userTwoPassword, user2ID)
    conn.commit()
    conn.close()

add_names(c, conn, userOneName, score1, userTwoName, score2, userOnePassword, user1ID, userTwoPassword,user2ID)

print("Database table and data entry has been successful!")

conn = sqlite3.connect('Database.db')
c = conn.cursor()
c.execute("""SELECT * FROM scores ORDER BY score DESC""")
rows = c.fetchall()[:10]
conn.close()
print("The top 5 scores are:", rows)

print("The game will close 25 seconds after this message.")
sleep(25)
