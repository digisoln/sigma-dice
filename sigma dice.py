import random
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)

if dice1 > dice2:
    score = str(dice1) + str(dice2)
else:
    score = str(dice2) + str(dice1)

print(score)