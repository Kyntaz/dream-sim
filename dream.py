"""
Simulation of Dream's behavior and probability computation.
Author: kyntaz
Date: 12/12/2020
"""

from ltables import PiglinBarter, BlazeDropper
import random

class Environment:
    def __init__(self):
        self.reset()
        self.cIngots = 0
        self.cPTrades = 0
        self.cBlazes = 0
        self.cRods = 0

    def reset(self):
        self.n_pearls = 0
        self.n_blazes = 0
        self.n_piglins = random.randint(1,4)
        self.piglinBarter = PiglinBarter()
        self.blazeDropper = BlazeDropper()
        self.time_skip = random.randint(300, 600)
    
    def killBlaze(self):
        self.cBlazes += 1
        items = self.blazeDropper.dropLoot()
        if items == {}: return
        self.n_blazes += items["n"]
        self.cRods += 1

    def barter(self,bars):
        if bars > self.n_piglins:
            bars = self.n_piglins
        self.cIngots += bars
        items = []
        items.append(self.piglinBarter.barter(6 + self.time_skip))
        self.time_skip = 0
        for _ in range(bars - 1):
            items.append(self.piglinBarter.barter(0))

        for item in items:
            if item["item"] != "Ender Pearl": continue
            self.n_pearls += item["n"]
            self.cPTrades += 1

class Dream:
    def __init__(self):
        self.env = Environment()
        self.data = []
        self.give_up = True
        self.attempts = 262

    def getPearls(self):
        while self.env.cIngots < self.attempts:
            print("Reseting the game.")
            self.env.reset()
            n_gold = random.randint(5,30)
            while n_gold > 0:
                self.data.append((self.env.cIngots, self.env.cPTrades))

                give = random.randint(min(2,n_gold),min(7,n_gold))
                n_gold -= give
                print(f"Giving {give} gold.")
                while give > 0:
                    g = min(give, self.env.n_piglins)
                    give -= g
                    self.env.barter(g)
                if self.env.n_pearls == 0 and self.give_up:
                    print("Giving up.")
                    break
                print(f"Got {self.env.n_pearls} total.")
                print(f"Got {n_gold} gold left.")

# Trials:

def monteCarlo_pearls(file):
    i = 1

    with open(file, 'w') as f:
        while True:
            print(f"\nStarting trial {i}.")
            i += 1
            dream = Dream()
            dream.give_up = False
            dream.getPearls()

            f.write(str(dream.data) + "\n")
