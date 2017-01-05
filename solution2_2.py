from itertools import permutations
from operator import mul
from functools import reduce

'''
Power-Hungry 
Find largest product in subarray.

'''

def answer(xs):

    products = []
    reduced_products_list = []

    if any([i == 0 for i in xs]) and all([i <= 0 for i in xs]):
        '''
        If xs contains a zero and every element is less than zerosub
        '''
        reduced_products_list.append(0)

    if all(i == 0 for i in xs):  # if xs consists entirely of zeros

        reduced_products_list.append(0)

    pos_nums = [num for num in xs if num > 0]  # list of positive integers
    neg_nums = [num for num in xs if num < 0]

    if len(pos_nums) != 0:
        '''
        If there are any integers in pos_num list, find their product
        and add to higher list
        '''
        pos_product = reduce(mul, pos_nums)
        reduced_products_list.append(pos_product)

    elif len(neg_nums) == 1:

        reduced_products_list.append(neg_nums[0])

    if len(neg_nums) > 2 and len(neg_nums) % 2 != 0:
        '''
        The product of two negative integers is positive. If an odd number of integers
        are in neg_num list, the value closest to zero is removed and added to the higher list.
        The even number of remaining values will then result in a positive product, then added. 
        '''
        neg_nums.pop(neg_nums.index(max(neg_nums)))
        neg_product = reduce(mul, neg_nums)
        reduced_products_list.append(neg_product)

    elif len(neg_nums) % 2 == 0 and len(neg_nums) != 0:
        # Lists of even number of negative integers 
        neg_product = reduce(mul, neg_nums)
        reduced_products_list.append(neg_product)

    print(reduced_products_list)
    for i in range(1, len(reduced_products_list)+1):
        '''
        Find all possible sets of values in the reduced_products_list.
        The set of numbers [3, 4, 5] has 6 possible permutations:

        [[3], [4], [5]]
        [[3, 4], [4, 5]]
        [[3, 4, 5]]

        Reduce is applied to each subset and the largest product is added to higest list

        perms = [[3], [4], [5]]
        perms = [[12], [15]]
        perms = [60]

        products = [5, 15, 60]

        '''
        perms = [reduce(mul, e) for e in [list(y) for y in permutations(reduced_products_list, i)]]
        products.append(max(perms))

    return str(max(products))


print(answer([0,-6]))