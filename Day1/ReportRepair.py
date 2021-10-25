#!/usr/bin/python
"""ReportRepair.py
    Author: Bissallah Ekele - bAe
    Date: 20/08/2021
    Description: Fixing my expense report
"""

def get_part_1(expenses):
    """Product of two enteries that sum up to 2020

        Keyword argument:
        expenses -- list of expenses as strings

        Return:
        Product of two integers that sum to 2020
    """
    for expense in expenses:
        expense_pair = 2020 - int(expense)
        if str(expense_pair) in expenses:
            return int(expense) * int(expense_pair)

def get_part_2(expenses):
    """Product of three enteries that sum up to 2020

        Keyword argument:
        expenses -- list of expenses as strings

        Return:
        Product of three integers that sum to 2020
    """
    expenses_size = len(expenses)
    for index in range(expenses_size):
        # Pseudocode:
        # Pick first
        # Find remainder
        # See if any two things sum up to remainder
        first_expense = int(expenses[index])
        remainder = 2020 - first_expense
        for index_plus in range(index+1, expenses_size):
            second_expense = int(expenses[index_plus])
            third_expense = remainder - second_expense
            if str(third_expense) in expenses:
                return first_expense * second_expense * third_expense


def main():
    test_file = "test_input.txt"
    puzzle_file = "puzzle_input.txt"

    file_name = puzzle_file

    with open(file_name) as f:
        expenses = f.read().splitlines()

    print("Day_1 Part_1: " 
        + str(get_part_1(expenses)) 
        + "\nPart_2: "
        + str(get_part_2(expenses)))

if __name__ == "__main__":
    main()