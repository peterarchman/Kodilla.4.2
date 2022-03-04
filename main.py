def is_palindron(text):
    if text == text[-1::-1]:
        return True
    else:
        return False

is_palindron("potop")