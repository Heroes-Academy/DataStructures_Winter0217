"""
This file is the solution to the recursive problems assigned in class.

There are comments below to explain things.
"""


def recursive_palindrome(number):
    number_str = str(number)
    if len(number_str) == 1:
        # in this case, there is only one thing left. return True
        return True

    elif number_str[0] == number_str[-1]:
        ### you can index a string like a list
        ### and indexing using -1 gets you the last item
        ### in this case, the number string is a palindrome so far
        ### so, let's cut off the ends and recurse on it

        ### this says, "Start at 1, go until -1"
        new_number_str = number_str[1:-1]

        ### just in case, check for 0 length (aka, our input string was only 2 long)
        ### then, we return True anyway
        if len(new_number_str) == 0:
            return True
        else:
            new_number = int(new_number_str)
            return recursive_palindrome(new_number)
    else:
        # this is the catch all condition.  it's false here.
        return False


def test_one():
    assert recursive_palindrome(1000) == False
    assert recursive_palindrome(110111233) == True
    assert recursive_palindrome(856743347658) == True

def hailstone_number(number):
    if number == 1:
        ### this it the base case
        return [number]
    elif number % 2 == 0:
        ### this is the first recursive case
        ### here I am putting the number into an array by itself
        ### and then, I add the result of the recursion to it
        ### this works because I know the function call will always return another array
        ### and you can add two arrays together to form a larger array
        return [number] + hailstone_number(number//2)
    else:
        ### the other recursive case.
        return [number] + hailstone_number(3*number+1)


def test_two():
    assert hailstone_number(8) == [8, 4, 2, 1]
    assert hailstone_number(9) == [9, 28, 14, 7, 22, 11, 34, 17, 52, 26, 13, 40, 20, 10, 5, 16, 8, 4, 2, 1]
    assert hailstone_number(3) == [3, 10, 5, 16, 8, 4, 2, 1]

def find_minimum_v1(a_list):
    if len(a_list) == 1:
        ### our base case, return the single  number
        return a_list[0]
    else:
        ### our recrusive case.
        ### get the first number
        first = a_list[0]
        ### find the minimum of the rest of the list
        second = find_minimum_v1(a_list[1:])
        return min(first, second)

def find_minimum_v2(a_list):
    if len(a_list) == 1:
        ### our first base case, return the single number
        return a_list[0]
    elif len(a_list) == 2:
        ### our other base case, return the min of the two numbers
        return min(a_list[0], a_list[1])
    else:
        ### find the minimum of either half and return it
        half = len(a_list) // 2
        first = find_minimum_v2(a_list[:half])
        second = find_minimum_v2(a_list[half:])
        return min(first, second)

def test_three():
    a_list = [1,2,3,4,817,83,-10,-188]
    assert find_minimum_v1(a_list) == -188
    assert find_minimum_v2(a_list) == -188


try:
    test_one()
except AssertionError as e:
    print("=========================")
    print("Test one failed.")
    print("=========================\n")
    raise e

try:
    test_two()
except AssertionError as e:
    print("=========================")
    print("Test two failed; {}".format(e))
    print("=========================\n")
    raise e

try:
    test_three()
except AssertionError as e:
    print("=========================")
    print("Test three failed; {}".format(e))
    print("=========================\n")
    raise e
