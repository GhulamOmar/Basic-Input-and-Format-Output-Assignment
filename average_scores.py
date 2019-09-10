"""
Program: average_scores.py
Author: Ghulam Omar
Last date modified: 09/10/19
This program allows the user to enter first name, last name, age , and 3 scores.
and print the average of 3 scores.
"""


def average(score_1, score_2, score_3, total_average):  # Function definition.
    return (score_1 + score_2 + score_3) / total_average  # return statement.


if __name__ == '__main__':
    # user inputs
    name = input("Please enter your first name")
    last_name = input("Please enter your last name")
    age = int(input("Please enter your age"))
    score_1 = int(input(" Enter the score"))
    score_2 = int(input(" Enter the score"))
    score_3 = int(input(" Enter the score"))
    total_average = float(3)  # variable declaration.
    total_score = float(score_1 + score_2 + score_3)/total_average # average calculation.

    print(last_name,",",name,"age:", age,"average score:",total_score) # output the result.
