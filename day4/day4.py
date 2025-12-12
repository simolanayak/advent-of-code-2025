import sys
import numpy as np
import os

def ingest_file(filepath):
    fp = open(filepath)
    return np.array(
        [list(line.strip()) for line in fp.readlines()]
    )

def get_indices_of_accessible_paper(paper_char, paper_array, max_paper, devnull=False):
    accessible_paper_count = 0
    accessible_paper_coords = []
    
    original_stdout = sys.stdout
    if devnull:
        f = open(os.devnull, 'w')
        sys.stdout = f
    
    for i in range(len(paper_array)):
        for j in range(len(paper_array[i])):
            #we only want to test paper if present
            if paper_array[i][j] != paper_char:
                continue
            print(f"Paper at: ({i},{j})")

            if i == 0:
                top_index = 0
                bottom_index = 2
            elif i == len(paper_array) - 1:
                top_index = len(paper_array) - 2
                bottom_index = len(paper_array)
            else:
                top_index = i - 1
                bottom_index = i + 2

            if j == 0:
                left_index = 0
                right_index = 2
            elif j == len(paper_array[i]) - 1:
                left_index = len(paper_array[i]) - 2
                right_index = len(paper_array[i])
            else:
                left_index = j - 1
                right_index = j + 2
            
            adjacents = paper_array[top_index: bottom_index, left_index: right_index]
            print(f"\tAdjacents: {adjacents}")
            #remember, we are only testing paper cells
            num_papers = (adjacents == paper_char).sum() - 1

            if num_papers < max_paper:
                print("Accessible!!\n\n")
                accessible_paper_count += 1
                accessible_paper_coords.append((i, j))
            else:
                print("\n\n")

    if devnull:
        sys.stdout = original_stdout

    return accessible_paper_count, accessible_paper_coords

def remove_paper(paper_array, paper_coords, paper_char, nonpaper_char):
    for x, y in paper_coords:
        if paper_array[x, y] != paper_char:
            print("QA ISSUE: PAPER NOT FOUND HERE! EXITING.")
            quit()
        else:
            paper_array[x, y] = nonpaper_char
    return paper_array

def main(filepath, part):
    paper_array = ingest_file(filepath)
    if part == "1":
        papercount, paperloc = get_indices_of_accessible_paper("@", paper_array, 4)
        print(papercount)
    elif part == "2":
        num_trips = 0
        total_paper_out = 0
        while True:
            print(f"Trip {num_trips + 1}:")
            paper_out, paperloc = get_indices_of_accessible_paper("@", paper_array, 4, devnull=True)
            print(f"\tPaper found at: {paperloc}")
            num_trips += 1
            paper_array = remove_paper(paper_array, paperloc, "@", ".")
            total_paper_out += paper_out
            if paper_out == 0:
                break
        print(f"Total trips: {num_trips}")
        print(f"Total paper removed: {total_paper_out}")
    else:
        print("no part 3, go tf to sleep.")

if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])