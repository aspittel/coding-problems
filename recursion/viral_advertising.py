"""
See how many people receive an advertisement after a specified number of days.

From https://www.hackerrank.com/challenges/strange-advertising
"""
def viral_advertising_calculator(days, curr_people=5, total_people=0):
    if days <= 0: return total_people
    curr_people = floor(curr_people/2)
    return viral_advertising_calculator(days-1, curr_people*3, curr_people + total_people)
