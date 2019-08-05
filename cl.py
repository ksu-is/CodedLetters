import pickle
import vectorize
import os

os.system('cls' if os.name == 'nt' else 'clear')
f = open('./vectors.pkl', 'rb')
dict = pickle.load(f)
f.close()

print('Word Unscrambler')

def coded_letters():
    word=''
    while word.lower().startswith('q')!=True:
        word=input('Enter a scrambled word or \"\'q\'uit\": ')
        key=vectorize.get_key(word)
        if word.lower().startswith('q')==True:
            break
        elif key in dict.keys():
            print(''.join(dict[key])[:-1])
        else:
            print('Not found')

coded_letters()
