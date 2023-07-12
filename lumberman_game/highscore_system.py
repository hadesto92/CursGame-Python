import os
import random
import sys

from unidecode import unidecode
from static import sounds

temp_score = 0

dictionary = ['1','2','3','4','5','6','7','8','9','0','.','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','R','S','T','Q','U','W','V','X','Y','Z']

def score_system(score, time_left, max_time, stop_music):
    global temp_score

    score += 1
    temp_score = score
    if time_left < max_time:
        if score < 1000:
            time_left += 2 / score + 0.3
        elif 1000 <= score < 2000:
            time_left += 2 / score + 0.25
        elif 2000 <= score < 4000:
            time_left += 2 / score + 0.2
        elif 4000 <= score < 8000:
            time_left += 2 / score + 0.15
        else:
            time_left += 2 / score + 0.11

        if score % 1000 == 0:
            if not stop_music:
                sounds.powerup.set_volume(0.3)
                sounds.powerup.play()
            if time_left + 5 <= max_time:
                time_left += 5
            else:
                time_left = max_time

    return score, time_left

#Wypisanie nazwy gracza bez znaków polskich i wielkimi literami
def visable_name(player_name):
    return unidecode(player_name.upper())

#Szyfrator
def encryption_cesar(score, name, key):
    #print('encryption')
    global dictionary

    temp_word = str(score)+'.'+str(name)
    encryption_word = ''

    for i, sign in enumerate(temp_word):
        for j, dic_sign in enumerate(dictionary):
            if sign==dic_sign:
                if int(j)+int(key) >= len(dictionary):
                    encryption_word += dictionary[(int(j)+int(key))-len(dictionary)]
                else:
                    encryption_word+=dictionary[int(j)+int(key)]

    encryption_word+='.'+str(key)

    return encryption_word

#Deszyfrator
def decryption_cesar(word):
    #print('descryption')
    flage = 0
    temp_key = ''

    for line in word:
        for index in range(len(line)-1, 0, -1):
            if line[index] == '.':
                flage += 1
            else:
                if flage == 0:
                    temp_key = line[index]+temp_key

    key = int(temp_key)
    score = ''
    name = ''

    decryption_word = ''

    for line in word:
        for i, sign in enumerate(line):
            if i < len(line)-(len(temp_key)+1):
                for j, dic_sign in enumerate(dictionary):
                    if sign == dic_sign:
                        if int(j)-int(key) < 0:
                            decryption_word += dictionary[len(dictionary)+(int(j)-int(key))]
                        else:
                            decryption_word += dictionary[int(j)-int(key)]


    flage = 0

    for sign in decryption_word:
        if sign == '.':
            flage+=1
        else:
            if flage==0:
                score+=sign
            elif flage==1:
                name+=sign

    return score, str(name), key

#print(decryption_cesar(encryption_cesar(1902, 'HADESTO', 10)))

#Pobranie informacji z pliku i zwraca zawartośc w formie tablicy każda linika pliku to odzielna wartość tablicy
def file_open():
    #print('file open')
    #file = os.path.join(os.path.dirname(sys.executable), 'all_score')
    file_temp = open('all_score', "r")
    content = file_temp.read()
    content_temp = content.split("\n")

    data = []
    for line in content_temp:
        if line == '':
            break
        sign_temp = ''
        temp_data = []
        for sign in line:
            if(sign != ' '):
                sign_temp+=sign
            else:
                temp_data.append(sign_temp)
                sign_temp=''
        temp_data.append(sign_temp)
        data.append(temp_data)

    file_temp.close()

    return data

#Zapisanie informacji do pliku
def save_file(data):
    #print('file save')
    #file = os.path.join(os.path.dirname(sys.executable), 'all_score')
    file_temp = open('all_score', "a")
    file_temp.write(data)
    file_temp.close()

#Utworzenie listy uporządkowanej z wynikami
def get_all_score():
    #print('get all score')
    data_temp = file_open()
    data = []
    for line in data_temp:
        data.append(decryption_cesar(line))

    return data

#Zapisanie nowego wyniku do pliku
def save_new_score(score, name):
    #print('save to file')
    key = random.randint(1,15)
    save_file(encryption_cesar(score, name, key)+"\n")

#Sortowanie wyników
def sort_list(list):

    for i in range(len(list)):
        for j in range(0, len(list)-i-1):
            if int(list[j][0]) > int(list[j+1][0]):
                list[j], list[j+1] = list[j+1], list[j]

    return list[::-1]

#Wypisanie 10 najlepszych wyników
def get_highscore():
    #print('get highscore')
    data = []

    temp_data = get_all_score()
    temp_data = sort_list(temp_data)

    for i in range(0,len(temp_data)):
        if i < 10:
            data.append(temp_data[i])

    return data