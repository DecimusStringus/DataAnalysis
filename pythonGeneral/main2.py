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

def checkio(words: str) -> bool:
    # add your code here
    lwords = list(words.split(" "))
    c = 0
    for w in lwords:
        if w.isalpha():
            c += 1
            if c == 3:
                break
        else:
            c = 0
    return c == 3


print("Example:")
print(checkio("Hello World hello"))

# assert checkio("Hello World hello") == True
# assert checkio("He is 123 man") == False
# assert checkio("1 2 3 4") == False
# assert checkio("bla bla bla bla") == True
# assert checkio("Hi") == False
assert checkio('one two 3 four five six 7 eight 9 ten eleven 12') == True
print("The mission is done! Click 'Check Solution' to earn rewards!")