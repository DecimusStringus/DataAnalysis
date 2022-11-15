# Taken from mission Acceptable Password I

# def is_acceptable_password(password: str) -> bool:
#     # your code here
#     return (len(password)>6 and
#     any([x.isdigit() for x in password]) and
#     any([x.isalpha() for x in password]))
p='t2esti1ng'

print(sum(c.isdigit() for c in p))

# assert is_acceptable_password("short") == False
# assert is_acceptable_password("muchlonger") == False
# assert is_acceptable_password("ashort") == False
# assert is_acceptable_password("muchlonger5") == True
# assert is_acceptable_password("sh5") == False
# assert is_acceptable_password("1234567") == False
#
# print("The mission is done! Click 'Check Solution' to earn rewards!")
