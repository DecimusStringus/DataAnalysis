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
import operator

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
# def goes_after(word: str, first: str, second: str) -> bool:
#     # your code here
#     if first + second in word:
#         return word.index(first) == word.index(second) - 1
#     else:
#         return False
#
# print("Example:")
# print(goes_after("world", "w", "o"))
#
# # assert goes_after("world", "w", "o") == True
# # assert goes_after("world", "w", "r") == False
# assert goes_after("world", "l", "o") == False
# assert goes_after("panorama", "a", "n") == True
# assert goes_after("list", "l", "o") == False
# assert goes_after("", "l", "o") == False
# assert goes_after("list", "l", "l") == False
# assert goes_after("world", "d", "w") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Bird Language
"""
# The bird converts words by two rules:
# - after each consonant letter the bird appends a random vowel letter (l ⇒ la or le);
# - after each vowel letter the bird appends two of the same letter (a ⇒ aaa);
# Vowels letters == "aeiouy".
# You are given an ornithological phrase as several words which are separated by white-spaces (each pair of words by one whitespace). The bird does not know how to punctuate its phrases and only speaks words as letters. All words are given in lowercase. You should translate this phrase from the bird language to something more understandable.
# def translate(text: str) -> str:
#     # your code here
#     vovels = "aeiouy"
#
#     # rule 2
#     for v in vovels:
#         text = text.replace(v*3, v)
#     # rule 1
#     output_text = text.split(' ')
#     for wcount, word in enumerate(text.split(' ')):
#         to_remove = list()
#         for lcount, letter in enumerate(word):
#             if letter not in vovels and word[lcount+1] in vovels:
#                 if [word[lcount:lcount+2], word[lcount]] not in to_remove:
#                     to_remove.append([word[lcount:lcount+2], word[lcount]])
#                 # output_text = output_text.replace(text[count:count+2], letter)
#
#         for each in to_remove:
#             word = word.replace(each[0], each[1])
#         output_text[wcount] = word
#     return ' '.join(output_text)
#
#
# print("Example:")
# print(translate("hieeelalaooo"))
#
# assert translate("hieeelalaooo") == "hello"
# assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
# assert translate("aaa bo cy da eee fe") == "a b c d e f"
# assert translate("sooooso aaaaaaaaa") == "sos aaa"
# assert translate('aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa') == 'abcdefghijklmnopqrstuvwxyz zyxwvutsrqponmlkjihgfedcba'
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
End Zeros
"""
# Try to find out how many zeros a given number has at the end.
# def end_zeros(a: int) -> int:
#     # your code here
#     return len(str(a)) - len(str(a).rstrip('0'))
#
#
# print("Example:")
# print(end_zeros(10))
#
# assert end_zeros(0) == 1
# assert end_zeros(1) == 0
# assert end_zeros(10) == 1
# assert end_zeros(101) == 0
# assert end_zeros(245) == 0
# assert end_zeros(100100) == 2
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Feed Pigeons
"""
# I start to feed one of the pigeons. A minute later two more fly by and a minute after that another 3. Then 4, and so on (Ex: 1+2+3+4+...). One portion of food lasts a pigeon for a minute, but in case there's not enough food for all the birds, the pigeons who arrived first ate first. Pigeons are hungry animals and eat without knowing when to stop. If I have N portions of bird feed, how many pigeons will be fed with at least one portion of wheat?
# How it is used: this task illustrates how we can model various situations. Of course, the model has a limited approximation, but often-times we don't need a perfect model.
#
# Precondition: 0 < N < 10 5 .
# def checkio(food: int) -> int:
#     # your code here
#     pigeon = 0
#     minute = 1
#     while food - pigeon > 0:
#         pigeon += minute
#         if food - pigeon >= 0:
#             food -= pigeon
#         else:
#             pigeon -= pigeon - food
#         minute += 1
#     return pigeon
#
#
# print("Example:")
# print(checkio(5))
#
# assert checkio(1) == 1
# assert checkio(3) == 2
# assert checkio(5) == 3
# assert checkio(10) == 6
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Excel Column Number
"""
# Given a string that represents the column title as appears in an Excel sheet, return its corresponding column number.
# def column_number(name: str) -> int:
#     # your code here
#     abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
#     counter = 0
#     for letter in ''.join(reversed(name)):
#         if counter == 0:
#             result = abc.index(letter) + 1
#         else:
#             result += (abc.index(letter) + 1) * len(abc) ** counter
#         counter += 1
#     return result
#     #return len(abc) ** len(name) + (abc.index(name[-1]) + 1)
#
#
# print("Example:")
# print(column_number("BA"))
# print(column_number("FXSHRXW"))
#
# assert column_number("A") == 1
# assert column_number("Z") == 26
# assert column_number("AB") == 28
# assert column_number("ZY") == 701
# assert column_number('FXSHRXW') == 2147483647
# print("The first mission is done! Click 'Check' to earn cool rewards!")

