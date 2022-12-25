import random

def play_again():
    game = input('Сыграть снова? да / нет\n')
    return game.lower().startswith('д')

def hangman_game():
    HANGMAN_PICS = ['''
+---+
    |
    |
    |
   ===''', '''
+---+
  0 |
    |
    |
   ===''', '''
+---+
  0 |
  | |
    |
   ===''', '''
+---+
  0 |
 /| |
    |
   ===''', '''
+---+
  0 |
 /|\|
    |
   ===''', '''
+---+
  0 |
 /|\|
 /  |
   ===''', '''
+---+
  0 |
 /|\|
 / \|
   ===''']

    count = 0 # количество неправильных попыток
    playGame = True
    correct_list = []
    incorrect_list = []


    words_dict = {'Фрукт': 'банан яблоко'.split(),
                  'Техника': 'компьютер холодильник утюг'.split(),
                  'Музыкальные инструменты': 'гитара пианино скрипка аккордеон'.split(),
                  'Транспорт': 'трамвай автобус поезд метро автомобиль самолет'.split(),
                  'Науки': 'психология астрономия биология физика'.split(),
                  'Цвет': 'черный красный голубой серый'.split(),
                  'Фигура': 'квадрат круг треугольник'.split(),
                  'Страна': 'германия англия россия'.split()}

    word_key = random.choice(list((words_dict).keys()))

    secret_word = random.choice(list(words_dict[word_key]))

    print('В И С Е Л И Ц А')
    print(HANGMAN_PICS[0])
    blanks = '_' * len(secret_word)
    print(blanks)

    while playGame:
        print(f'Загаданное слово относится к категории "{word_key}"')
        guess = input('Введите букву: ')
        guess.lower()
        if len(guess) != 1:
            print('Введите ОДНУ букву: ')
        if guess not in 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя':
            print('Введите БУКВУ')
        if guess in secret_word:
            if guess not in correct_list:
                correct_list.append(guess)
                for i in range(len(secret_word)):
                    if secret_word[i] in correct_list:
                        blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
            else:
                print('Эта буква уже угадана')
            print(HANGMAN_PICS[count])

        if guess not in secret_word:
            if guess in incorrect_list:
                print('Вы уже называли эту букву')
            if guess not in incorrect_list:
                incorrect_list.append(guess)
                count += 1
            
            print(HANGMAN_PICS[count])
    
        print(blanks)
        
        if blanks.count('_') == 0:
            print('YOU WIN!')
            playGame = False
        
        if count == len(HANGMAN_PICS) - 1:
            print('GAME OVER! YOU LOSE!')
            print(f'Было загадано слово "{secret_word}"')
            playGame = False
        
hangman_game()
while play_again():
    hangman_game()