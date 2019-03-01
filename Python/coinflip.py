"""
Coinflip program
"""
import random
number = input("How many times would you like to flip the coin? ")
flipNumber = int(number)
resultList = []
for i in range(flipNumber):
    flip = random.randint(0,1)
    if (flip == 0):
        print("Heads!")
        resultList.append("Heads")
    else:
        print("Tails!")
        resultList.append("Tails")
print(str(resultList))
print("Heads appeared " + str(resultList.count("Heads")) + " times")
print("Tails appeared " + str(resultList.count("Tails")) + " times")