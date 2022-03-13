# -*- coding: utf-8 -*-
"""
Created on Sat Mar 12 19:14:17 2022
Given an amount in [1, 99] cents, make change
Follow a greedy heuristic, giving back the fewest possible number of coins
@author: apt4c
"""

class ChangeMaker:
    def __init__(self, denoms):
        self.denoms = denoms # change denominations
        self.lower = 0       # lower bound
        self.upper = 100     # upper bound
        
    def initialize_coins(self):
        '''
        set the initial coin counts to zero for each denomination
        '''
        self.coins = {denom:0 for denom in self.denoms}
        
    def make_change(self, target):
        '''
        Use greedy algorithm to make change (use max quarters, then dimes, ...)
        '''
        
        # validate the target
        assert target > self.lower, "target must be > 0"
        assert target < self.upper, "target must be < $1"
        
        self.initialize_coins()
        
        while target > self.lower:
            for denom in denoms:
                if target >= denom:
                    quotient = target // denom
                    self.coins[denom] += quotient
                    target -= denom * quotient

###########
        
# set up parameters
denoms = [25,10,5,1]
test_amounts = [99,75,74,24,11,9,4]

# Create ChangeMarker object
cm1 = ChangeMaker(denoms)

for amt in test_amounts:
    cm1.make_change(amt)
    print('test amount:', amt)
    print(cm1.coins, '\n')

# edge cases
cm1.make_change(101)
cm1.make_change(-1)


# Question 1: What small change can be made to give back the largest number of coins?

# Question 2: Can you think of code modifications to make change following a different heuristic?