"""
Digits Multiplication
"""
# You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.
# For example: The number given is 123405. The result will be 1*2*3*4*5=120 (don't forget to exclude zeroes).

# def checkio(number: int) -> int:
#     # your code here
#     result = 1
#     for i in str(number).replace('0',''):
#         result *= int(i)
#     return result
#
# print("Example:")
# print(checkio(123405))
#
# assert checkio(123405) == 120
# assert checkio(999) == 729
# assert checkio(1000) == 1
# assert checkio(1111) == 1
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
All Upper I
"""
# Check if a given string has all symbols in upper case. If the string is empty or doesn't have any letter in it - function should return True.
# def is_all_upper(text: str) -> bool:
#     # your code here
#     return text.isupper() or text.replace(' ','') == "" or text.replace(' ','').isdigit()
#
#
# print("Example:")
# print(is_all_upper("ALL UPPER"))
#
# assert is_all_upper("ALL UPPER") == True
# assert is_all_upper("all lower") == False
# assert is_all_upper("mixed UPPER and lower") == False
# assert is_all_upper("") == True
# assert is_all_upper("444") == True
# assert is_all_upper("55 55 5 ") == True
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Conversion from CamelCase
"""
# Your mission is to convert the name of a function (a string) from CamelCase ("MyFunctionName") into the Python format ("my_function_name") where all chars are in lowercase and all words are concatenated with an intervening underscore symbol "_".
# def from_camel_case(name: str) -> str:
#     # replace this for solution
#     pname = list()
#     counter = 0
#     for letter in name:
#         if letter.isupper() and counter > 0:
#             pname.append("_" + letter.lower())
#         else:
#             pname.append(letter.lower())
#         counter += 1
#     return ''.join(pname)
#
# print("Example:")
# print(from_camel_case("MyFunctionName"))
#
# assert from_camel_case("MyFunctionName") == "my_function_name"
# assert from_camel_case("IPhone") == "i_phone"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Conversion into CamelCase
"""
# Your mission is to convert the name of a function (a string) from the Python format (for example "my_function_name") into CamelCase ("MyFunctionName"), where the first char of every word is in uppercase and all words are concatenated without any intervening characters.
# def to_camel_case(name: str) -> str:
#     # replace this for solution
#     upper = 1
#     camel_name = list()
#     for letter in name:
#         if upper == 1:
#             camel_name.append(letter.upper())
#             upper = 0
#         elif letter == '_':
#             upper = 1
#         else:
#             camel_name.append(letter)
#
#     return ''.join(camel_name)
#
# print("Example:")
# print(to_camel_case("my_function_name"))
#
# assert to_camel_case("my_function_name") == "MyFunctionName"
# assert to_camel_case("i_phone") == "IPhone"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
The Most Wanted Letter
"""
# You are given a text, which contains different English letters and punctuation symbols. You should find the most frequent letter in the text. The letter returned must be in lower case.
# While checking for the most wanted letter, casing does not matter, so for the purpose of your search, "A" == "a". Make sure you do not count punctuation symbols, digits and whitespaces, only letters.
#
# If you have two or more letters with the same frequency , then return the letter which comes first in the Latin alphabet. For example -- "one" contains "o", "n", "e" only once for each, thus we choose "e".

