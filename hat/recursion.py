def sum_array(array):

    '''Return sum of all items in array'''

    if array == 0:
        return 0
    else:
        return array[0] + sum_array(array[1:])

def fibonacci(n):

    '''Return nth term in fibonacci sequence'''

    if n <= 1:
        return n

    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):

    '''Return n!'''

    if n == 0:
        return n

    else:
        return n * factorial(n)

def reverse(word):

    '''Return word in reverse'''
    if word ==1 :
        return word

    rev= []
    count=0

    for x in range(0, len(word)):
        rev.append(word[len(word)-1-count])
        count +=1
    return ''.join(rev)
