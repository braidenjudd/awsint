cards = range(1, 53)
shuffled_cards = []

import random

while len(cards) > 0:
	i = random.randint(0, len(cards) - 1)
	shuffled_cards.append(cards[i])
	del(cards[i])

print(shuffled_cards)