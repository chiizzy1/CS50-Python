import random
# get random number from a list of random numbers

# coin = random.choice(['heads', 'tails'])
# print(coin)


# get random number from a range of numbers

# number = random.randint(1, 10)
# print(number)

cards = ['jack', 'queen', 'king']
random.shuffle(cards)
for card in cards:
    print(card)