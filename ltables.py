"""
Implementation of the Loot Tables and the drop loot and barter procedures.
Author: kyntaz
Date: 12/12/2020
"""

from mcrng import McRng

class BlazeDropper:
    def dropLoot(self):
        rng = McRng.make()
        rn = rng.nextInt(2)
        if rn == 1: return {"item": "Blaze Rod", "n": 1}
        elif rn == 0: return {}
        else: raise RuntimeError("BlazeDropper.dropLoot: Random number not valid.")

class PiglinBarter:
    def __init__(self):
        self.world_rng = McRng.make()
    
    def barter(self, d_time):
        n_calls = int(d_time * 7500)
        for _ in range(n_calls): self.world_rng.next(31) # Simulate random calls

        rn = self.world_rng.nextInt(423)
        if 0 <= rn < 40: return {"item": "Soul Sand", "n": 4 + self.world_rng.nextInt(13)}
        elif 40 <= rn < 80: return {"item": "Crying Obsidian", "n": 1 + self.world_rng.nextInt(3)}
        elif 80 <= rn < 120: return {"item": "Obsidian", "n": 1}
        elif 120 <= rn < 160: return {"item": "Nether Brick", "n": 4 + self.world_rng.nextInt(13)}
        elif 160 <= rn < 200: return {"item": "Leather", "n": 4 + self.world_rng.nextInt(7)}
        elif 200 <= rn < 240: return {"item": "Gravel", "n": 8 + self.world_rng.nextInt(9)}
        elif 240 <= rn < 280: return {"item": "Fire Charge", "n": 1 + self.world_rng.nextInt(5)}
        elif 280 <= rn < 300: return {"item": "String", "n": 8 + self.world_rng.nextInt(17)}
        elif 300 <= rn < 320: return {"item": "Ender Pearl", "n": 4 + self.world_rng.nextInt(5)}
        elif 320 <= rn < 340: return {"item": "Magma Cream", "n": 2 + self.world_rng.nextInt(5)}
        elif 340 <= rn < 360: return {"item": "Glowstone Dust", "n": 5 + self.world_rng.nextInt(8)}
        elif 360 <= rn < 380: return {"item": "Nether Quartz", "n": 8 + self.world_rng.nextInt(9)}
        elif 380 <= rn < 390: return {"item": "Potion of Fire Resistance", "n": 1}
        elif 390 <= rn < 400: return {"item": "Splash Potion of Fire Resistance", "n": 1}
        elif 400 <= rn < 410: return {"item": "Iron Nugget", "n": 9 + self.world_rng.nextInt(28)}
        elif 410 <= rn < 418: return {"item": f"Iron Boots (Soul Speed {1 + self.world_rng.nextInt(3)}", "n": 1}
        elif 418 <= rn < 423: return {"item": f"Enchanted Book (Soul Speed {1 + self.world_rng.nextInt(3)}", "n": 1}
        else: raise RuntimeError("PiglinBarter.barter: Random number not valid.")

# Test:
from tqdm import tqdm

def test_barter(trials):
    piglin = PiglinBarter()
    counts = {}
    trials = int(trials)
    for _ in tqdm(range(trials)):
        item = piglin.barter(6)
        if not item["item"] in counts:
            counts[item["item"]] = 0
        counts[item["item"]] += 100 / trials

    return counts
