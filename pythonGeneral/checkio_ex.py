"""
Easy Unpack
"""
# Your mission here is to create a function that gets a tuple and returns a tuple with only 3 elements - the first, third and second element from the last for the given tuple.
# def easy_unpack(elements: tuple) -> tuple:
#     # your code here
#     return (elements[0], elements[2], elements[-2])
#
#
# print("Example:")
# print(easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)))
#
# assert easy_unpack((1, 2, 3, 4, 5, 6, 7, 9)) == (1, 3, 7)
# assert easy_unpack((1, 1, 1, 1)) == (1, 1, 1)
# assert easy_unpack((6, 3, 7)) == (6, 7, 3)
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Index Power
"""
# You are given an array with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
#
# Let's look at a few examples:
# - array = [1, 2, 3, 4] and N = 2, then the result is 3 2 == 9;
# - array = [1, 2, 3] and N = 3, but N is outside of the array, so the result is -1.
#
# Input: Two arguments. An array as a list of integers and a number as a integer.
#
# Output: The result as an integer.
# How it is used: This mission teaches you how to use basic arrays and indexes when combined with simple mathematics.
# Precondition: 0 < len(array) ≤ 10
# 0 ≤ N
# all(0 ≤ x ≤ 100 for x in array)
# def index_power(array: list, n: int) -> int:
#     # your code here
#     if len(array) > n:
#         result = array[n] ** n
#     else:
#         result = -1
#     return result
#
# print("Example:")
# print(index_power([1, 2, 3], 2))
#
# assert index_power([1, 2, 3, 4], 2) == 9
# assert index_power([1, 3, 10, 100], 3) == 1000000
# assert index_power([0, 1], 0) == 1
# assert index_power([1, 2], 3) == -1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Median
"""
# A median is a numerical value separating the upper half of a sorted list of numbers from the lower half. In a list where there are an odd number of entities, the median is the number found in the middle of the list. If the list contains an even number of entities, then there is no single middle value, instead the median becomes the average of the two numbers found in the middle. For this mission, you are given a non-empty list of natural integers. With it, you must separate the upper half of the numbers from the lower half and find the median.
# Input: A list of integers.
#
# Output: The median as a float or an integer.
# def checkio(data: list[int]) -> int | float:
#     # replace this for solution
#     data = sorted(data)
#     if len(data) % 2 == 0:
#         return (data[int(len(data)/2 - 1)] + data[int(len(data)/2)])/2
#     else:
#         return data[int(len(data)//2)]
#
#
# print("Example:")
# # print(checkio([1, 2, 3, 4, 5]))
#
# assert checkio([1, 2, 3, 4, 5]) == 3
# assert checkio([3, 1, 2, 5, 3]) == 3
# assert checkio([1, 300, 2, 200, 1]) == 2
# assert checkio([3, 6, 20, 99, 10, 15]) == 12.5
# assert checkio([10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]) == 5
# assert checkio([0, 7, 1, 8, 4, 9, 5, 6, 2, 3]) == 4.5
# assert checkio([33, 56, 62]) == 56
# assert checkio([21, 56, 84, 82, 52, 9]) == 54
# assert checkio([100, 1, 1, 1, 1, 1, 1]) == 1
# assert checkio([64, 6, 92, 7, 70, 5]) == 35.5
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Stock Profit
"""
# You are a broker with a single chance to buy stock and sell stock. Having an array of prices, pick the best time to buy stock and sell stock to maximize the profit.
# “short-selling” (sell first, buy later) is not allowed in this market.
# Your profit is zero when it is impossible to get profit at all. The size of pricing can't be less than 2.
# Input: Array of int. Stock prices.
#
# Output: Int. Maximum possible profit.
# def stock_profit(stock: list) -> int:
#     # your code here
#     result = 0
#     for max_price in sorted(stock)[::-1]:
#         for count_max, var_max in enumerate(reversed(stock)):
#             if var_max == max_price and result == 0:
#                 for min_price in sorted(stock):
#                     for count_min, var_min in enumerate(stock):
#                         if var_min == min_price and result == 0:
#                             if len(stock) - count_max - 1 > count_min and max_price - min_price > 0:
#                                 result = max_price - min_price
#                                 break
#     if result < 0:
#         return 0
#     else:
#         return result
#
# print("Example:")
# print(stock_profit([3, 1, 3, 4, 5, 1]))
#
# assert stock_profit([2, 3, 4, 5]) == 3
# assert stock_profit([3, 1, 3, 4, 5, 1]) == 4
# assert stock_profit([4, 3, 2, 1]) == 0
# assert stock_profit([6, 2, 1, 2, 3, 2, 3, 4, 5, 4]) == 4
# assert stock_profit([1, 1, 1, 2, 1, 1, 1]) == 1
# assert stock_profit([4, 3, 2, 1, 2, 1, 2, 1]) == 1
# assert stock_profit([1, 1, 1, 1]) == 0
# assert stock_profit([60, 50, 51, 52, 40]) == 2
#
# print("You are the best broker here! Click 'Check' to earn cool rewards!")
"""
Even the Last
"""
# You are given an array of integers. You should find the sum of the integers with even indexes (0th, 2nd, 4th...). Then multiply this summed number and the final element of the array together. Don't forget that the first element has an index of 0.
# For an empty array, the result will always be 0 (zero).
# Input: A list of integers.
# Output: The number as an integer.
# def checkio(array: list[int]) -> int:
#     # your code here
#     result = 0
#     if array:
#         for count, var in enumerate(array,start=2):
#             if count % 2 == 0:
#                 result += var
#         result *= array[-1]
#     return result
#
# print("Example:")
# print(checkio([0, 1, 2, 3, 4, 5]))
#
# assert checkio([0, 1, 2, 3, 4, 5]) == 30
# assert checkio([1, 3, 5]) == 30
# assert checkio([6]) == 36
# assert checkio([]) == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Duplicate Zeros
"""
# "Sometimes, zeros resemble very tasty donut. And every time we finish a donut, we want another, and then another, and then another..."
#
# You are given a list of integers. Your task in this mission is to duplicate (..., 🍩, ... --> ..., 🍩, 🍩, ...) all zeros (think about donuts ;-P) and return the result as any Iterable. Let's look on the example:
# donuts: list[int] = [1, 0, 2, 0]
# print(list(duplicate_zeros(donuts)))
# Output:
# [1, 0, 0, 2, 0, 0]
#
# Input: A List of integers.
# Output: A List on another Iterable (tuple, generator, iterator) of integers.
# from typing import Iterable
#
#
# def duplicate_zeros(donuts: list[int]) -> Iterable[int]:
#     # your code here
#     result = []
#     for i in donuts:
#         result.append(i)
#         if i == 0:
#             result.append(i)
#     return result
#
# print("Example:")
# print(list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])))
#
# assert list(duplicate_zeros([1, 0, 2, 3, 0, 4, 5, 0])) == [
#     1,
#     0,
#     0,
#     2,
#     3,
#     0,
#     0,
#     4,
#     5,
#     0,
#     0,
# ]
# assert list(duplicate_zeros([0, 0, 0, 0])) == [0, 0, 0, 0, 0, 0, 0, 0]
# assert list(duplicate_zeros([100, 10, 0, 101, 1000])) == [100, 10, 0, 0, 101, 1000]
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Right to Left
"""
# One of the robots is charged with a simple task: to join a sequence of strings into one sentence to produce instructions on how to get around the ship. But this robot is left-handed and has a tendency to joke around and confuse its right-handed friends.
# You are given a sequence of strings. You should join these strings into a chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.
# Input: A sequence of strings.
# Output: The text as a comma-separated string.
# def left_join(phrases: tuple) -> str:
#     """
#     Join strings and replace "right" to "left"
#     """
#     return ','.join(phrases).replace("right", "left")
#
#
# print("Example:")
# print(left_join(("left", "right", "left", "stop")))
#
# assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
# assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
# assert left_join(("brightness wright",)) == "bleftness wleft"
# assert left_join(("enough", "jokes")) == "enough,jokes"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Non Empty Lines
"""
# You need to count how many non-empty lines a given text has.
# An empty line is a line without symbols or the one that contains only spaces.
# Input: A text.
# Output: An int.
# def non_empty_lines(text: str) -> int:
#     # your code here
#     result = 0
#     if text:
#         for s in text.split("\n"):
#             if len(s.strip(" ")) > 0:
#                 result += 1
#     return result
#
#
# print("Example:")
# print(non_empty_lines("one simple line\n"))
#
# assert non_empty_lines("one simple line\n") == 1
# assert non_empty_lines("") == 0
# assert non_empty_lines("\nonly one line\n            ") == 1
# assert (
#     non_empty_lines(
#         "\nLorem ipsum dolor sit amet,\n\nconsectetur adipiscing elit\nNam odio nisi, aliquam\n            "
#     )
#     == 3
# )
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Replace First
"""
# In a given list the first element should become the last one. An empty list or list with only one element should stay the same.
# from typing import Iterable
#
# def replace_first(items: list) -> Iterable:
#     # your code here
#     if items:
#         items.append(items.pop(0))
#     return items
#
# print("Example:")
# print(list(replace_first([1, 2, 3, 4])))
#
# assert replace_first([1, 2, 3, 4]) == [2, 3, 4, 1]
# assert replace_first([1]) == [1]
# assert replace_first([]) == []
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
All the Same
"""
# In this mission you should check if all elements in the given list are equal.
# from typing import List, Any
#
# def all_the_same(elements: List[Any]) -> bool:
#     # your code here
#     if elements:
#         template = elements[0]
#         for item in elements:
#             if template != item:
#                 return False
#     return True
#
#
# print("Example:")
# print(all_the_same([1, 1, 1]))
#
# assert all_the_same([1, 1, 1]) == True
# assert all_the_same([1, 2, 1]) == False
# assert all_the_same([1, 1, 1, 2]) == False
# assert all_the_same([2, 1, 1, 1]) == False
# assert all_the_same([]) == True
# assert all_the_same([1]) == True
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Majority
"""
# We have a list of booleans. Let's check if the majority of elements are True.
# Some cases worth mentioning: 1) an empty list should return False; 2) if True-s and False-s have an equal amount, function should return False.
# Input: A list of booleans.
# Output: A Boolean.
def is_majority(items: list[bool]) -> bool:
    # your code here
    # t_count = 0
    # f_count = 0
    # if items:
    #     for item in items:
    #         if item == True:
    #             t_count += 1
    #         elif item == False:
    #             f_count += 1
    #     if t_count > f_count:
    #         return True
    #
    # return False
