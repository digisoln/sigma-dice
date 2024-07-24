import random
dice1 = random.randint(1,9)
dice2 = random.randint(1,9)
if dice1 > dice2:
    score = str(dice1) + str(dice2)
else:
    score = str(dice2) + str(dice1)
print("Side by side:", score)
print("Sum of both:", dice1+dice2)