# How it is used: For most decryption tasks you need to know the frequency of occurrence for various letters in a section of text. For example: we can easily crack a simple addition or substitution cipher if we know the frequency in which letters appear. This is interesting stuff for language experts!
#
# Precondition :
# A text contains only ASCII symbols.
# 0 < len(text) ≤ 10 5
# import operator
# def checkio(text: str) -> str:
#     # your code here
#     freq = {}
#     text = text.lower()
#     for letter in text:
#         if letter.isalpha():
#             if letter in freq:
#                 freq[letter] += 1
#             else:
#                 freq[letter] = 1
#     result = sorted(freq.items(), key=operator.itemgetter(1), reverse=True)
#     # process equal frequency items
#     var = result[0][1]
#     result_list = []
#     for line in result:
#         if line[1] == var:
#             result_list.append(line[0])
#
#     return sorted(result_list)[0]
#
# print("Example:")
# print(checkio("Hello World!"))
#
# # assert checkio("Hello World!") == "l"
# # assert checkio("How do you do?") == "o"
# # assert checkio("One") == "e"
# # assert checkio("Oops!") == "o"
# assert checkio("AAaooo!!!!") == "a"
# assert checkio("abe") == "a"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")

"""
Middle Characters
"""
# You are given some string where you need to find its middle character(s). The string may contain one word, a few symbols or a whole sentence. If the length of the string is even, then you should return two middle characters, but if the length is odd, return just one. For more details look at the Example.
# def middle(text: str) -> str:
#     # replace this for solution
#     if len(text) % 2 == 0:
#         return text[int(len(text)/2 - 1):int(len(text)/2+1)]
#     else:
#         return text[int(len(text)//2):int(len(text)//2 + 1)]
#
# print("Example:")
# print(middle("example"))
#
# assert middle("example") == "m"
# assert middle("test") == "es"
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
"""
Cut Sentence
"""
# Your task in this mission is to truncate a sentence to a length that does not exceed a given number of characters.
#
# If the given sentence already is short enough, you don't have to do anything to it. But if it needs to be truncated, the omission must be indicated by concatenating an ellipsis ("...") to the end of the shortened sentence.
#
# The shortened sentence can contain complete words and spaces.
# It must neither contain truncated words nor trailing spaces.
# The ellipsis has been taken into account for the allowed number of characters, so it does not count against the given length.
# line.startswith(' ') == False
# 0 < len(line) ≤ 79
# 0 < length ≤ 76
# all(char in string.ascii_letters + ' ' for char in line)
def cut_sentence(line: str, length: int) -> str:
    """
    Cut a given sentence, so it becomes shorter than or equal to a given length.
    """
    # your code here
#     result_line = []
#     if len(line) > length:
#         #line = line[:length-2].rstrip(' ') + '...'
#         for word in line.split(' '):
#             if len(' '.join(result_line) + ' ' + word) <= length:
#                 result_line.append(word)
#             else:
#                 break
#         result = ' '.join(result_line) + '...'
#     else:
#         result = line
#     return result
#
# print("Example:")
# print(cut_sentence("Hi my name is Alex", 4))
# #print(cut_sentence('OMG you did it', 4))
#
# assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
# assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
# assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
# assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"
# assert cut_sentence('Hi my name is Alex', 9) == 'Hi my...'
# assert cut_sentence('OMG you did it', 4) == 'OMG...'
# print("The mission is done! Click 'Check Solution' to earn rewards!")