# The code above is commented because it is clumsy
# The code below is better
#     if items:
#         my_dict = {item: items.count(item) for item in items}
#         if True in my_dict.keys() and False in my_dict.keys():
#             if my_dict[1] > my_dict[0]:
#                 return True
#         elif True in my_dict.keys():
#             return True
#     return False
#
# print("Example:")
# print(is_majority([True, True, False, True, False]))
#
# assert is_majority([True, True, False, True, False]) == True
# assert is_majority([True, True, False]) == True
# assert is_majority([True, True, False, False]) == False
# assert is_majority([True, True, False, False, False]) == False
# assert is_majority([False]) == False
# assert is_majority([True]) == True
# assert is_majority([]) == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Backward Each Word
"""
# In a given string you should reverse every word, but the words should stay in their places.
# Input: A string.
# Output: A string.
def backward_string_by_word(text: str) -> str:
    # your code here
    return None


print("Example:")
print(backward_string_by_word(""))

assert backward_string_by_word("") == ""
assert backward_string_by_word("world") == "dlrow"
assert backward_string_by_word("hello world") == "olleh dlrow"
assert backward_string_by_word("hello   world") == "olleh   dlrow"
assert backward_string_by_word("welcome to a game") == "emoclew ot a emag"

print("The mission is done! Click 'Check Solution' to earn rewards!")

