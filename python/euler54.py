# In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

# High Card: Highest value card.
# One Pair: Two cards of the same value.
# Two Pairs: Two different pairs.
# Three of a Kind: Three cards of the same value.
# Straight: All cards are consecutive values.
# Flush: All cards of the same suit.
# Full House: Three of a kind and a pair.
# Four of a Kind: Four cards of the same value.
# Straight Flush: All cards are consecutive values of same suit.
# Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
# The cards are valued in the order:
# 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

# If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

# Consider the following five hands dealt to two players:

# Hand	 	Player 1	 	Player 2	 	Winner 
#                                                                      
# 1	     5H 5C 6S 7S KD          2C 3S 8S 8D TD            Player 2
#            Pair of fives           Pair of eights                    
#                                                                      
# 2          5D 8C 9S JS AC          2C 5C 7D 8S QH            Player 1
#            High card ace           High card queen                   
#                                                                      
# 3          2D 9C AS AH AC          3D 6D 7D TD QD            Player 2
#            Three aces              Diamond flush                     
#                                                                      
# 4          4D 6S 9H QH QC          3D 6D 7H QD QS            Player 1
#            Pair of queens          Pair of queens                    
#            High card 9             High card 7                       
#                                                                      
# 5          2H 2D 4C 4D 4S          3C 3D 3S 9S 9D            Player 1
#            Full house              Full house                        
#            Three fours             Three threes                      

# The file, data/euler54_input.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

# How many hands does Player 1 win?


from euler import read_input
from decorator import time_and_memory_decorator as tamd
import inspect

filename = f'{inspect.getmodule(inspect.stack()[0][0]).__file__[36:-3]}'

card_values = \
    {
        '2' : 2,
        '3' : 3,
        '4' : 4,
        '5' : 5,
        '6' : 6,
        '7' : 7,
        '8' : 8,
        '9' : 9,
        'T' : 10,
        'J' : 11,
        'Q' : 12,
        'K' : 13,
        'A' : 14
    }


def find_highest_card(hand):
    high_card = 0

    for card in hand:
        if card_values[card[0]] > high_card:
            high_card = card_values[card[0]]
    return high_card



# Tested, working
def is_royal_flush(hand):
    if not is_flush(hand):
        return False

    hand_values = [card[0] for card in hand]

    return sorted(['T', 'J', 'Q', 'K', 'A']) == sorted(hand_values)

# Tested, working
def is_straight_flush(hand):
    if is_straight(hand) != False and is_flush(hand) != False:
        return True
    
    return False

# Tested, working
def is_four_of_kind(hand):
    cards = {}
    for card in hand:
        try:
            cards[card[0]] += 1
        except KeyError as _:
            cards[card[0]] = 1
            
    for card, count in cards.items():
        if count == 4:
            return card

    return False

# Tested, working
def is_full_house(hand):
    
    if is_three_of_kind(hand) != False and is_one_pair(hand) != False:
        d = {}
        for card in hand:
            try:
                d[card[0]] += 1
            except KeyError as _:
                d[card[0]] = 1
        return d
    return False
    

# Tested, working
def is_flush(hand):
    suit = hand[0][1]

    for card in hand:
        if card[1] != suit:
            return False
        
    return True

# Tested, working
def is_straight(hand):
    card_scores = []
    for card in hand:
        card_scores.append(card_values[card[0]])
    card_scores.sort()

    for index, score in enumerate(card_scores):
        if card_scores[0] + index != score:
            return False
            
    return True

# Tested, working
def is_three_of_kind(hand):
    cards = {}
    for card in hand:
        try:
            cards[card[0]] += 1
        except KeyError as _:
            cards[card[0]] = 1
            
    for card, count in cards.items():
        if count == 3:
            return card

    return False


# Tested, working
def is_two_pair(hand):
    cards = {}
    pairs = 0
    pair_values = []
    for card in hand:
        try:
            cards[card[0]] += 1
        except KeyError as _:
            cards[card[0]] = 1

    for card, count in cards.items():
        if count == 2:
            pairs += 1
            pair_values.append(card)
            
    if pairs == 2:
        return pair_values
    
    else:
        return False


