#!/usr/bin/python
"""ReportRepair.py
    Author: Bissallah Ekele - bAe
    Date: 24/08/2021
    Description: Geology navigation on a toboggan, avoiding trees.
"""
import math

def get_biome_stable_map(map_seed, right_step, down_step):
    """Derive the full map based on steps,
     adhering to arboreal genetics and biome stability.

    Key argumeny:
    map_seed - string to be multiplied
    right_step - right step(s) as an int
    down_step - down step(s) as as int

    Return:
    String representation of full map
    """
    # Pseudocode
    # split input at new-line
    # get length of input-list as y-salt (1-steps)
    # get length of first line in list as x-salt (3-steps)
    # generate x-ward geology (x-length = [y-length*3]+1):
    # for each line in puzzle-input,
    # add x-base-geology to array

    input_lines = map_seed.splitlines()
    y_size = len(input_lines)
    x_salt_size = len(input_lines[0])
    x_size = (y_size / down_step * right_step) + 1
    
    x_multiple = int(math.ceil(x_size/x_salt_size) + 1) # Plus one for padding
    
    for index in range(y_size):
        line = input_lines[index]
        input_lines[index] = line * x_multiple

    return input_lines

def count_encountered_trees(map_seed, right_step, down_step):
    """Derive number of trees encountered down the slope.
    
    Key argument:
    map_seed -- base geology as a string
    right_step -- right step(s) as an int 
    down_step -- down step(s) as an int
    
    Return:
    Tree count encountered down slope.
    """
    geology = get_biome_stable_map(map_seed, right_step, down_step)
    
    count = 0
    down_index = 0
    right_index = 0

    while down_index < len(geology):
        # Pseudocode
        # check if every nth(right_step) index is a hash
        # increase index-start by a multiple

        line = geology[down_index]

        if line[right_index] == "#":
            count = count + 1

        right_index = right_index + right_step
        down_index = down_index + down_step

    return count

def main():
    test_input = "test_input.txt"
    puzzle_input = "puzzle_input.txt"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        map_seed = f.read()

    # Tree count for each slope
    tree_count_1 = count_encountered_trees(map_seed, 1, 1)
    tree_count_2 = count_encountered_trees(map_seed, 3, 1)
    tree_count_3 = count_encountered_trees(map_seed, 5, 1)
    tree_count_4 = count_encountered_trees(map_seed, 7, 1)
    tree_count_5 = count_encountered_trees(map_seed, 1, 2)
    
    print("Day_1 Part_1: "
        + str(tree_count_2)
        + "\nPart_2: "
        + str(tree_count_1 * tree_count_2 * tree_count_3 * tree_count_4 * tree_count_5))

if __name__ == "__main__":
    main()