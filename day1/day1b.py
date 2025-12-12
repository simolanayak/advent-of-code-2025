import sys 
if __name__ == "__main__":
    file_path = sys.argv[1]
    if len(sys.argv) < 3:
        startnum = 50
    else:
        startnum = sys.argv[2]

    deltas = open(file_path).readlines()
    numzeros = 0
    currnum = startnum

    for d in deltas:
        direction = d[0]
        mag = int(d[1:])

        print(d.strip())
        if direction == "L":
            for i in range(mag):
                currnum -=1
                currnum = currnum % 100
                if currnum == 0:
                    numzeros += 1
        elif direction == "R":
            for i in range(mag):
                currnum +=1
                currnum = currnum % 100
                if currnum == 0:
                    numzeros += 1
        print(f"Current: {currnum}")
        print(f"Total zeros: {numzeros}")