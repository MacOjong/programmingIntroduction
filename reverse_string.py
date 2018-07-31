# // --- Directions
# // Given a string, return a new string with the reversed
# // order of characters
# // --- Examples
# //   reverse('apple') === 'elppa'
# //   reverse('hello') === 'olleh'
# //   reverse('Greetings!') === '!sgniteerG'


def reverse_string(string):

    # Empty string
    result = ""
    # initialiazing a counter for the while loop
    count = 0

    while count < len(string):
        result += string[count]
        count += 1
    return string



# Test  Zone
str_ = "Welocme to this tutorial"
print(reverse_string(str_))
