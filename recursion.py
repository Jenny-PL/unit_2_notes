
# exponenent = 1 is base ase
def power(num, exponent):
    if exponent == 0:
        return 1

    return num * power(num, exponent - 1)

def digit_match(num1, num2):
    '''
    input: two non-negative integers (not necessarily same length)
    output: number of matches (same value at same location relative end)
    '''
    count = 0
    if len(str(num1)) == 0 or len(str(num2)) == 0:
        return count
    elif str(num1)[-1] == str(num2)[-1]:
        count += 1
    return count + digit_match(str(num1)[:-1], str(num2)[:-1])

digit_match(1072503891,62530841)

# Ada's solution, without converting to strings:
def digit_match(apples, oranges):
    # Base cases:
    # If both apples and oranges are 0 return 1
    if apples == 0 and oranges == 0:
        return 1
    # If one or both are 1-digit numbers
    elif apples < 10 or oranges < 10:
        if apples % 10 == oranges % 10:
            return 1
        
        return 0
    
    # Recursive Cases
    if apples % 10 == oranges % 10:
        return 1 + digit_match(apples // 10, oranges // 10)
        
    return digit_match(apples // 10, oranges // 10)