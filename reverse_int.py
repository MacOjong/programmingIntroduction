# // --- Directions
# // Given an integer, return an integer that is the reverse
# // ordering of numbers.
# // --- Examples
# //   reverseInt(15) === 51
# //   reverseInt(981) === 189
# //   reverseInt(500) === 5
# //   reverseInt(-15) === -51
# //   reverseInt(-90) === -09


def reverse_int(x): 
    
    # Check if x is positive or negative
    if x > 0:
        # if positive go with int(str(x)[::-1])
        return int(str(x)[::-1])
        
    # else get the absolute value of x
    return int(str(x * (-1))[::-1]) * - 1

n = 456     
# print(str(x))[::-1]

# print (reverse_int(n))
reverse_int(n)