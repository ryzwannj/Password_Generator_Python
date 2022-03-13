import random
import string
import uuid
from time import time, ctime
import sqlite3

con = sqlite3.connect('users.db')
cur = con.cursor()

cur.execute('''CREATE TABLE  IF NOT EXISTS Users
                (id integer primary key, Name text, Firstname char, Email char, Password char, Username text, Created text)''')

def random_name():
    lines = open('names.txt').read().splitlines()
    myline = (random.choice(lines))
    return myline


def create_user():
    random_uuid = uuid.uuid4()

    name = str(random_name().lower())
    firstname = str(random_name()).lower()
    password = str(random_uuid)[:10]
    username = str((name+name[3:5].upper()+(str(random.randint(0, 99))+'.'+(str(random.randint(0, 9))))))
    email = str(username+'@yahoo.com')
    date = str(ctime())

    cur.execute('''INSERT INTO Users (Name,Firstname,Email,Password,Username,Created)
    VALUES (?,?,?,?,?,?)''',(name,firstname,email,password,username,date))
    con.commit()

    print('\n'
        + 'name: '+ name +'\n'
        + 'firstname: '+ firstname + '\n'
        + 'email: '+ email + '\n'
        + 'password: '+ password +'\n')

create_user()