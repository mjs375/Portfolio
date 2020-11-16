def adjacent_element_product(array):
    products = []
    for i in range(len(array)):
        try:
            products.append(array[i]*array[i+1])
        except:
            pass
    return max(products)
    
    
 """
 Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
 """
