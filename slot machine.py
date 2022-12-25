import random
import time

play_slot_machine = True
slot_money = 0

print('ОДНОРУКИЙ БАНДИТ')

one = None
two = None
three = None
four = None
five = None


def get_slots():
    print(one, end=' | ')
    time.sleep(0.5)
    print(two, end=' | ')
    time.sleep(0.5)
    print(three, end=' | ')
    time.sleep(0.5)
    print(four, end=' | ')
    time.sleep(0.5)
    print(five)
    

def get_result():
    if any(value == 5 for key, value in count_dict.items()):
        print('Совпало 5 чисел! Выигрыш 10:1')
        return 5
    elif any(value == 4 for key, value in count_dict.items()):
        print('Совпало 4 числа! Выигрыш 5:1')
        return 4
    elif any(value == 3 for key, value in count_dict.items()):
        print('Совпало 3 числа! Выигрыш 2:1')
        return 3
    elif any(value == 2 for key, value in count_dict.items()):
        print('Совпало 2 числа! Ставка не спиывается')
        return 2
    else:
        print('Не совпало ни одного числа! Вы проиграли {bet}')
        return 1
        

correct_input = False
while not correct_input:
    money = input('Сколько всего денег: ')
    try:
        money = int(money)
        if money <= 0:
            print("Сумма длжна быть больше 0.")
        else:
            correct_input = True
    except:
        print("Введи число!")
        
        
while play_slot_machine:
    slot_list = []
    correct_bet = False
    while not correct_bet:
        bet = input(f'Ставка (не больше {money}). Если хочешь выйти - введи 0: ')
        try:
            bet = int(bet)
            if bet > money:
                print(f'Ставка должна быть не больше {money}!')
                continue
            elif bet == 0:
                play_slot_machine = False
                break
        except:
            print('Введи число!')
        else:
            correct_bet = True
            one = random.randint(0, 9)
            two = random.randint(0, 9)
            three = random.randint(0, 9)
            four = random.randint(0, 9)
            five = random.randint(0, 9)
            #print(slot_list)
            get_slots()
            slot_list = [one, two, three, four, five]
            count_list = []
            for i in slot_list:
                count_list.append(slot_list.count(i))
            #print(count_list)
    
            count_dict = dict(zip(slot_list, count_list))
            #print(count_dict)
            get_result()
            result = get_result()
            print(result)
            if result == 5:
                money += bet * 10
                print(f'Твой выигрыш {bet * 10}. У тебя на счету {money}')
            elif result == 4:
                money += bet * 5
                print(f'Твой выигрыш {bet * 5}. У тебя на счету {money}')
            elif result == 3:
                money += bet * 2
                print(f'Твой выигрыш {bet * 2}. У тебя на счету {money}')
            elif result == 2:
                print(f'У тебя на счету {money}')
            elif result == 1:
                money -= bet
                print(f'Ты проиграл! У тебя на счету {money}')
                
            if money == 0:
                play_slot_machine = False
                print('YOU LOSE! NO MORE MONEY!')
                break