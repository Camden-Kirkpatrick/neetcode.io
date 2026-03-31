from math import ceil

def min_eating_speed(piles, max_hours) -> int:
    low = 1
    high = max(piles)

    while low <= high:
        mid = (low + high) // 2

        total_hours = 0
        for pile in piles:
            hours = ceil(pile / mid)
            total_hours += hours
        
        if total_hours <= max_hours:
            high = mid - 1
        else:
            low = mid + 1

    return low