import sys
import numpy as np

def read_file(filepath):
    fp = open(filepath)
    line = fp.readline()

    numranges = []
    nums = []

    while line:
        line = line.strip()
        if '-' in line:
            numranges.append(
                tuple([int(i) for i in line.split(sep="-")])
            )
        elif line.isnumeric():
            nums.append(int(line))
        line = fp.readline()

    return numranges, nums

def sort_produce(ranges, ingredient_ids):
    #this is key
    ingredient_ids = sorted(ingredient_ids)

    good_ingredients = []
    bad_ingredients = []

    rg_index = 0
    while(len(ingredient_ids) > 0):
        curr_range = ranges[rg_index]
        l = curr_range[0]
        h = curr_range[1]
        print(f"Assessing {l} to {h}")
        
        while ingredient_ids[0] < l:
            bad_apple = ingredient_ids.pop(0)
            bad_ingredients.append(bad_apple)
            print(f"\tBad ingredient: {bad_apple}")
            if len(ingredient_ids) < 1:
                break
        while ingredient_ids[0] >= l and ingredient_ids[0] <= h:
            good_apple = ingredient_ids.pop(0)
            good_ingredients.append(good_apple)
            print(f"\tGood ingredient: {good_apple}")
            if len(ingredient_ids) < 1:
                break

        rg_index += 1
        #endcap problem
        if rg_index == len(ranges):
            while(len(ingredient_ids) > 0):
                print(f"Reached endcap, dumping the rest")
                bad_apple = ingredient_ids.pop(0)
                bad_ingredients.append(bad_apple)
                print(f"\tBad ingredient: {bad_apple}")
            break
    print(len(good_ingredients))

#JUST NO ALGO
def collapse_ranges_oom(ranges):
    allnums = np.array([range(r[0], r[1] + 1) for r in ranges])
    return allnums.unique(())

def collapse_ranges_v2(ranges):
    ranges = sorted(ranges, key=lambda x: x[0])
    collapsed_ranges = [ranges[0]]
    
    for i in range(1, len(ranges)):
        last = list(collapsed_ranges[-1])
        curr = list(ranges[i])
        
        if curr[0] <= last[1]:
            old_last = last
            last[1] = max(last[1], curr[1])
            print(f"Range collapsed: {old_last} to {last}")
            collapsed_ranges[-1] = tuple(last)
        else:
            collapsed_ranges.append(tuple(curr))
    print(f"Before: {len(ranges)}\nAfter: {len(collapsed_ranges)}")
    return collapsed_ranges

def total_fresh_ids(ranges):
    total_fresh = 0
    for r in ranges:
        upper = r[1]
        lower = r[0]
        total_fresh += (upper - lower) + 1
        print(f"{upper}\t-\t{lower} + 1\t=\t{upper - lower + 1} fresh")
    print(f"Total fresh: {total_fresh}")
    return total_fresh

def main(filepath):
    fresh_ranges, ingredient_ids = read_file(filepath)
    #collapsed_ranges = collapse_ranges(fresh_ranges) #this is helpful for part a
    collapsed_ranges = collapse_ranges_v2(fresh_ranges)
    #print(len(collapsed_ranges))
    sort_produce(collapsed_ranges, ingredient_ids) #part a
    total_fresh_ids(collapsed_ranges) #part b

if __name__ == "__main__":
    main(sys.argv[1])