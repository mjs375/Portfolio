from calendar import monthrange
def last_day(year, month):
    return monthrange(year, month)[1]

"""
monthrange(y, m):
  Returns weekday of first day of the month and number of days in month, for the specified year and month.
Task:
  Return the length of the given month in the given year.
  Your code must be shorter than 90 characters.
"""
