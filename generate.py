import pickle
import random
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--model', action='store', dest='model')
parser.add_argument('--length', action='store', dest='length')
parser.add_argument('--seed', action='store', dest='seed')
args = parser.parse_args()
model = args.model
length = int(args.length)
seed = args.seed
if seed == None:
    seed = 'случайное слово'



class Code:
    def generate(model, length, seed):
        with open(model, 'rb') as f:
            dict_new = pickle.load(f) 
        for j in range(length):
            if seed == 'случайное слово':
                word = random.choice(dict_new['начало предложения'])
            else:
                word = seed.lower()
            print(word[0].upper() + word[1:], end='')
                
            sentence_length = random.randint(3, 10)
            for i in range(20):
                if word in dict_new:
                    word = random.choice(dict_new[word])
                    if i > sentence_length and word in dict_new['конец предложения']:
                        if word in dict_new['слова с большой буквы']:
                            print('', word[0].upper() + word[1:], end='. ')
                        else:
                            print('', word, end='. ')
                        seed = 'случайное слово'
                        break
                    else:
                        if word in dict_new['слова с большой буквы']:
                            word = word[0] + word[1:]
                            print('', word[0].upper() + word[1:], end='')
                        else:
                            print('', word, end='')
                else: 
                    print('. ', end='')
                    seed = 'случайное слово'
                    break
                if i == 19:
                    print('. ', end='')
                    seed = 'случайное слово'
                    break


Code.generate(model, length, seed)