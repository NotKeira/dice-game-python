##INFORMATION##
# -- Permission Locked Data.
# -- User with highest number wins
# -- User must save in a file externally
# -- There can not be a draw
# -- User cannot go NEGATIVE
# -- Ends in 5 rounds
# -- Display top 5 results from external

"Import Statements"
import sqlite3
import random
import sys
import random
from time import sleep
global userOneName
global userTwoName
global score1
global score2

"Text Elements"
a = "Welcome to Keira’s interpretation of the 2 User Dice Game.\n\n"
b = "There are very simple instructions:\n"
c = "1. An AI will 2 Die 5 times for a match of 5 rounds\n"
d = "2. You are going to go against another player, you must get the highest score to win\n"
e = "3. If you match scores, you will go to a tiebreaker round\n"
f = "4. If you get an even scored roll, you will get 10 added to your score\n"
g = "5. If you get an odd scored roll, you will get 5 taken from your score\n"
h = "6. Do not steal my code or I will hunt you down and murder you and your family.\n"

even = [2, 4, 6, 8, 10, 12]
storageCreate = open("PlayerData.txt", "x")
scoreCreate = open("score.txt", "x")
storage = open("PlayerData.txt", "a")


print(a, b, c, d, e, f, g, h)

for i in range(5):
    sys.stdout.write("Ready? ")
    sys.stdout.write("[{0}]   \r".format('#' * (i+1) + ' ' * (4 - i)))
    sys.stdout.flush()
    sleep(random.random())

start = input("Are you ready to start?")

userOneName = input("What is your username?")
userOnePassword = input("What is your password?")
user11 = input("Please repeat your username for confirmation. ")
password11 = input("Please repeat your password for confirmation. ")
if password11 != userOnePassword:
    print("That is not the same password, please try again.")
    password111 = input(
        "Please repeat your password correctly for confirmation."
    )
if user11 != userOneName:
    print("That is not the same username, please try again.")
    user111 = input(
        "Please repeat your username correctly for confirmation.")

if password11 or password111 == userOnePassword and user11 or user111 == userOneName:
    ranger = range(0, 999999)
    user1ID = random.sample(ranger, 1)
    data = "\n\nPlayer Data: \n{0}\n{1}\n{2}"
    print(data.format(userOneName, userOnePassword, user1ID))
    # storage.write(data.format(userOneName, userOnePassword, user1ID))
    # storage.close()
    # reader = open("PlayerData.txt", "r")
    # print(reader.read())
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

userTwoName = input("What is your username?")
userTwoPassword = input("What is your password?")
user22 = input("Please repeat your username for confirmation. ")
password22 = input("Please repeat your password for confirmation. ")
if password22 != userTwoPassword:
    print("That is not the same password, please try again.")
    password222 = input(
        "Please repeat your password correctly for confirmation.")
if user22 != userTwoName:
    print("That is not the same username, please try again.")
    user222 = input(
        "Please repeat your username correctly for confirmation.")


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

    dice1 = int(0)
    dice2 = int(0)
    print(dice1, dice2)
    num = 0
    player = 1
    while player == 1:
        score = open("score.txt", "a")
        score.write("Player 1\n")
        score1 = 0
        for i in range(5):
            num = num+1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1+dice2 in even:
                score1 = score1+10
            else:
                score1 = score1-5
            entry = "Roll {0} = {1} and {2}\n"
            score.write(entry.format(num, dice1, dice2))
            print(dice1, dice2)
            roundText1 = "\nUser 1's Round {0} Scores\n{1} {2}\n"
            text = roundText1.format(num, dice1, dice2)
            print(text)
            score1 = score1+dice1+dice2
        player = 2
        if num >= 6:
            print("it f*cked up")
            pass
    num = 0
    while player == 2:
        score = open("score.txt", "a")
        score.write("\nPlayer 2\n")
        score2 = 0
        for i in range(5):
            num = num+1
            score = open("score.txt", "a")
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            if dice1 == dice2:
                dice3 = random.randint(1, 6)
                score2 = score2+dice1+dice2
            if dice1+dice2 in even:
                score2 = score2+10
            else:
                score2 = score2-5
            entry = "Roll {0} = {1} and {2}\n"
            score.write(entry.format(num, dice1, dice2))
            print(dice1, dice2)
            roundText2 = "\nUser 2's Round {0} Scores\n{1} {2}\n"
            text = roundText2.format(num, dice1, dice2)
            print(text)
            score2 = score2+dice1+dice2
        player = 0
        if num >= 6:
            print("it f*cked up")
            pass

if score1 == score2:
    num = num+1
    score = open("score.txt", "a")
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

# sql database
conn = sqlite3.connect('scores.db')
c = conn.cursor()


def create_table(c):
    c.execute("CREATE TABLE IF NOT EXISTS scores(Name TEXT, Score INTEGER)")


def add_names(c, conn):
    c.execute('''INSERT INTO scores (name, score, name, score2)VALUES(?,?,?,?)''',
              (userOneName, score1, userTwoName, score2))

    conn.commit()
    conn.close()


create_table(c)
add_names(c, conn)

print("Database table and data entry has been successful!")

conn = sqlite3.connect("scores.db")
c = conn.cursor()
c.execute("""SELECT * FROM scores ORDER BY score DESC""")
rows = c.fetchall()[:10]

print("The top 5 scores are:", rows)
