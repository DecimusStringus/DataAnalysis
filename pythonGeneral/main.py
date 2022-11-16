def is_acceptable_password(password: str) -> bool:
    # your code here
    return not ("password" in password.lower()) and 6 < len(password) <= 9 and 0 < sum(c.isdigit() for c in password) < len(password) or 9 < len(password) and not ("password" in password.lower())

assert is_acceptable_password("short") == False
assert is_acceptable_password("short54") == True
assert is_acceptable_password("muchlonger") == True
assert is_acceptable_password("ashort") == False
assert is_acceptable_password("muchlonger5") == True
assert is_acceptable_password("sh5") == False
assert is_acceptable_password("1234567") == False
assert is_acceptable_password("12345678910") == True
assert is_acceptable_password("password12345") == False
assert is_acceptable_password("PASSWORD12345") == False
assert is_acceptable_password("pass1234word") == True
assert is_acceptable_password('this is password') == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
