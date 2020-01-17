# Password List Maker 1.0
# By mrsploit
# t.me/zoneh
import os

data_list = []
word_list = []
characters = []

def add(word, met):
    if word == 's':
        pass
    elif word == 'S':
        pass
    else:
        if met == 'data':
            data_list.append(word)
        elif met == 'word':
            word_list.append(word)
        elif met == 'characters':
            characters.append(word)

def get_data():
    print ("\033[1;35m  For Skip Enter The s/S \033[1;m"+'\n')
    add(input("\033[1;32mName: "), 'data')
    add(input("Last Name: "), 'data')
    add(input("Age : "), 'data')
    job = input("Job : ")
    if len(job) == 6:
        add(job, 'word')
        add(job, 'data')
    elif len(job) > 6:
        add(job, 'word')
        add(job, 'data')
    else:
        add(job, 'data')
    birthday = input("Birthday (zzzz/yy/xx) : ")
    if birthday == 's':
        pass
    elif birthday == 'S':
        pass
    else:
        if '/' in birthday:
            birthday_s = birthday.split("/")
            if len(birthday_s) == 3:
                add(birthday_s[0]+birthday_s[0], 'word')
                add(birthday_s[2], 'data')
            else:
                pass
        else:
            pass
    while True:
        x = input("Phone Number (For Next Enter The n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input("Other Words (For Next Enter The n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            if len(x) == 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) > 6:
                add(x, 'word')
                add(x, 'data')
            elif len(x) < 6:
                add(x, 'data')
    while True:
        x = input("Characters For Join (For Next Enter The n/N): ")
        if x == 'n':
            break
        elif x == 'N':
            break
        else:
            add(x, 'characters')

banner = '''
\033[1;31m     Name
        Age
       Job          \033[1;m   \033[1;34m  (●)
      _______            | |
     (_______)  _________| |__
     \       /  |  Password  |
      \     /   |    List    |
       \   /____|  Generator |_______
       |__________________________   |
                                  |  |
                             _____||||______
                            |■■■■■■■■■■■■■■■|\033[1;m
\033[1;33m  × Password List Generator \033[1;m \033[1;32m^^^^^^^^^^^^^^^ \033[1;m
 \033[1;33m × Jailbreak & Root  \033[1;m     \033[1;31m   ____________
 \033[1;33m * t.me/jailbrrakandroot  \033[1;m  \033[1;31m | 123456   | \033[1;m
\033[1;33m  * https://jilrot.com   \033[1;m    \033[1;31m | p@ssword | \033[1;m
                           \033[1;31m   | abcd123  | \033[1;m
                         \033[1;31m     | •••••••  | \033[1;m
                          \033[1;31m    | •••••••  | \033[1;m
                          \033[1;31m    |__________| \033[1;m

'''

def generat_save():
    f = open('Password_List.lst', 'a')
    for wr in word_list:
        f.write(wr+'\n')
    for da1 in data_list:
        for da2 in data_list:
            for chra in characters:
                f.write(da1+da2+'\n')
                f.write(da1+chra+da2+'\n')
    f.close()
    print ("\033[1;35m  Password List Maked in 'Password_List.lst' \033[1;m"+'\n')

if __name__ == '__main__':
    os.system('clear')
    print (banner)
    get_data()
    generat_save()

