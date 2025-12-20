import numpy as np
import re
import sys

def ingest_file(filepath):
    lines = open(filepath).readlines()
    operators = re.sub(r"\s+", "", lines[-1])

    digits = np.array([list(line.replace("\n", "")) for line in lines[:-1]]).T
    digits = np.array(["".join(arr).strip() for arr in digits])
    blank_indices = np.where(digits=='')[0]
    
    operand_arrays = np.split(digits, blank_indices)
    #print(operand_arrays)
    return operand_arrays, operators

def iterate_calculations_loop(operands, operators):
    results = []
    for i in range(len(operands)):
        results.append(calculate_row(operands[i], operators[i]))
    return results

def calculate_row(operands, operator):
    operands = np.delete(operands, np.where(operands == "")).astype('i')
    
    if operator in ["-", "+"]:
        startval = 0
    else:
        startval = 1

    total = startval
    if operator == "+":
        for num in operands:
            total += num
    elif operator == "-":
        for num in operands:
            total -= num
    elif operator == "*":
        for num in operands:
            total *= num
    elif operator == "/":
        for num in operands:
            total = total/num
    else:
        print(f"Invalid operator {operator}. Exit.")
        quit(code=1)
    print(total)
    return total

if __name__ == "__main__":
    digits, ops = ingest_file(sys.argv[1])
    results = iterate_calculations_loop(digits, ops)
    print(f"Sum: {np.sum(results)}")