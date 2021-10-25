#!/usr/bin/python
"""ReportRepair.py
    Author: Bissallah Ekele - bAe
    Date: 22/08/2021
    Description: Resolve corrupt password database.
"""

def analyze_input(input_line):
    """Make sense of each line from puzzle input

        Keyword argument:
        input_line -- policy & password string

        Return:
        list of policy bounds on a character and considered passowrd
    """
    entry_list = input_line.split(" ")
    character = entry_list[1][:-1]
    password = entry_list[2]
    limit = entry_list[0].split("-")
    lower_limit = limit[0]
    upper_limit = limit[1]
    
    return [lower_limit, upper_limit, character, password]

def count_valid_passwords(policy_password_list):
    """Number of valid passwords based on a corporate policy

        Keyword argument:
        policy_password_list -- list of policy & passwords as strings

        Return:
        Count of valid passwords
    """
    count = 0
    for entry in policy_password_list:
        policy_password = analyze_input(entry)
        lower_limit = int(policy_password[0])
        upper_limit = int(policy_password[1])
        character = policy_password[2]
        password = policy_password[3]
        
        character_count = password.count(character)

        if character_count >= lower_limit and character_count <= upper_limit:
            count = count + 1
    
    return count

def get_part_2(policy_password_list):
    """Valid passwords that comply to updated policy.
        Exactly on of either position must contain given letter.

        Key argument:
        policy_password_list -- list of policy & passwords as strings

        Return:
        Count of valid passwords
    """
    count = 0
    for entry in policy_password_list:
        password_policy = analyze_input(entry)
        position_1 = int(password_policy[0]) - 1
        position_2 = int(password_policy[1]) - 1
        character = password_policy[2]
        password = password_policy[3]

        password_size = len(password)
        
        # if position_2 < password_size:
        #     if position_1 >= password_size and password[position_2] == character:
        #         count = count + 1

        # if position_1 < password_size:
        #     if position_2 >= password_size and password[position_1] == character:
        #         count = count +1
        
        if position_1 < password_size and position_2 < password_size:
            if ((password[position_1] == character and password[position_2] != character)
                or (password[position_2] == character and password[position_1] != character)):
                count = count + 1

    return count

def main():
    test_input = "test_input.txt"
    puzzle_input = "puzzle_input.txt"

    file_name = puzzle_input #test_input

    policy_password_list = None # Not necessary
    with open(file_name) as f:
        policy_password_list = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(count_valid_passwords(policy_password_list)) 
        + "\nPart_2: "
        + str(get_part_2(policy_password_list)))

if __name__ == "__main__":
    main()