#!/usr/bin/python
"""ReportRepair.py
    Author: Bissallah Ekele - bAe
    Date: 27/08/2021
    Description: Find valid passports and slip in North Pole Credentials. *wink
"""
import re

"""
    ############## PART 2 - METHODS - START ##################################
"""
def is_yr_valid(passport, year_type, lower_bound, upper_bound):
    """Check year validity.
    
    Key argument:
    passport -- passport string to be considered
    year_type -- byr, iyr or eyr enum
    lower_bound -- year lower bound
    upper_bound -- year upper bound
    
    Return:
    True if year is valid, else False.
    """
    if year_type in passport:
        regex = "".join([year_type, r":\d+"])
        match_object = re.search(regex, passport)
        if match_object != None:
            key_value_pair = match_object.group()
        else:
            return False

        value = int(key_value_pair[4:])

        if value >= lower_bound and value <= upper_bound:
            return True

    return False

def is_byr_valid(passport):
    """Check birth-year validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if birth-year is valid, else False.
    """
    return is_yr_valid(passport, "byr", 1920, 2002)

def is_iyr_valid(passport):
    """Check issue-year validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if issue-year is valid, else False.
    """
    return is_yr_valid(passport, "iyr", 2010, 2020)

def is_eyr_valid(passport):
    """Check expiration-year validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if expiration-year is valid, else False.
    """
    return is_yr_valid(passport, "eyr", 2020, 2030)

def is_hgt_valid(passport):
    """Check height validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if height is valid, else False.
    """
    if "hgt" in passport:
        regex = r"hgt:\d+(cm|in)"
        match_object = re.search(regex, passport)
        if match_object != None:
            key_value_pair = match_object.group()
        else:
            return False

        value = int(key_value_pair[4:-2])
        unit = key_value_pair[-2:]
        
        if unit == "cm" and value >= 150 and value <= 193:
            return True
        
        if unit == "in" and value >= 59 and value <= 76:
            return True
    
    return False

def is_hcl_valid(passport):
    """Check hair color validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if hair color is valid, else False.
    """
    value = None
    if "hcl" in passport:
        regex = r"#[\da-f]{6}"
        value = re.search(regex, passport) # Match object returns None if regex is absent

    return value != None

def is_ecl_valid(passport):
    """Check eye color validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if eye color is valid, else False.
    """
    eye_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

    for color in eye_colors:
        if color in passport:
            return True
    
    return False

def is_pid_valid(passport):
    """Check passport ID validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if passport ID is valid, else False.
    """
    if "pid" in passport:
        regex = r"pid:0*\d+"
        match_object = re.search(regex, passport)
        if match_object != None:
            key_value_pair = match_object.group()
        else:
            return False

        value = key_value_pair[4:]
        if len(value) == 9:
            return True

    return False

def is_valid(passport):
    """Check passport validity.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if passport is valid, else False.
    """
    return (is_byr_valid(passport) 
        and is_iyr_valid(passport)
        and is_eyr_valid(passport)
        and is_hgt_valid(passport)
        and is_hcl_valid(passport)
        and is_ecl_valid(passport)
        and is_pid_valid(passport))
        
def count_valid_passports(passports):
    """Get count of valid passports. - Day4 Part2.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    Count of valid passports as an int.
    """
    count = 0
    for passport in passports:
        if is_valid(passport):
            count = count + 1
    
    return count    
"""
    ############## PART 2 - METHODS - END ##################################
"""

"""
    ############## PART 1 - METHODS - START ##################################
"""
def is_present(passport):
    """Check passport validity (weak check).
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    True if passport is valid, else False.
    """
    valid_fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]

    for field in valid_fields:
        if field not in passport:
            return False
    
    return True

def get_part_1(passports):
    """Get count of valid passports. - Day4 Part1.
    
    Key argument:
    passport -- passport string to be considered
    
    Return:
    Count of valid passports as an int.
    """
    count = 0
    for passport in passports:
        if is_present(passport):
            count = count + 1
    
    return count 
"""
    ############## PART 1 - METHODS - END ##################################
"""

def main():
    test_input = r"inputs/test_input.txt"
    test_invalid_input = r"inputs/test_invalid_input.txt"
    test_valid_input = r"inputs/test_valid_input.txt"
    puzzle_input = r"inputs/puzzle_input.txt"

    file_name = puzzle_input

    with open(file_name) as f:
        regex = r"\n\s+"
        passports = re.split(regex, f.read())
    
    print("Day_1 Part_1: " 
        + str(get_part_1(passports)) 
        + "\nPart_2: "
        + str(count_valid_passports(passports)))

if __name__ == "__main__":
    main()