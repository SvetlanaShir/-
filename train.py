import pickle
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input-dir', action='store', dest='dir_name')
parser.add_argument('--model', action='store', dest='model')
args = parser.parse_args()
dir_name = args.dir_name
model = args.model


class Code:
    ABC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя-'
    CAPS_ABC= 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
    punctuation = ',.!?: '
    my_dict = dict()
    my_dict['конец предложения'] = []
    my_dict['начало предложения'] = []
    my_dict['слова с большой буквы'] = []
    small_words={'слово'}
    def fit(dir_name, model):
        folder = os.listdir(dir_name)
        for file in folder:
            path = dir_name + '/' + file
            with open(path, "r", encoding='utf-8') as inf:
                for line in inf:
                    line = line.strip()
                    line = line.lower()
                    line += ' '
                    word = ''
                    begin = 1
                    previous_word = ''
                    for symbol in line:
                        if symbol in Code.ABC:
                            word += symbol
                        elif symbol in Code.punctuation and not word == '':
                            if begin == 1:
                                Code.my_dict['начало предложения'].append(word)
                            begin = 0
                            if not previous_word == '':
                                if previous_word in Code.my_dict:
                                    Code.my_dict[previous_word].append(word)
                                else:
                                    Code.my_dict[previous_word] = [word]
                            previous_word = word
                            word = ''
                            if symbol == '.' and len(previous_word) > 3:
                                Code.my_dict['конец предложения'].append(previous_word)
                                begin = 1
                            if not symbol == ' ':
                                previous_word = '' 
                        else:
                            word = ''
                            previous_word = ''
                            if not symbol ==' ':
                                begin = 0
            #часть кода дальше нужна, чтобы слова с большой буквы (в основном имена) были написаны с большой буквы. Эта часть не подходит для стихов, например.
            with open(path, "r", encoding='utf-8') as inf:
                for line in inf:
                    line = line.strip()
                    line += ' '
                    word = ''
                    for symbol in line:
                        if symbol in Code.ABC or symbol in Code.CAPS_ABC:
                            word += symbol
                        elif symbol in Code.punctuation:
                            if word == word.lower():
                                Code.small_words.add(word)                           
                            word = ''
                        else: word = ''
        for file in folder:
            path = dir_name + '/' + file
            with open(path, "r", encoding='utf-8') as inf:
                for line in inf:
                    line = line.strip()
                    line += ' '
                    word = ''
                    for symbol in line:
                        if symbol in Code.ABC or symbol in Code.CAPS_ABC:
                            word += symbol
                        elif symbol in Code.punctuation and not word == '':
                            if word[0] in Code.CAPS_ABC and not word.lower() in Code.small_words:
                                Code.my_dict['слова с большой буквы'].append(word.lower()) 
                            word = ''
                        else: word = '' 
        
        with open(model, 'wb') as f:
            pickle.dump(Code.my_dict, f)
        
    def print():
        print(Code.my_dict)

Code.fit(dir_name, model)
