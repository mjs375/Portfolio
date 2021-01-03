# Clean up later...

def sum_arrays(array1,array2):
    print(array1, array2)
    if array1 == [] and array2 == []:
        return []
    
    sum1 = str()
    for num in array1:
        num = str(num)
        if num.lstrip('-').isdigit():
            sum1 += str(num)
    sum2 = str()
    for num in array2:
        num = str(num)
        if num.lstrip('-').isdigit():
            sum2 += str(num)
    
    
    if sum1 == str():
        ans = sum2
    elif sum2 == str():
        ans = sum1
    else:
        ans = int(sum1) + int(sum2)
        
        
    ans = str(ans)
    solution = []
    print("ANS::",ans)
    negative = False
    leadingzero = True
    
    if ans == "0":
        return [0]
    
    for char in ans:
        print(char)
        if char == "-":
            negative = True
        elif char == "0" and leadingzero == True:
            pass
        else:
            solution.append(int(char))
            leadingzero = False
    print(solution)
    if negative == True:
        solution[0] = solution[0] * -1
    return solution


"""
Your task is to create a function called sum_arrays(), which takes two arrays consisting of integers, and returns the sum of those two arrays.

The twist is that (for example) [3,2,9] does not equal 3 + 2 + 9, it would equal '3' + '2' + '9' converted to an integer for this kata, meaning it would equal 329. The output should be an array of the the sum in a similar fashion to the input (for example, if the sum is 341, you would return [3,4,1]). Examples are given below of what two arrays should return.

[3,2,9],[1,2] --> [3,4,1]
[4,7,3],[1,2,3] --> [5,9,6]
[1],[5,7,6] --> [5,7,7]
If both arrays are empty, return an empty array.

In some cases, there will be an array containing a negative number as the first index in the array. In this case treat the whole number as a negative number. See below:

[3,2,6,6],[-7,2,2,8] --> [-3,9,6,2] # 3266 + (-7228) = -3962
"""
