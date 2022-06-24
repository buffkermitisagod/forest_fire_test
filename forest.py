import random
import time
from colorama import Fore, init

init()

"""
main rule set:

    A burning cell turns into an empty cell
    A tree will burn if at least one neighbor is burning
    A tree ignites with probability f even if no neighbor is burning
    An empty space fills with a tree with probability p

"""

m = [[" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "],
     [" ", " ", " ", " ", " ", " ", " ", " ", " "]]

smbol = {
    "tree": "T",
    "fire": "F",
    "empt": " "
}

p = 50
f = 50

def print_map(ma):
    for i in ma:
        for x in i:
            print(" ", end="")
            if x == smbol["tree"]:
                print(Fore.GREEN+x+Fore.RESET, end="")
            elif x == smbol["fire"]:
                print(Fore.RED+x+Fore.RESET, end="")
            else:
                print(x, end="")
        print("\n")
    print("\n")

def proc_map(ma):
    global smbol, f, p
    for i in range(len(ma)):
        line = ma[i]
        for x in range(len(line)):
            char = line[x]
            skip_empt = False

            # basic check if fire starts or tree grows
            if char == smbol['tree']:
                if random.randint(0, 100) <= f:
                    char = smbol["fire"]
            elif char == smbol["empt"]:
                if random.randint(0, 100) <= p:
                    char = smbol["tree"]
            elif char == smbol["fire"]:
                char = smbol["empt"]
                skip_empt = True
            
            # calc if tree starts burning
            if char == smbol["tree"]:
                try:
                    if line[x-1] == smbol["fire"]:
                        if random.randint(0, 100) <= f:
                            char = smbol["fire"]
                except IndexError:
                    pass

                try:
                    if line[x+1] == smbol["fire"]:
                        if random.randint(0, 100) <= f:
                            char = smbol["fire"]
                except IndexError:
                    pass

                try:
                    if ma[i-1][x] == smbol["fire"]:
                        if random.randint(0, 100) <= f:
                            char = smbol["fire"]
                except IndexError:
                    pass

                try:
                    if ma[i+1][x] == smbol["fire"]:
                        if random.randint(0, 100) <= f:
                            char = smbol["fire"]
                except IndexError:
                    pass

            if char == smbol["empt"] and skip_empt == False:
                if random.randint(0, 100) <= p:
                    char = smbol["tree"]
            
            # update the map
            line[x] = char
        ma[i] = line
    return ma

def run(ma):
    print_map(ma)
    while True:
        ma = proc_map(ma)
        print_map(ma)
        time.sleep(2)
