from itertools import combinations_with_replacement

def find_optimized_set(target, units):
    best_set = None
    min_units = float('inf')

    for combo in combinations_with_replacement(units, 6):
        if sum(combo) == target:
            num_units = len(combo)
            if num_units < min_units:
                min_units = num_units
                best_set = combo

    return best_set, min_units


target_value = 20
available_units = [1, 2, 5, 10, 20, 50]

optimized_set, num_units = find_optimized_set(target_value, available_units)

if optimized_set:
    print("Optimized set:", optimized_set)
    print("Number of units:", num_units)
    print("Average units:", sum(optimized_set) / num_units)
else:
    print("No combination found for the target value.")
