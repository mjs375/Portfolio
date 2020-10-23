def life_path_number(birthdate): #birthdate is a string
    birthdate = sum([int(num) for num in str(birthdate) if num != "-"])
    if birthdate >= 10:
        birthdate = life_path_number(birthdate)  #RECURSION!
    return birthdate


"""
A person's Life Path Number is calculated by adding each individual number in that person's date of birth, untill it is reduced to a single digit number.
For example, Albert Einstein's birthday is March 14, 1879. The calculation of his Life Path Number would look like this:
    year: 1 + 8 + 7 + 9 = 25; 2 + 5 = 7
    month: 0 + 3 = 3
    day: 1 + 4 = 5
    final result: 7 + 3 + 5 = 15; 1 + 5 = 6
"""
