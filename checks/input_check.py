def user_enter_digit(*digits):
    for digit in digits:
        if not digit.isdigit():
            return False

    return True
