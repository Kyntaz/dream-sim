"""
Implementation of Java random number generation, as it is used in Mincecraft.
Author: kyntaz
Date: 12/12/2020
"""

import time

SEED_UNIQUIFIER = 8682522807148012

def logic_rshift(val,n): return (val % 0x100000000) >> n

def seedUniquifier():
    global SEED_UNIQUIFIER
    SEED_UNIQUIFIER = SEED_UNIQUIFIER * 181783497276652981
    return SEED_UNIQUIFIER

class McRng:
    def __init__(self, seed):
        self.seed = seed

    def reset(self, seed):
        self.seed = seed

    def next(self, bits):
        self.seed = (self.seed * 0x5DEECE66D + 0xB) & ((1 << 48) - 1)
        return int(logic_rshift(self.seed, 48-bits))

    def nextInt(self, bound):
        if (bound <= 0): raise ValueError("McRng.nextInt: bound < 0")
        if ((bound & -bound) == bound): # bound == 2^n
            return int(bound * self.next(31)) >> 31
        
        bits = self.next(31)
        val = bits % bound
        while (bits - val + (bound - 1) < 0):
            bits = self.next(31)
            val = bits % bound
        return val

    @staticmethod
    def make():
        return McRng(seedUniquifier() ^ time.time_ns())
