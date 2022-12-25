import random

low_digit = 10
high_digit = 50

digit = random.randint(low_digit, high_digit)

playgame = True
win = False
count_input = 0
score = 0

prompt = 'Введите число от 10 до 50: '

print('Компьютер загадал число от 10 до 50')
print('Попробуйте его угадать.\nУ вас есть 10 попыток')

while playgame:
    count_input +=1
    print('*' * 30)
    print(f'\n{count_input} попытка')
    x = input(prompt)
    
    while (not x.isdigit()):
        x = input(prompt)
        if (not x.isdigit()):
            print('enter the number')
        
    x = int(x)
    
    if x == digit:
        playgame = False
        print('You win!')
    else:
        if digit < x:
            print('Загаданное число меньше')
        else:
            print('Загаданное число больше')
    
    if count_input == 5:
        if digit % 2 == 0:
            print('Число четное')
        else:
            print('Число нечетное')
    
    if count_input == 10:
        playgame = False
        print('You lose!')
        print('Попыток больше нет!')
