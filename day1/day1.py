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

        if direction == "L":
            currnum = (currnum - mag)%100
        elif direction == "R":
            currnum = (currnum + mag)%100
        print("Now at:" + str(currnum))

        if currnum == 0:
            numzeros += 1
            print("ZERO!!")

    print("Total zeros: " + str(numzeros))