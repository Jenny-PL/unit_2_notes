# Create a hash table (using a dictionary) that maps a number in an array
#to True, to show that it is present

# new_dictionary = {key:value for(key:value) in old_dict (if conditional)}

# Create an empty list to hold all missing numbers

# For each number in the range between low and high, 
#check the value in the map:

# If the number exists as a key in the dictionary, then the number is present
# If the number does not exist as a key in the dictionary, then the number is missing
# Append it to our list that holds all missing numbers

def get_missing_numbers_in_range(array, num_low, num_high):
    num_dict = {num: True for num in array}
    missing_nums = []
    
    for num in range(num_low, num_high):
        if num in num_dict:
            num +=1
        else:
            missing_nums.append(num)
            num +=1
    return missing_nums
            

answer = get_missing_numbers_in_range([10, 12, 11, 15], 10, 15)
print(answer)

# Create a hash table that maps every pair's first item to its second item
# Create an empty list to hold all symmetric pairs
# Iterate over the pair list again to ensure we process pairs in order:
# Check the hash table if the symmetric pair exists:
# Take the current second item, and use it as a key in the hash table
# Look up the value of the current second item in the hash table, and 
# check whether its value is equal to the current key (current first item)
# If it's equal, then there's a symmetric pair!
# Append it to our list of symmetric pairs
# Remove the current pair from the hash table so that it can't 
# be matched by the symmetric pair when we reach it in the list.


def get_symmetric_pairs(list):
    '''
    input: list of pairs, with sublists that each have two items
    output: list of symetric pairs: a list with sublists of pairs; 
    A pair is only listed once; its symmetric pair is not also listed.
    '''
    # Create a hash table that maps every pair's first item to its second item
    dict_of_pairs = {couple[0] : couple[1] for couple in list}
    # dict_of_pairs = {}
    # for couple in list:
    #     dict_of_pairs[couple[0]]= couple[1]

    # Create an empty list to hold all symmetric pair
    symmetric_pairs  = []
    #Iterate over the pair list again to ensure we process pairs in order:
    # Check the hash table if the symmetric pair exists:
    for couple in list:
        if couple[0] in dict_of_pairs:
            if couple[1] in dict_of_pairs:
                new_key = couple[1]
                if dict_of_pairs[new_key] == couple[0]:
                    symmetric_pairs.append(couple)
                    del dict_of_pairs[couple[0]]
    return symmetric_pairs 

    # Take the current second item, and use it as a key in the hash table
    # Look up the value of the current second item in the hash table, and 
    # check whether its value is equal to the current key (current first item)
    # If it's equal, then there's a symmetric pair!
    # Append it to our list of symmetric pairs

answer = get_symmetric_pairs([[11, 20], [30, 40], [5, 10], [40, 30], [10, 5]])
print(answer) # expect [[30, 40], [5, 10]]

def get_intersection(list_1, list_2):
    dict = {list_1[i]: False for i in range(len(list_1))}
    dict = {list_2[i]: True for i in range(len(list_2)) if list_2[i] in dict}
    intersection_list = []
    for num in dict:
        if dict[num] == True:
            intersection_list.append(num)
    return intersection_list

result = get_intersection([50, 43, 25, 72],[25, 36, 43, 50, 80]
)
print(set(result)) # 25,43,50 in set

# alternate solutions:
def get_intersection(red, blue):
    frequency_hash = {}

    for list in [red, blue]:
        for item in list:
            if item in frequency_hash:
                frequency_hash[item] += 1
            else:
                frequency_hash[item] = 1

    intersections = []
    for item, quantity in frequency_hash.items():
        if quantity > 1:
            intersections.append(item)

    return intersections

def is_permutation(str_1, str_2):
    str_1_hash = {}
    for char in str_1:
        if char in str_1_hash:
            str_1_hash[char] += 1
        else: 
            str_1_hash[char] = 1
    # print(str_1_hash)
    str_2_hash = {}
    for char in str_2:
        if char in str_2_hash:
            str_2_hash[char] += 1
        else:
            str_2_hash[char] = 1
    # print(str_2_hash)
    if str_1_hash == str_2_hash:
        return True
    else:
        return False

# With helper function:
def populate_frequency_map(text):
    frequency_hash = {}
    for char in text:
        if char in frequency_hash:
            frequency_hash[char] += 1
        else:
            frequency_hash[char] = 1
    return frequency_hash


def is_permutation(red, blue):
    red_frequency_hash = populate_frequency_map(red)
    blue_frequency_hash = populate_frequency_map(blue)

    return red_frequency_hash == blue_frequency_hash

    