# Tested, working
def is_one_pair(hand):
    cards = {}
    for card in hand:
        try:
            cards[card[0]] += 1
        except KeyError as _:
            cards[card[0]] = 1
            
    for card, count in cards.items():
        if count == 2:
            return card

    return False


ordered_tests = [is_royal_flush, is_straight_flush, is_four_of_kind, is_full_house, is_flush, is_straight, is_three_of_kind, is_two_pair, is_one_pair]
ordered_scores = [i for i in range(110,29,-10)]

def score_hand(hand):
    for test, score in zip(ordered_tests, ordered_scores):
        if test(hand) != False:
            return score
    return find_highest_card(hand)


def high_card_tiebreaker(p1hand, p2hand):
   
    while len(p1hand) > 0:
        p1high = 0
        p2high = 0
        p1high_card = 0
        p2high_card = 0
        
        for card1, card2 in zip(p1hand, p2hand):
            
            if card_values[card1[0]] > p1high:
                p1high = card_values[card1[0]]
                p1high_card = card1
                
            if card_values[card2[0]] > p2high:
                p2high = card_values[card2[0]]
                p2high_card = card2

        if p1high > p2high:
            return 1
        
        elif p1high < p2high:
            return 2

        else:
            p1hand.remove(p1high_card)
            p2hand.remove(p2high_card)
    print("What the fuck, bruh?")
    return False

def tiebreaker(tie_score, p1hand, p2hand):
    found_function = False
    for index, score in enumerate(ordered_scores):
        if score == tie_score:
            found_function = True
            tie_test = ordered_tests[index]
            break
        
    if not found_function:
        return high_card_tiebreaker(p1hand, p2hand)
    
    elif tie_test in (is_royal_flush, is_straight_flush, is_flush, is_straight):
        return high_card_tiebreaker(p1hand, p2hand)

    else:
        
        if tie_test == is_two_pair:
            if max(card_values[tie_test(p1hand)]) > max(card_values[tie_test(p2hand)]):
                return 1
            elif max(card_values[tie_test(p1hand)]) < max(card_values[tie_test(p2hand)]):
                return 2
            else:
                return high_card_tiebreaker(p1hand, p2hand)
        
        elif tie_test == is_full_house:
            if card_values[is_three_of_kind(p1hand)] > card_values[is_three_of_kind(p2hand)]:
                return 1
            else:
                return 2
            
        else:
            if card_values[tie_test(p1hand)] > card_values[tie_test(p2hand)]:
                return 1
            elif card_values[tie_test(p1hand)] < card_values[tie_test(p2hand)]:
                return 2
            else:
                return high_card_tiebreaker(p1hand, p2hand)
        

    

@tamd
def find_answer():
    p1wins = 0
    p2wins = 0
    input_data = read_input(filename)
    
    player_1_hands = []
    player_2_hands = []
    
    for hands in input_data:
        hands = hands.strip().split(' ')
        player_1_hands.append(hands[:5])
        player_2_hands.append(hands[5:])


    # 2 1 2 1 1
    # 1 : 3
    # 2 : 2
    for hand_index, (p1hand, p2hand) in enumerate(zip(player_1_hands, player_2_hands)):
        p1score = score_hand(p1hand)
        p2score = score_hand(p2hand)
        
        if p1score > p2score:
            p1wins += 1
            
        elif p1score < p2score:
            p2wins += 1
            
        else:
            tie_break = tiebreaker(p1score, p1hand, p2hand)
            if tie_break == 1:
                p1wins += 1
                
            elif tie_break == 2:
                p2wins += 2
                
            else:
                print(f'Hand {hand_index+1} is a tie')

    return p1wins

if __name__ == '__main__':
    print(filename, ": ", end="")
    
    answer, mem, time = find_answer()

    print(answer)
    print(mem)
    print(time)
