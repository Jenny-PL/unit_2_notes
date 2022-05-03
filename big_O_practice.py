def pairs_with_given_sum(numbers, target):
    if type(target) != int: # O(1) time
        return TypeError("Please give an integer value for target sum ") #O(1)
        
    for num in numbers:  #O(n)
        if type(num) != int: #O(1)
            return TypeError("Please give a list of integers") # O(1)

    list_to_alter = numbers.copy() #O(n)
    num_of_pairs = 0 #O(1)

    for num in numbers: #O(n)
        first_num = num #O(1)
        list_to_alter.remove(first_num) #O(n)
        for item in list_to_alter: #O(n)
            sum = first_num + item #O(1)
            if sum == target: #O(1)
                num_of_pairs += 1  #O(1)
    return num_of_pairs  #O(1)

# Overall O(n)**2