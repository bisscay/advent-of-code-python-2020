#!/usr/bin/python
"""CustomCustoms.py
    Author: Bissallah Ekele - bAe
    Date: 01/09/2021
    Description: Find "yes" answers on customs declaration form.
"""

import re

def count_unique_answers(group_answer):
    """Count group's unique answers.
    
    Key argument:
    group_answer -- a group's answers
    
    Return:
    Each groups unique answer count as an int.
    """
    answer_set = set()

    for character in group_answer:
        answer_set.add(character)

    if "\n" in answer_set: # Consider new-line character
        return len(answer_set) - 1

    return len(answer_set)

def sum_group_answers(group_answers):
    """Sum each group's unique answers.
    
    Key argument:
    group_answers -- list of answers from each group
    
    Return:
    Each groups unique answer count summed as an int.
    """
    unique_group_count = 0
    for group_answer in group_answers:
        unique_group_count = unique_group_count + count_unique_answers(group_answer)
    
    return unique_group_count
    
################################### Part2 ###################################
def get_member_count(group_answer):
    """Derive member-count in a group.
    
    Key argument:
    group_answer -- answers from each group as a string
    
    Return:
    Number of members in a group as an int.
    """
    member_list = group_answer.split("\n")
    return len(member_list)

def get_answer_weight(group_answer):
    """Derive member-answer count in a group.
    
    Key argument:
    group_answer -- answers from each group as a string
    
    Return:
    Number of common member-answer in a group as a dict.
    """
    answer_weight_dict = {}

    for character in group_answer:
        if character != "\n":
            if character not in answer_weight_dict:
                answer_weight_dict[character] = 1
            else:
                answer_weight_dict[character] = answer_weight_dict[character] + 1
    
    return answer_weight_dict

def count_common_answers(group_answer):
    """Derive each group's common answers.
    
    Key argument:
    group_answers -- answers from a group as a string
    
    Return:
    Count of common answers in a group as an int.
    """
    # Pseudocode
    # Split at new-line
    # store count of split
    # -------------------
    # Avoid \n character
    # if character not in dict,
    # place character and weight (1) in dict
    # else 
    # get character-weight
    # replace weight with weight+1
    # -------------------------
    # walk through dict
    # if character has weight equal to length of split
    # increase count
    # return count

    common_count = 0

    member_count = get_member_count(group_answer)

    answer_weight_dict = get_answer_weight(group_answer)

    for character in answer_weight_dict:
        if answer_weight_dict[character] == member_count:
            common_count = common_count + 1

    return common_count

def sum_common_group_answers(group_answers):
    """Sum count of common answers in all groups.
    
    Key argument:
    group_answers -- list of answers from each group
    
    Return:
    Each groups common answer count summed as an int.
    """
    common_answer_count = 0
    for group_answer in group_answers:
        common_answer_count = common_answer_count + count_common_answers(group_answer)

    return common_answer_count

def main():
    test_input = "test_input.txt"
    puzzle_input = "puzzle_input.txt"

    file_name = puzzle_input #test_input

    with open(file_name) as f:
        regex = r"\n\s+"
        group_answers = re.split(regex, f.read())

    print("Day_6"
            + "\nPart_1: " 
            + str(sum_group_answers(group_answers)) 
            + "\nPart_2: "
            + str(sum_common_group_answers(group_answers)))

if __name__ == "__main__":
    main()