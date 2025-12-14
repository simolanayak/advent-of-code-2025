import numpy as np
import re
import sys

def ingest_file(filepath):
    lines = open(filepath).readlines()
    lines = [re.split("\s+", line.strip()) for line in lines]

    digits = [[int(i) for i in line] for line in lines[:-1]]

    operators = lines[-1]
    digits = np.array(digits).transpose()
    print(f"Check len(digits) == len(operators): {len(digits) == len(operators)}")
    if not (len(digits) == len(operators)):
        print("Incompatible lengths. Quitting")
        quit()
    return digits, operators

def iterate_calculations_loop(operands, operators):
    results = []
    for i in range(len(operands)):
        results.append(calculate_row(operands[i], operators[i]))
    return results

def iterate_calculations_axisapply(operands, operators):
    operators = np.array(operators).reshape(-1, 1)
    #digestible by function
    all_array = np.concatenate((operands, operators), axis=1)
    result = np.apply_along_axis(calculate_row, 1, all_array)
    return result

def calculate_row(row):
    operator = row[-1]
    row = row[:-1]

    if operator in ["-", "+"]:
        startval = 0
    else:
        startval = 1

    total = startval
    if operator == "+":
        for num in row:
            total += int(num)
    elif operator == "-":
        for num in row:
            total -= int(num)
    elif operator == "*":
        for num in row:
            total *= int(num)
    elif operator == "/":
        for num in row:
            total = total/num
    else:
        print(f"Invalid operator {operator}. Exit.")
        quit(code=1)
    print(total)
    return total

if __name__ == "__main__":
    digits, ops = ingest_file(sys.argv[1])
    results = iterate_calculations_axisapply(digits, ops)
    print(f"Sum: {np.sum(results)}")