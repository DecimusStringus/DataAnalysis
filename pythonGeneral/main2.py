# def between_markers(text: str, start: str, end: str) -> str:
#     # your code here
#     return text[text.index(start)+1:text.index(end)]
#
#
# print("Example:")
# print(between_markers("What is >apple<", ">", "<"))
#
# assert between_markers("What is >apple<", ">", "<") == "apple"
# assert between_markers("What is [apple]", "[", "]") == "apple"
# assert between_markers("What is ><", ">", "<") == ""
# assert between_markers("[an apple]", "[", "]") == "an apple"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Next code
"""
# def beginning_zeros(a: str) -> int:
#     # your code here
#     c = 0
#     for i in a:
#         if i == '0':
#             c = c + 1
#         else:
#             break
#     return c
#
# print("Example:")
# print(beginning_zeros("10"))
#
# assert beginning_zeros("100") == 0
# assert beginning_zeros("001") == 2
# assert beginning_zeros("100100") == 0
# assert beginning_zeros("001001") == 2
# assert beginning_zeros("012345679") == 1
# assert beginning_zeros("0000") == 4
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Next code
"""
# def checkio(words: str) -> bool:
#     # add your code here
#     lwords = list(words.split(" "))
#     c = 0
#     for w in lwords:
#         if w.isalpha():
#             c += 1
#             if c == 3:
#                 break
#         else:
#             c = 0
#     return c == 3
#
#
# print("Example:")
# print(checkio("Hello World hello"))
#
# # assert checkio("Hello World hello") == True
# # assert checkio("He is 123 man") == False
# # assert checkio("1 2 3 4") == False
# # assert checkio("bla bla bla bla") == True
# # assert checkio("Hi") == False
# assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Next code
"""
# products = [("Dining Table", 3, 199.90), ("Chair", 12, 39.59), ("Shelf", 5, 9.90)]
#
# for product in products:
#     print(
#         f"{product[0]:15s} Count: {product[1]:3d} Price: {product[2]:6.2f} Total: {product[1]*product[2]:6.2f}"
#     )
"""
Next code
"""
# def max_digit(value: int) -> int:
#     # your code here
#     if value == 0:
#         return 0
#     else:
#         return int(sorted(list(str(value)))[-1])
#
# print("Example:")
# print(max_digit(10))
#
# assert max_digit(0) == 0
# assert max_digit(52) == 5
# assert max_digit(634) == 6
# assert max_digit(1) == 1
# assert max_digit(10000) == 1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Next code
"""
# def sum_numbers(text: str) -> int:
#     # your code here
#     c = 0
#     for w in text.split(' '):
#         if w.isdigit():
#             c += int(w)
#
#     return c
#
#
# print("Example:")
# print(sum_numbers("hi"))
#
# assert sum_numbers("hi") == 0
# assert sum_numbers("who is 1st here") == 0
# assert sum_numbers("my numbers is 2") == 2
# assert (
#         sum_numbers(
#             "This picture is an oil on canvas painting by Danish artist Anna Petersen between 1845 and 1910 year"
#         )
#         == 3755
# )
# assert sum_numbers("5 plus 6 is") == 11
# assert sum_numbers("") == 0
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Acceptable Password VI
"""
# In this mission you need to create a password verification function.
#
# The verification conditions are:
#
# the length should be bigger than 6;
# should contain at least one digit, but it cannot consist of just digits;
# having numbers or containing just numbers does not apply to the password longer than 9.
# a string should not contain the word "password" in any case;
# should contain at least 3 different letters (or digits) even if it is longer than 10
# Taken from mission Acceptable Password V
# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return not ("password" in password.lower()) and 6 < len(password) <= 9 and 0 < sum(c.isdigit() for c in password) < len(password)\
#         and len(set(password)) >= 3 \
#         or 9 < len(password) and not ("password" in password.lower()) and len(set(password)) >= 3
#
# assert is_acceptable_password("short") == False
# assert is_acceptable_password("short54") == True
# assert is_acceptable_password("muchlonger") == True
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True
# assert is_acceptable_password("sh5") == False
# assert is_acceptable_password("1234567") == False
# assert is_acceptable_password("12345678910") == True
# assert is_acceptable_password("password12345") == False
# assert is_acceptable_password("PASSWORD12345") == False
# assert is_acceptable_password("pass1234word") == True
# assert is_acceptable_password("aaaaaa1") == False
# assert is_acceptable_password("aaaaaabbbbb") == False
# assert is_acceptable_password("aaaaaabb1") == True
# assert is_acceptable_password("abc1") == False
# assert is_acceptable_password("abbcc12") == True
# assert is_acceptable_password("aaaaaaabbaaaaaaaab") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
First Word
"""
# You are given a string where you have to find its first word.
#
# When solving a task pay attention to the following points:
#
# There can be dots and commas in a string.
# A string can start with a letter or, for example, one/multiple dot(s) or space(s).
# A word can contain an apostrophe and it's a part of a word.
# The whole text can be represented with one word and that's it.
# def first_word(text: str) -> str:
#     """
#     function returns the first word in a given text.
#     """
#     # your code here
#     # import re
#     # return re.split('.| ', text.strip(',. '))[0].strip(',. ') - didn't work
#
#     return text.replace('.', ' ').strip(',. ').split(' ')[0].strip(',. ')
#
#
# print("Example:")
# print(first_word("Hello world"))
#
# assert first_word("Hello world") == "Hello"
# assert first_word(" a word ") == "a"
# assert first_word("don't touch it") == "don't"
# assert first_word("greetings, friends") == "greetings"
# assert first_word("... and so on ...") == "and"
# assert first_word("hi") == "hi"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Correct Sentence
"""
# For the input of your function, you will be given one sentence. You have to return a corrected version, that starts with a capital letter and ends with a period (dot).
#
# Pay attention to the fact that not all of the fixes are necessary. If a sentence already ends with a period (dot), then adding another one will be a mistake.
# def correct_sentence(text: str) -> str:
#     """
#     returns a corrected sentence which starts with a capital letter
#     and ends with a dot.
#     """
#     # your code here
#     nextext = list(text.rstrip('.')+'.')
#     nextext[0] = nextext[0].upper()
#     return ''.join(nextext)
#
# print("Example:")
# print(correct_sentence("greetings, friends"))
#
# assert correct_sentence("greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends") == "Greetings, friends."
# assert correct_sentence("Greetings, friends.") == "Greetings, friends."
# assert correct_sentence("greetings, friends.") == "Greetings, friends."
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Speech Module
"""
# Stephen's speech module is broken. This module is responsible for his number pronunciation.
# He has to click to input all of the numerical digits in a figure, so when there are big numbers it can take him a long time.
# Help the robot to speak properly and increase his number processing speed by writing a new speech module for him.
# All the words in the string must be separated by exactly one space character.
# Be careful with spaces - it's hard to see if you place two spaces instead one.
# FIRST_TEN = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
# SECOND_TEN = [
#     "ten",
#     "eleven",
#     "twelve",
#     "thirteen",
#     "fourteen",
#     "fifteen",
#     "sixteen",
#     "seventeen",
#     "eighteen",
#     "nineteen",
# ]
# OTHER_TENS = [
#     "twenty",
#     "thirty",
#     "forty",
#     "fifty",
#     "sixty",
#     "seventy",
#     "eighty",
#     "ninety",
# ]
# HUNDRED = "hundred"
#
# def checkio(num: int) -> str:
#     # replace this for solution
#     # less than 10
#     if len(str(num)) == 1:
#         result = FIRST_TEN[num-1]
#     # two digits
#     elif len(str(num)) == 2:
#         # two digits: less than 20
#         if num < 20:
#             result = SECOND_TEN[num-10]
#         # two digits: 20 and bigger
#         else:
#             # round
#             if len(str(num).rstrip('0')) == 1:
#                 result = OTHER_TENS[int(str(num)[0]) - 2]
#             # not round
#             else:
#                 result = OTHER_TENS[int(str(num)[0])-2] + ' ' + FIRST_TEN[int(str(num)[1])-1]
#     # three digits
#     elif len(str(num)) == 3:
#         # define variables
#         hundred = ''.join(str(num)[0])
#         dozen = ''.join(str(num)[1:])
#         lastdigit = ''.join(str(num)[2])
#         # amount of complete hundreds
#         result = FIRST_TEN[int(hundred)-1] + ' ' + HUNDRED
#         if len(str(num).rstrip('0')) == 1:
#             result = result
#         # process last two digits
#         else:
#             # last two digits: first ten
#
#             if int(dozen) < 10:
#                 result = result + ' ' + FIRST_TEN[int(lastdigit)-1]
#                 # last two digits: second ten
#             elif 10 <= int(dozen) < 20:
#                 result = result + ' ' + SECOND_TEN[int(dozen) - 10]
#             # last two digits: 20 and bigger
#             else:
#                 # round
#                 if len(dozen.rstrip('0')) == 1:
#                     result = result + ' ' + OTHER_TENS[int(str(dozen)[0]) - 2]
#                 # not round
#                 else:
#                     result = result + ' ' + OTHER_TENS[int(str(num)[1]) - 2] + ' ' + FIRST_TEN[int(str(num)[2]) - 1]
#     return result
#
#
# print("Example:")
# print(checkio(4))
#
# assert checkio(1) == "one"
# assert checkio(2) == "two"
# assert checkio(3) == "three"
# assert checkio(4) == "four"
# assert checkio(5) == "five"
# assert checkio(6) == "six"
# assert checkio(9) == "nine"
# assert checkio(10) == "ten"
# assert checkio(11) == "eleven"
# assert checkio(12) == "twelve"
# assert checkio(13) == "thirteen"
# assert checkio(14) == "fourteen"
# assert checkio(15) == "fifteen"
# assert checkio(16) == "sixteen"
# assert checkio(17) == "seventeen"
# assert checkio(18) == "eighteen"
# assert checkio(19) == "nineteen"
# assert checkio(999) == "nine hundred ninety nine"
# assert checkio(784) == "seven hundred eighty four"
# assert checkio(777) == "seven hundred seventy seven"
# assert checkio(88) == "eighty eight"
# assert checkio(44) == "forty four"
# assert checkio(20) == "twenty"
# assert checkio(30) == "thirty"
# assert checkio(40) == "forty"
# assert checkio(50) == "fifty"
# assert checkio(80) == "eighty"
# assert checkio(90) == "ninety"
# assert checkio(100) == "one hundred"
# assert checkio(200) == "two hundred"
# assert checkio(300) == "three hundred"
# assert checkio(600) == "six hundred"
# assert checkio(700) == "seven hundred"
# assert checkio(900) == "nine hundred"
# assert checkio(21) == "twenty one"
# assert checkio(312) == "three hundred twelve"
# assert checkio(302) == "three hundred two"
# assert checkio(509) == "five hundred nine"
# assert checkio(753) == "seven hundred fifty three"
# assert checkio(940) == "nine hundred forty"
# assert checkio(999) == "nine hundred ninety nine"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Next task
"""