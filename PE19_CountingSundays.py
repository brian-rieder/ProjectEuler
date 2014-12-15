__author__ = 'Brian Rieder'

# Problem 19: Counting Sundays

# You are given the following information, but you may prefer to do some research for yourself.
#
# -- 1 Jan 1900 was a Monday.
# -- Thirty days has September,
#    April, June and November.
#    All the rest have thirty-one,
#    Saving February alone,
#    Which has twenty-eight, rain or shine.
#    And on leap years, twenty-nine.
# -- A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
#
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

# Answer:

# Note the the Reader:
# This is a mathematical approach using the Gaussian Day of the Week function:
# w = (d + floor(2.6*m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) mod 7
# Y is the year minus 1 for January or February, and the year for  the rest of the year
# y is the last 2 digits of Y
# c is the first 2 digits of Y
# d is the day of the month (1 to 31)
# m is the shifted month (March=1,...February=12)
# w is the day of week (0=Sunday,..6=Saturday)
# See: http://en.wikipedia.org/wiki/Determination_of_the_day_of_the_week

from math import floor

monday_cnt = 0


def find_day_of_week(d, m, big_y):
    """
    Find the day of the week of a given date
    :param d: Day of the month (1 to 31)
    :param m: Shifted month (March=1,...February=12)
    :param big_y: Year minus 1 for January or February, and the year for the rest of the year
    :return: w: Day of the week (0=Sunday,..6=Saturday)
    """
    if m == 11 or m == 12:
        big_y -= 1
    y = big_y % 100
    c = floor(big_y / 100)
    w = (d + floor(2.6*m - 0.2) + y + floor(y/4) + floor(c/4) - 2*c) % 7
    return w

# Always want the first day of the month
day = 1

sunday_count = 0
for year in range(1901, 2001):
    for month in range(1, 13):
        weekday = find_day_of_week(day, month, year)
        if weekday == 0:
            sunday_count += 1

print sunday_count