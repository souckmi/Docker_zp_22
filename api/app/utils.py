import os
from random import randint
from flask import send_file
from os import path


def save_txt(filename,max):
    with open(os.path.dirname(__file__) +'/data/'+filename+'.txt', 'w+') as new_file:
        for i in range(max):
            new_file.write(str(randint(0,100))+'\n')
    return "Soubor vytvoren"

def get_data(filename):
    filepath=os.path.dirname(__file__) +'/data/'+filename+'.txt'
    if path.exists(filepath):
        return send_file(filepath,as_attachment=True)        
    else:
        return "Tento soubor neexistuje."