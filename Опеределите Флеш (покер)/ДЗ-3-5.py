
table_cards = ["A_S", "J_H", "7_D", "8_D", "10_D"]
hand_cards = ["J_D", "3_D"]

# ваше решение ниже:

table_suits = [x[-1] for x in table_cards]
hand_suits = [x[-1] for x in hand_cards]

game_suits = table_suits + hand_suits

flush = any([game_suits.count(suits) >= 5 for suits in 'SHCD'])
if flush:
    print('Flush!')
else:
    print('No Flush!')










