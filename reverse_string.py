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
    reversed_result = ""
    for char in string:
        # incremently concanetate char into reversed_result
        reversed_result = char + reversed_result 

        # print(char)
    return reversed_result 
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