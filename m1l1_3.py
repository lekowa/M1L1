import time 
meme_dict = {
            "КРИНЖ": "Что-то очень странное или стыдное.",
            "ЛОЛ": "Что-то очень смешное.",
            "КАПЕЦ": "значающее конец чего-либо, часто именно неудачный конец, провал.",
            "СЛЕНГ": "набор слов или новых значений существующих слов, употребляемых в различных группах.",
            "ШАРИТЬ": "сленг понимать что-либо, разбираться в чём-либо.",
            }
print('Добро пожаловать! Рады видеть вас у нас. что бы всё получилсь просто напишите слова только большими буквами , и обязательно только 1 слово на 1 вопрос, за 1 запуск данной функции словаря вы сможете узнать значение 5 слов , если у вас допусти 3 слова - то продублируйте последнее слово в оставшихся вопросах , большое спасибо!')
print("           ")
hm = input('Выбирете сколько слов вам потребуеться(1,3,5)')
if hm == '1':
    time.sleep(1)
    word = input("Введите непонятное слово (большими буквами!): ")
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(1)
    print('DONE!')
    time.sleep(3)
    if word in meme_dict.keys():
        print(word,'-',  meme_dict[word])
        time.sleep(1)
    else:
        print('Erorr , try again')
elif hm == '3':
    time.sleep(1)
    word = input("Введите непонятное слово (большими буквами!): ")
    time.sleep(1)
    word1 = input("Введите ещё одно непонятное слово (большими буквами!):")
    time.sleep(1)
    word2 = input("Введите можно и ещё непонятное слово (большими буквами!):")
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(1)
    print('DONE!')
    time.sleep(3)
    if word in meme_dict.keys():
        print(word,'-',  meme_dict[word])
        time.sleep(1)
        print(word1, "-", meme_dict[word1])
        time.sleep(1)
        print(word2, "-", meme_dict[word2])
    else:
        print('Erorr , try again')
elif hm == '5':
    time.sleep(1)
    word = input("Введите непонятное слово (большими буквами!): ")
    time.sleep(1)
    word1 = input("Введите ещё одно непонятное слово (большими буквами!):")
    time.sleep(1)
    word2 = input("Введите можно и ещё непонятное слово (большими буквами!):")
    time.sleep(1)
    word3 = input("Введите и ещё непонятное слово (большими буквами!):")
    time.sleep(1)
    word4 = input("Введите и ещё непонятное слово (большими буквами!):")
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(3)
    print('Loading.')
    time.sleep(1)
    print('Loading..')
    time.sleep(1)
    print('Loading...')
    time.sleep(1)
    print('DONE!')
    time.sleep(3)
    if word in meme_dict.keys():
        print(word,'-',  meme_dict[word])
        time.sleep(1)
        print(word1, "-", meme_dict[word1])
        time.sleep(1)
        print(word2, "-", meme_dict[word2])
        time.sleep(1)
        print(word3, "-", meme_dict[word3])
        time.sleep(1)
        print(word4, "-", meme_dict[word4])
    else:
        print('Erorr , try again')
    
else:
    print('Erorr , try again')
