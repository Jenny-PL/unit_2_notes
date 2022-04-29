'''
NO FOR OR WHILE LOOPS ALLOWED
NO COMPREHENSIONS ALLOWED

You can assume valid, non-empty input

Useful functions
- min
- max
- sorted
- map
- filter

'''


# Helper function for giving more informative test failure messages
# Feel free to ignore!
def pretty_assert(actual, expected):
    assert actual == expected, f"\n  Expected: {expected}\n  Actual: {actual}"


# Wave 1
# Write a function that takes in a list of words and returns the shortest one. (assume no ties)


def shortest_word(words):
    return min(words, key=len)


pretty_assert(shortest_word(["from", "swerve", "of", "shore"]), "of")
pretty_assert(shortest_word(["bay"]), "bay")
print("Wave 1 passed!")

# Wave 2
# Write a function that takes in a list of numbers and returns a new list containing only the ones that are even, in the same order.
# Hint: remember to convert back to a list!


def even_nums(nums):
  return list(filter(lambda n: n%2==0, nums))

pretty_assert(even_nums([1, 2, 8, 3, 4]), [2, 8, 4])
pretty_assert(even_nums([2, 2, 8]), [2, 2, 8])
print("Wave 2 passed!")

# Wave 3
# Write a function that takes in a list of numbers and returns a new list containing the squares of those numbers (the numbers raised to the second power)
# Hint: remember to convert back to a list!


def squares(nums):
    return list(map(lambda n: n**2, nums))


pretty_assert(squares([1, 2, 8, 3, 4]), [1, 4, 64, 9, 16])
pretty_assert(squares([2, 2, 8]), [4, 4, 64])
print("Wave 3 passed!")

# Wave 4
# Write a function that accepts a word, a function, and the name of that function. It should return a string that reports: "The result of applying FUNCTION_NAME to WORD is RESULT"


def report(word, function, function_name):
    # result = function(word)
    return f"The result of applying {function_name} to {word} is {function(word)}"

pretty_assert(report("hello", len, "len"),
              'The result of applying len to hello is 5')
pretty_assert(report("people", lambda w: w.upper(), "upper"),
              'The result of applying upper to people is PEOPLE')
print("Wave 4 passed!")

# Wave 5
# Write a function that takes a list of passwords and returns a list of only those passwords that have at least one non-alphabetic character in them. The returned list should be sorted by in order of increasing length.


def sorted_valid_passwords(passwords):

    return sorted(list(filter(lambda x: x.isalpha() == False, passwords)), key=len)
    
    # for letter in passwords:
    #     if letter.isalpha() == False

pretty_assert(sorted_valid_passwords(
    ["password", "p@ssword", "z00p", "hello", "password123"]), ['z00p', 'p@ssword', 'password123'])
    
print("Wave 5 passed!")


# sorted_valid_passwords(
#         ["password", "p@ssword", "z00p", "hello"
#          "password123"]), ['z00p', 'p@ssword', 'hellopassword123'])