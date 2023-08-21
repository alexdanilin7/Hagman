from hagman_list import hagman
import random

words = ['python', 'cat', 'program']

abc=' '.join([chr(el) for el in range(ord('a'), ord('z')+1)])

word = random.choice(words)
letter_base = '*' * len(word)
letter_used = []
count_wrong = 0
count_max_wrong = len(hagman) - 1

while count_wrong < count_max_wrong and letter_base != word:
    print(hagman[count_wrong])
    print('Использованные буквы:', ' '.join(letter_used))
    print('Алфавит:', abc)
    print('Загаданное слово:', letter_base)

    letter_user = input('Введите букву:')

    while letter_user in letter_used:
        print('Error in letter')
        letter_user = input('Введите букву:')
    letter_used.append(letter_user)
    if letter_user in word:
        temp = ""
        for i in range(len(word)):
            if letter_user == word[i]:
                temp+=letter_user
            else:
                temp+=letter_base[i]
        letter_base = temp
    else:
        print('Такой буквы нет в слове!!!')
        count_wrong += 1
if count_wrong == count_max_wrong:
    print(hagman[count_wrong])
    print('Вы проиграли!!')
else:
    print('Вы победили!!!')
