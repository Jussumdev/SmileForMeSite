
import math
import keyboard
import time


deck_lengths = [15, 15, 16, 45, 45, 45, 45]

cards_per_day = 15
#a sequence decks, defined by (number of cards, base cost, base income per second)
decks = [   (15, 15, 0.1),
            (15, 300, 1),
            (16, 110000, 8),
            (45, 12000000, 47),
            (45, 400000000, 2600),
            (45, 35000000000, 14000),
            (45, 8000000000000, 78000)
        ]
time_passed = 0
currency = decks[0][1]

#def upgradeDeck(index):
deck_multiplier = []
deck_level = []
for num in decks:
    deck_multiplier.append(1)
    deck_level.append(0)

updateTime = int(input("Enter time per update (in seconds): "))

num_upgrade_intervals = 8
target_mult = 2048
def addMultiplier(index, num = 1):
    single_multiplier = target_mult ** (1 / (num_upgrade_intervals * decks[index][0]))
    deck_multiplier[index] *= single_multiplier ** num


#gets the per-hour income at this moment
def getIncome():
    total_income = 0
    for i in range(len(decks)):
        total_income += deck_level[i] * deck_multiplier[i] * decks[i][2]
    return total_income

def getPrice(index):
    return decks[index][1] * (1.15 ** deck_level[index])

def buyAvailable(currency, wait_for_new = False):
    for i in range(len(decks)):
        index = len(decks) - i - 1

        if (wait_for_new and deck_level[index] > 0):
            pass
        else:
            cost = getPrice(index)
            if (currency >= cost):
                currency -= cost
                deck_level[index] += 1
                ## TEMP:
                if (deck_level[index] == 1):
                    addMultiplier(index, cards_per_day)
                currency = buyAvailable(currency)
                break
    return currency

def printStatus(income, currency, time_passed):
    print("Time Passed: "+str(time_passed // 60)+" minutes, "+str(time_passed % 60)+" seconds.")
    print("Income: "+str(income)+"/sec")
    print("Currency: "+str(currency)+"")
    for i in range(len(decks)):
        print("Lvl "+str(deck_level[i])+"\t\tCost "+str(getPrice(i)))

#buy first building
buyAvailable(currency);
print(deck_multiplier)

held = False
while(True):
    input = keyboard.is_pressed('spacebar')
    smooth_input = keyboard.is_pressed('z')
    if ((not held and input) or smooth_input):
        held = True
        #------------------------------
        income = getIncome()
        currency += income * updateTime
        if (not smooth_input):
            currency = buyAvailable(currency)
        else:
            currency = buyAvailable(currency, True)
        time_passed += updateTime
        printStatus(income, currency, time_passed)
        #------------------------------
    elif (input):
        pass
    else:
        held = False
    time.sleep(0.05)
