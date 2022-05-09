# Recursion
A recursive function is one that calls itself.    

Example: Fibinacci's #
```
f(0)= 0  
f(1)= 1 # base case  
f(n) = f(n-1) + f(n -2) # recursion
```

 Recursive functions must have a **base case** (a conditional situation in which a recursive function ends).  **Recursive cases** are cases in which the function calls itself.  
-  A function with no base case (an **infinite recursion**) will cause a stack overflow error (or RecursionError).  
- As the function runs the recursions, it must hold space (memory)  for each function's call.  Once it gets to the base case, it can use the base case for the first function call in the stack and work its way to the last call.   
- **Call stacks are LIFO**: last in, first out.

- Using a for loop can perform the same thing as a recursive function.

## Recursive function examples:
Adding the sum of all numbers:
```
def sum_natural_nums(num):
    if num == 1:
        return num
    return num + sum_natural_nums(n-1)
```
Finding number of bunny ears for a specific # of bunnies:
```
def bunny(count):
    if count == 0:
        return 0
    elif count == 1:
        return 2
    return 2 + bunny(count-1)
```
Or written better:
```
def bunny(count):
    if count == 0:
        return 0
    else:
        return 2 + bunny(count-1)
```
How does that work?
```
# count: 3 return 6  '2 + bunny(2)' evaluates to 2 + 4 == 6
# count: 2 return 4   '2 + bunny(1)'  evaluates to 2 + 2 == 4
# count: 1 return 2   '2 + bunny(0)'  evaluates to 2 + 0 == 2
```
Print a string backwards:
```
def reverse(text):
    if len(text) <=1:
        return text # base case
    return text[-1] + reverse(text[0:-1])
    
# text = 'hello'
# returns:
# 1st: text[-1] + rev(text[0:-1]) ==> 'o' + rev('hell')
# 2nd: text[-1] + rev(text[0:-1]) ==> 'l' + rev('hel')
# 3rd: text[-1] + rev(text[0:-1]) ==> 'l' + rev('he')
# 4th: text[-1] + rev(text[0:-1]) ==> 'e' + rev('h') 
# 5th: text                       ==> 'h'

# sooo.. 'o'+'l' + 'l' + 'e' + 'h'
```
More examples:
```
def search(array, query):
    '''
    input: array: unsorted list of ints;  query: int value to find
    output: True if query found in array, else False
    '''
    if len(array) == 0:
        return False
    elif array[-1] == query:
        return True
    else:
        return search(array[:-1], query)
```
palindrome:
```
def is_palindrome(text):
    '''
    input: string
    output: boolean indicating if palindrome (aka reversible)
    '''
    if text[0] != text[-1]:
        return False
    if len(text) <= 2:
        return True
    # slicing removes first and last letter of the string for next iteration
    return is_palindrome(text[1:-1])
```
