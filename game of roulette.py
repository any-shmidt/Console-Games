import random


play_roulette = True

def even():
    if number % 2 == 0:
        print(f"You win! Твой выигрыш = {bet * 2}")
        return bet * 2
    else:
        print(f"You lose! Ты проиграл {bet}")
        return - bet


def odd():
    if number % 2 != 0:
        print(f"You win! Твой выигрыш = {bet * 2}")
        return bet * 2
    else:
        print(f"You lose! Ты проиграл {bet}")
        return - bet


def dozen():     
    if dozen_choice == 1:
        if number >= 1 and number <= 12:
            print(f"You win! Твой выигрыш = {bet * 3}")
            return bet * 3
        else:
            print(f"You lose! Ты проиграл {bet}")
            return - bet
    elif dozen_choice == 2:
        if number >= 13 and number <= 24:
            print(f"You win! Твой выигрыш = {bet * 3}")
            return bet * 3
        else:
            print(f"You lose! Ты проиграл {bet}")
            return - bet
    elif dozen_choice == 3:
        if number >= 25 and number <= 36:
            print(f"You win! Твой выигрыш = {bet * 3}")
            return bet * 3
        else:
            print(f"You lose! Ты проиграл {bet}")
            return - bet


def number_bet():
    if number == number_choice:
        print(f"You win! Твой выигрыш = {bet * 36}")
        return bet * 36
    else:
        print(f"You lose! Ты проиграл {bet}")
        return - bet

#def play_again():

correct_input = False
while not correct_input:
    money = input("Сколько всего денег: ")
    try:
        money = int(money)
        if money <= 0:
            print("Сумма длжна быть больше 0.")
        else:
            correct_input = True
    except:
        print("Введи число!")

while play_roulette:
    print('*' * 30)
    print(f"У тебя на счету: {money}")
    correct_bet_choice = False
    while not correct_bet_choice:
        bet_choice = input("""На что ставим?
1 - на четное,
2 - на нечетное,
3 - на дюжину,
4 - на число:\n""")
        try:
            bet_choice = int(bet_choice)
            if bet_choice < 1 or bet_choice > 4:
                continue
            else:
                correct_bet_choice = True
        except ValueError:
            print("Введи число!")
    
    if bet_choice == 3:
        correct_dozen_choice = False
        while not correct_dozen_choice:
            dozen_choice = input("""На какую дюжину ставим?
1 - 1-12,
2 - 13-24,
3 - 25-36:\n""")
            try:
                dozen_choice = int(dozen_choice)
                if dozen_choice < 1 or dozen_choice > 3:
                    continue
                else:
                    correct_dozen_choice = True
            except:
                print("Введи число!")

        
    if bet_choice == 4:
        correct_number_choice = False
        while not correct_number_choice:
            number_choice = input("На какое число ставишь? (1-36): ")
            try:
                number_choice = int(number_choice)
                if number_choice < 1 or number_choice > 36:
                    print("Введи число от 1 до 36 включительно!")
                    continue
                else:
                    correct_number_choice = True
            except:
                print("Введи число от 1 до 36 включительно!")
    
    correct_bet = False
    while not correct_bet:
        bet = input(f"Сколько ставишь (не больше {money}): ") # ставка
        try:
            bet = int(bet)
            if bet > money:
                print(f"Ставка не может быть больше {money}!")
                continue
            elif bet == 0:
                print("Ставка не может быть равна 0!")
                continue
            else:
                correct_bet = True
        except:
            print("Введи число!")
    
    number = random.randint(0, 38)
    if number == 0:
        print('Выпало зеро (0)')
    elif number > 0 and number <= 37:
        print(f'Выпало число {number}')
    elif number == 38:
        print('Выпало двойное зеро (00)')
    
    if bet_choice == 1:
        money_amount = even() # money_amount - сумма выигыша или проигранна сумма
        money += money_amount
        print(f"Осталось денег: {money}")
        
    if bet_choice == 2:
        money_amount = odd()
        money += money_amount
        print(f"Осталось денег: {money}")
    
    if bet_choice == 3:
        money_amount = dozen()
        money += money_amount
        print(f"Осталось денег: {money}")
        
    if bet_choice == 4:
        money_amount = number_bet()
        money += money_amount
        print(f"Осталось денег: {money}")
    
    if money == 0:
        play_roulette = False
        print("NO MORE MONEY")
    else:
        again = input("Play again? yes/no ")
        if again == "no":
            play_roulette = False