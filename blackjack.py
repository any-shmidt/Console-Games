import random
import time

hearts = chr(9829)
diamonds = chr(9830)
spades = chr(9824)
clubs = chr(9827)

card_deck = []
dealer_hand = []
player_hand = []

backside = '##'
show_backside = False
playGame = True


def create_deck():
    card_suits = (hearts, diamonds, spades, clubs)
    for suit in card_suits:
        for rank in range(2, 11):
            card_deck.append((str(rank), suit))
        for rank in ('J', 'Q', 'K', 'A'):
            card_deck.append((rank, suit))
    
    random.shuffle(card_deck)
            
    return card_deck
        

def deal_cards(deck):

    global dealer_hand
    global player_hand
    dealer_hand = [card_deck.pop(), card_deck.pop()]
    player_hand = [card_deck.pop(), card_deck.pop()]

    print(dealer_hand)
    print(player_hand)
    
    return dealer_hand, player_hand


def display_card(cards):
    rows = ['', '', '', '', '']
    
    for i, card in enumerate(cards):
        rows[0] += ' ___ '
        rank, suit = card
        rows[1] += f'|{rank.ljust(3)}|'
        rows[2] += f'|{suit.center(3)}|'
        rows[3] += f'|{rank.rjust(3, "_")}|'
            
    for row in rows:
        print(row)


def get_sum_hand_card(cards):
    value = 0
    for card in cards:
        rank = card[0]
        if rank == 'A':
            value += 1
        elif rank in ('J', 'Q', 'K'):
            value += 10
        else:
            value += int(rank)
    
        if 'A' in card:
            if value + 10 < 22:
                value += 10
            
    return value


def display_hand_cards(dealer_hand, player_hand, show_backside):
    if show_backside:
        print('Dealer cards: ', end='')
        print(get_sum_hand_card(dealer_hand))
        display_card(dealer_hand)
    else:
        print('Dealer cards: ?')
        display_card([backside] + dealer_hand[1:])

    print('Your cards: ', end='')
    print(get_sum_hand_card(player_hand))
    display_card(player_hand)
    
    print('-----------------------------')
    

def get_money():
    correct_input = False
    while not correct_input:
        money = input('How much money do you have?\n')
        try:
            money = int(money)
            if money <= 0:
                print('Number must be greater than 0')
            else:
                correct_input = True
        except:
            print('Enter a number!')
    return money


def get_bet():
    correct_bet = False
    while not correct_bet:
        bet = input(f'Your bet (not more than {money}): ')
        try:
            bet = int(bet)
            if bet > money:
                print(f'Bet cannot be more than {money}!')
                continue
            elif bet == 0:
                print('Bet cannot be equal to 0!')
                continue
            else:
                correct_bet = True
        except:
            print('Enter a number!')
            
    return bet


def get_more_cards():
    more_cards = input('Get more cards? yes/no\n').lower()
            
    return more_cards.startswith('y')
            
            
print('B L A C K J A C K')

money = get_money()
bet = get_bet()

while playGame:
    
    create_deck()
    deal_cards(card_deck)
    

    display_hand_cards(dealer_hand, player_hand, show_backside)
    
    if get_sum_hand_card(player_hand) < 21:
        
        if get_more_cards():
            new_card = card_deck.pop()
            player_hand.append(new_card)

            
    while get_sum_hand_card(dealer_hand) < 17:
        new_card = card_deck.pop()
        dealer_hand.append(new_card)
        print('Dealer takes the card')
        time.sleep(1.5)
        display_hand_cards(dealer_hand, player_hand, show_backside)
        
        
    print('Dealer opens the cards')
    time.sleep(1.5)
    show_backside = True
    display_hand_cards(dealer_hand, player_hand, show_backside)


    player_value = get_sum_hand_card(player_hand)
    dealer_value = get_sum_hand_card(dealer_hand)
    
    if dealer_value > 21 and dealer_value > player_value:
        print(f'Dealer busts! You won {bet}!')
        money += bet
    elif player_value == 21 and dealer_value != 21:
        print(f'Blackjack! You won {bet * 1.5}!')
        money += bet * 1.5
    elif player_value > 21 or player_value < dealer_value:
        print('You lose!')
        money -= bet
    elif player_value > dealer_value and player_value <= 21:
        print(f'You won {bet}!')
        money += bet
    elif player_value == dealer_value and player_value <= 21 and dealer_value <= 21:
        print('Push! Your bet stays with you!')
    elif player_value > 21 and dealer_value > 21:
        print('Nobody won! Your bet stays with you!')
    print(f'Remaining money: {money}')
    
    if money == 0:
        playGame = False
        print('You ran out of money')
    
    
    playGame = False
    
    if not playGame and money != 0:
        again = input("Play again? yes/no ")
        if again.startswith('y'):
            playGame = True
            print()
            print('-----------------------------')
            bet = get_bet()
