card_deck = [3, 11, 5, 2, 5, 8]
hand = []

while sum(hand) <= 17:
    hand.append(card_deck.pop())
    print(sum(hand))
    # 8
    # 13
    # 15
    # 20

print(hand) # [8, 5, 2, 5]