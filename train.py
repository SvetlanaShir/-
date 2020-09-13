import pickle
import os
import argparse

parser = argparse.ArgumentParser()

parser.add_argument('--input-dir', action='store', dest='dir_name')
parser.add_argument('--model', action='store', dest='model')

args = parser.parse_args()

#print(args.dir_name)
#print(args.model)

#exit(0)

dir_name = args.dir_name
model = args.model
#print (model)
#dir_name = sys.argv[1]
#dir_name = "C:/Users/lenas/Desktop/input"   
#dir_name = "C:/Users/lenas/Desktop/output"   
# --input-dir C:/Users/lenas/Desktop/input --model C:/Users/lenas/Desktop/output
class Code:
    ABC = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
    punctuation = ',.!?: '
    my_dict = {}
    my_dict['конец предложения'] = []
    my_dict['начало предложения'] = []
    
    def fit(dir_name, model):
        folder = os.listdir(dir_name)
        for file in folder:
            path = dir_name + '/' + file
            with open(path, "r", encoding='utf-8') as inf:
                for line in inf:
                    line = line.strip()
                    line = line.lower()
                    line +=' '
                    word = ''
                    begin = 1
                    previous_word = ''
                    for symbol in line:
                        if symbol in Code.ABC:
                            word+=symbol
                            #print(symbol, end='')
                        elif symbol in Code.punctuation and not word == '':
                            #print(word)
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
                            if symbol == '.' and len(previous_word)>3:
                                Code.my_dict['конец предложения'].append(previous_word)
                                begin=1
                            if not symbol == ' ':
                                previous_word = '' 
                        else:
                            word = ''
                            previous_word = ''
                            begin = 0                            
        with open(model, 'wb') as f:
            pickle.dump(Code.my_dict, f)

    def print():
        print(Code.my_dict)

Code.fit(dir_name, model)
       
        
        
    