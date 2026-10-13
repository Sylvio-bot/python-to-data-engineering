import random

coin = random.choice(["head","tails"])
print(coin)

print("random.randint(a,b) return a integer between a and b")
number_winner = random.randint(1, 10)
print(number_winner)

cards = ["jack", "queen", "king"]
print("shuffle")
random.shuffle(cards)
print(cards)
