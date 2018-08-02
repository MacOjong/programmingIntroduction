# // --- Directions
# // Given a string, return a new string with the reversed
# // order of characters
# // --- Examples
# //   reverse('apple') === 'elppa'
# //   reverse('hello') === 'olleh'
# //   reverse('Greetings!') === '!sgniteerG'

# def reverse_string(string):
#     return string[::-1]


# Different approaches:

# def reverse_string(string):
 
#     reversed_string = ""
#     # counter at 0
#     count = 0
#     while count < len(string):

#         reversed_string = string[count] + reversed_string 
#         count += 1 # count = count + 1
#     return reversed_string

def reverse_string(string):

    # creating an empty string because we will be using it to add characters one at the time
    # from string backward
    reversed_s = ""
    for index in range(len(string)):
        # incremently concanetate string[index] into reversed_d
        # Thsis will be adding the the new value o the character in string
        # to the reversed_s(which was empty at the end) in a backward way
        # From righ to left.
        reversed_s = string[index] + reversed_s # => index is of type integer(int)

    return reversed_s

# Test  Zone
s = "Propinquity"
# print(reverse_string(string))
print(reverse_string(s))


# # A comment
# string = "apple"
# print(reverse_string(string))

# # str = "hello"
# print(reverse_string(str))

# # string = "Greetings!"
# print(reverse_string(string))