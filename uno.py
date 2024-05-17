import random

def build_deck():
    deck = []
    colors = ['Red', 'Green', 'Yellow', 'Blue']
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'Draw Two', 'Skip', 'Reverse']  
    wilds = ['Wild', 'Wild Draw Four']

    for color in colors:
        for value in values:
            card_value = f'{color} {value}'
            deck.append(card_value)
            if value != 0:
                deck.append(card_value)

    for i in range(4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

def shuffle_deck(deck):
    for card_position in range(len(deck)):
        random_position = random.randint(0,107)
        deck[card_position], deck[random_position] = deck[random_position], deck[card_position]
    return deck

def draw_cards(num_cards):
    cards_drawn = []
    for x in range(num_cards):
        cards_drawn.append(uno_deck.pop(0))
    return cards_drawn

def show_hand(player, player_hand):
    print(f'{player+1}\'s turn. ')
    print('It is your hand')
    print('****************************')
    y = 1
    for card in player_hand:
        print(f'{y}) {card} ')
        y+=1
    print('')

def playable(color, value, player_hand):
    for card in player_hand:
        if 'Wild' in card:
            return True
        elif color in card or value in card:
            return True
    return False

uno_deck = build_deck()
uno_deck = shuffle_deck(uno_deck)
uno_deck = shuffle_deck(uno_deck)
discards = []

players = []
colors = ['Red', 'Green', 'Yellow', 'Blue']
num_players = int(input('How many players? '))
while num_players<2 or num_players>4:
    num_players = int(input('Invalid number, Please enter a number beetwen 2 and 4. '))
for player in range(num_players):
    players.append(draw_cards(7))

player_turn = 0
player_direction = 1
playing = True
discards.append(uno_deck.pop(0))
starter = discards[0].split(' ', 1)
current_color = starter[0]
if current_color != 'Wild':
    card_value = starter[1]
else:
    card_value = 'Any'

while playing:
    show_hand(player_turn, players[player_turn])
    print(f'Card on top of discard pile: {discards[-1]}')
    if playable(current_color, card_value, players[player_turn]):
        card_chosen = int(input('Which card do you want to play? '))
        while not playable(current_color, card_value, [players[player_turn][card_chosen-1]]):
            card_chosen = int(input('Not a valid card. Please chose valid card for playing. '))
        print(f'You played {players[player_turn][card_chosen-1]}')
        discards.append(players[player_turn].pop(card_chosen-1))

        if len(players[player_turn])==0:
            playing = False
            winner = f'Player {player_turn+1}'   
        else:
            starter = discards[-1].split(' ', 1)
            current_color = starter[0]
            if len(starter) == 1:
                card_value = 'Any'
            else:
                card_value = starter[1]
            if current_color == 'Wild':
                for x in range(len(colors)):
                    print(f'{x+1}) {colors[x]}')
                new_color = int(input('What color would you like to choose? '))
                while new_color < 1 or new_color > 4:
                    new_color = int(input('Invalid option. What color would you like to choose? '))
                current_color = colors[new_color-1]
                print(f'\ncurrent color is: {current_color}')
            if card_value == 'Reverse':
                player_direction*=-1
            elif card_value == 'Skip':
                player_turn += player_direction
                if player_turn>=num_players:
                    player_turn = 0
                elif player_turn < 0: 
                    player_turn = num_players-1
            elif card_value == 'Draw Two':
                player_draw = player_turn + player_direction
                if player_draw==num_players:
                    player_draw = 0
                elif player_draw < 0: 
                    player_draw = num_players-1
                players[player_draw].extend(draw_cards(2))
            elif card_value == 'Draw Four':
                player_draw = player_turn + player_direction
                if player_draw==num_players:
                    player_draw = 0
                elif player_draw < 0: 
                    player_draw = num_players-1
                players[player_draw].extend(draw_cards(4))
            print('')   

    else:
        print('You cant play you must draw a card.')
        players[player_turn].extend(draw_cards(1))
    print('')

    player_turn+=player_direction 
    if player_turn>=num_players:
        player_turn = 0
    elif player_turn < 0: 
        player_turn = num_players-1

print('Game Over')
print(f'{winner} is the Winner!')