def is_palindrom(text):
    lenght = len(text)
    if text[0] == text[-1]:
        return True
    else:
        return False

is_palindrom("kajak")