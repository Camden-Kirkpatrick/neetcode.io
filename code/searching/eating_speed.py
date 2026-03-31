# Koko Eating Bananas (Binary Search on the Answer)
#
# This program demonstrates how to use binary search to find
# the minimum eating speed needed to finish all banana piles
# within a limited number of hours.
#
# Koko can decide on one eating speed:
#   bananas_per_hour
#
# She must use that same speed for every pile.
#
# For each pile:
#   - If the pile has fewer bananas than her speed,
#     it still takes 1 full hour
#   - If the pile has more bananas than her speed,
#     it may take multiple hours
#
# The goal is to find the smallest eating speed that allows
# her to finish all piles within max_hours.
#
#
# How This Works
#
# 1. Search possible eating speeds:
#    - minimum speed = 1 banana per hour
#    - maximum speed = largest pile
#
# 2. Pick a middle speed:
#    bananas_per_hour = (low + high) // 2
#
# 3. Compute how many hours this speed would take:
#
#    For each pile:
#      hours_for_pile = ceil(pile / bananas_per_hour)
#
#    Add those hours together to get total_hours.
#
# 4. Compare total_hours with max_hours:
#
#    - If total_hours <= max_hours:
#        this speed works
#        try a smaller speed (high = bananas_per_hour - 1)
#
#    - If total_hours > max_hours:
#        this speed is too slow
#        try a larger speed (low = bananas_per_hour + 1)
#
# 5. Repeat until:
#    - the search space becomes empty
#
# 6. Return low:
#    low ends up at the smallest valid eating speed
#
#
# Example
#
# piles = [3, 6, 7, 11]
# max_hours = 8
#
# We want the minimum speed that lets Koko finish in 8 hours or less.
#
# Possible speeds range from:
# 1 to 11
#
# Step 1:
# low = 1, high = 11
# bananas_per_hour = 6
#
# Hours needed:
# pile 3  -> ceil(3 / 6)  = 1
# pile 6  -> ceil(6 / 6)  = 1
# pile 7  -> ceil(7 / 6)  = 2
# pile 11 -> ceil(11 / 6) = 2
#
# total_hours = 6
#
# 6 <= 8, so speed 6 works
# Try smaller speed:
# high = 5
#
#
# Step 2:
# low = 1, high = 5
# bananas_per_hour = 3
#
# Hours needed:
# pile 3  -> 1
# pile 6  -> 2
# pile 7  -> 3
# pile 11 -> 4
#
# total_hours = 10
#
# 10 > 8, so speed 3 is too slow
# Try larger speed:
# low = 4
#
#
# Step 3:
# low = 4, high = 5
# bananas_per_hour = 4
#
# Hours needed:
# pile 3  -> 1
# pile 6  -> 2
# pile 7  -> 2
# pile 11 -> 3
#
# total_hours = 8
#
# 8 <= 8, so speed 4 works
# Try smaller speed:
# high = 3
#
#
# Now:
# low = 4, high = 3
#
# The loop stops because low > high.
#
# At this point:
# - high is the last speed that was too small
# - low is the first speed that works
#
# So the answer is:
# 4
#
#
# Key Idea
#
# We are not binary searching the piles themselves.
#
# We are binary searching the answer:
# "What is the minimum eating speed that works?"
#
# Each guessed speed gives a yes/no result:
# - works
# - does not work
#
# That creates a pattern like:
# false, false, false, true, true, true
#
# Binary search can find the first true value efficiently.
#
#
# Complexity
#
# Let:
# n = number of piles
# m = largest pile size
#
# Binary search checks speeds from 1 to m:
# O(log m) iterations
#
# In each iteration, we scan all piles:
# O(n)
#
# Total Time: O(n log m)
#
# Space Complexity: O(1)
#
#
# Limitation
#
# This approach works because larger eating speeds never make
# the total required hours go up.
#
# As speed increases, total_hours stays the same or decreases.
# That monotonic behavior is what makes binary search possible.

from math import ceil

def min_eating_speed(piles, max_hours):
    low = 1
    high = max(piles)

    while low <= high:
        bananas_per_hour = (low + high) // 2

        total_hours = 0

        for pile in piles:
            hours_for_pile = ceil(pile / bananas_per_hour)
            total_hours += hours_for_pile

        # This speed works, so try to find a smaller valid speed
        if total_hours <= max_hours:
            high = bananas_per_hour - 1

        # This speed is too slow, so we need to eat faster
        else:
            low = bananas_per_hour + 1

    # low ends at the smallest speed that works
    return low



piles = [3, 6, 7, 11]
max_hours = 8

min_speed = min_eating_speed(piles, max_hours)
print(min_speed)