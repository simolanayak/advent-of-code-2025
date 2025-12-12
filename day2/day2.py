import sys
import re

def ingest_inputs(filepath):
    array_in = open(filepath).readline().strip().split(sep=",")
    num_ranges = []
    for item in array_in:
        num1, num2 = item.split("-")
        #normalize to ensure smaller number first
        if int(num1) > int(num2):
            num_ranges.append((num2, num1))
        else:
            num_ranges.append((num1, num2))
    return num_ranges

def test_repeat_v1(lower, upper):
    repeat_array = []
    for i in range(int(lower), int(upper) + 1):
        if re.fullmatch(r"(\d+)\1", str(i)):
            repeat_array.append(i)
    return repeat_array

def test_repeat_v2(lower, upper):
    repeat_array = []
    for i in range(int(lower), int(upper) + 1):
        if re.fullmatch(r"(\d+)\1+", str(i)):
            repeat_array.append(i)
    return repeat_array

if __name__ == "__main__":
    numranges = ingest_inputs(sys.argv[1])
    if "anyrepeat" in sys.argv:
        repeat_multiple = True
    else:
        repeat_multiple = False

    total_invalid_id = 0
    for nr in numranges:
        print(nr[0] + ", " + nr[1])
        if not repeat_multiple:
            repeat_array = test_repeat_v1(nr[0], nr[1])
        else:
            repeat_array = test_repeat_v2(nr[0], nr[1])

        print("Repeat Array: " + str(repeat_array))
        total_invalid_id += sum(repeat_array)
        print("Total Invalid IDs: " + str(total_invalid_id))