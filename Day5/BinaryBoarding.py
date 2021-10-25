#!/usr/bin/python3
"""BinaryBoarding.py
    Author: Bissallah Ekele - bAe
    Date: 30/08/2021
    Description: Scan boarding passes to find seat number by elimination.
"""
# Note: For python2 include: from sets import Set

def perform_elimination(boarding_pass, seed, lower_index, upper_index):
    """Perform elimination on boarding pass indices.
    
    Key argument:
    boarding_pass -- boarding pass as a binary space partition
    seed -- number of cells elimination is performed on
    lower_index -- considered boarding pass lower index, inclusive
    upper_index -- considered boarding pass upper index, inclusive
    
    Return:
    Index left after elimination.
    """
    # Algorithm
    # B or R increases the start point by half of the seed, cumulatively
    # F or L decreases the end point by half of the seed, cumulatively
    
    start = 0
    end = seed - 1 # Zero-based index
    for index in range(lower_index, upper_index+1):
        seed = seed / 2
        letter = boarding_pass[index]
        if letter in {"F", "L"}: # Note in python2: Set(["F","L"])
            end = end - seed
        else:
            start = start + seed

    if start == end:
        return start

    return -1 # Else throw an invalid boarding pass exception

def get_seat_ID(boarding_pass):
    """Get seat ID from boarding pass.
    
    Key argument:
    boarding_pass -- boadring pass as binary space partitions
    
    Return:
    Seat ID from boarding pass as int.
    """
    row = perform_elimination(boarding_pass, 128, 0, 6)
    column = perform_elimination(boarding_pass, 8, 7, 9)

    return int(row * 8 + column)

def get_all_seat_ID(boarding_passes):
    """Get all seat IDs from boarding passes.
    
    Key argument:
    boarding_passes -- list of boadring passes as binary space partitions
    
    Return:
    List of seat IDs from boarding passes.
    """
    seat_ID_list = []

    for boarding_pass in boarding_passes:
        seat_ID_list.append(get_seat_ID(boarding_pass))
    
    return seat_ID_list 

def get_highest_ID(boarding_passes):
    """Get highest seat ID from list of boarding passes.
    
    Key argument:
    boarding_passes -- list of boadring passes as binary space partitions
    
    Return:
    Highest seat ID from boarding passes.
    """
    return max(get_all_seat_ID(boarding_passes))

def get_my_seat_ID(boarding_passes):
    # Algorithm
    # Exclude front and back row
    # back
    # 127 * 8 + 0 = 1016
    # 127  * 8 + 7 = 1023
    # front
    # 0 * 8 + 0 = 0
    # 0 * 8 + 7 = 7
    # span
    # 8 - 1015
    # Get highest and lowest ID in seat_ID_list
    # span: lowest - highest
    # Find missing id in seat_ID_list
    
    seat_ID_list = get_all_seat_ID(boarding_passes)

    my_seat = -1

    for query in range(54, 930):
        if query not in seat_ID_list:
            my_seat = query
    
    return my_seat # TODO: Throw seat not found exception
  
def main():
    test_input = "test_input.txt"
    puzzle_input = "puzzle_input.txt"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        binary_partitions = f.read().splitlines()
        binary_partitions = set(binary_partitions)

    print("Day_5"
            + "\nPart_1: " 
            + str(get_highest_ID(binary_partitions)) 
            + "\nPart_2: "
            + str(get_my_seat_ID(binary_partitions)))

if __name__ == "__main__":
    main()