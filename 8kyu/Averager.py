def get_average(marks):
    sum, count = 0, 0
    for mark in marks:
        sum += mark
        count += 1
    return sum // count

# Round down the average in a list of grades.
