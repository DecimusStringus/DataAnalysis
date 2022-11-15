# Taken from mission Acceptable Password I

def is_acceptable_password(password: str) -> bool:
    # your code here

    if 6 < len(password) <= 9 and 0 < sum(c.isdigit() for c in password) < len(password) or 9 < len(password):
        x = True
    else:
        x = False
    return x

assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("notshort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
