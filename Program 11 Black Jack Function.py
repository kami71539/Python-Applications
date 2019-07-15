#Black Jack Function
def hand_total(hand):
    total=0
    aces=0
    for card in hand:
        if card in['J','Q','K']:
            total=total+10
        elif card=='A':
            aces=aces+1
        else:
            total=total+int(card)
    total=total+aces
    while total<=21 and aces !=0:
        total=total+10
        aces=aces-1
    return total
def blackjack(hand_1,hand_2):
    player_total=hand_total(hand_1)
    dealer_card_val=hand_total(hand_2)
    return total_1 <=21 and (total_1>total_2 or total_2>21)