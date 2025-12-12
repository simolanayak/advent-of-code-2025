import sys
import numpy as np

def ingest_input(file):
    digit_arr = []
    fp = open(file)
    line = fp.readline().strip()
    while line:
        digit_arr.append(list(line))
        line = fp.readline().strip()
    return digit_arr

def get_joltage_a(line):
    max_joltage = int(line[0] + line[len(line) - 1])
    for i in range(len(line)):
        for j in range(len(line) - 1, i, -1):
            joltage = int(line[i] + line[j])
            if joltage > max_joltage:
                print(f"\tCurrent Joltage: {joltage}")
                max_joltage = joltage
    print(f"Max Joltage: {max_joltage}")
    return max_joltage

def get_joltage_b(line, num_digits):
    max_joltage_subset = []
    startdex = 0
    print(f"Line: {''.join(line)}\tLength: {len(line)}")
    line = [int(i) for i in line]
    for i in range(num_digits, 0, -1):
        subset = line[startdex : len(line) -i + 1]
        print(subset)
        print(f"Looking at range {startdex}:{len(line)-i}")
        maxval = max(subset)
        first_occurrence = subset.index(maxval)
        print(f"\tMax value: {maxval}\tAt:{startdex + first_occurrence}")
        max_joltage_subset.append(maxval)
        startdex += first_occurrence + 1
        print(f"\tHarvested: {max_joltage_subset}")
    max_joltage_subset = [str(i) for i in max_joltage_subset]
    max_joltage = int("".join(max_joltage_subset))
    print(f"Max Joltage: {max_joltage}\n\n")
    return max_joltage

def main(input_path):
    input_arr = ingest_input(input_path)
    joltages = []

    total_j = 0
    for line in input_arr:
        total_j += get_joltage_b(line, 12)
    print(f"Total Joltage: {total_j}")

if __name__ == "__main__":
    main(sys.argv[1])