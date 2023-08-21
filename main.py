from hagman_list import hagman   # подключаем данные с картинками
import random  # подключаем библиотеку для работы со случйным данными

words = ['python', 'cat', 'program'] # Создаем список слов из которых будет загадано слово

abc=' '.join([chr(el) for el in range(ord('a'), ord('z')+1)]) #создаем алфавит для игрока

word = random.choice(words) #выбираем слово из списка слов
letter_base = '*' * len(word) # создаем строку символов по количеству букв в слове
letter_used = [] # в переменной будем хранить использованные буквы
count_wrong = 0 # ведем количество ошибок
count_max_wrong = len(hagman) - 1 # максимальное количество ошибок которое может сделать игрок

while count_wrong < count_max_wrong and letter_base != word:
    ''' игровой цикл'''
    print(hagman[count_wrong])
    print('Использованные буквы:', ' '.join(letter_used))
    print('Алфавит:', abc)
    print('Загаданное слово:', letter_base)

    letter_user = input('Введите букву:')

    while letter_user in letter_used: # проверка ввода буквы игроком
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
    print('Вы проиграли!!','Слово было:', word)
else:
    print('Вы победили!!!')
