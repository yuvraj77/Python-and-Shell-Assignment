def is_palindrome(s, t='both'):
    # only odd sequences can be palindromes
    if t=='odd':
        if len(s)%2 == 0:
            return False
        else:
            return s == s[::-1]

    # only even sequences can be palindromes
    elif t=='even':
        if len(s)%2:
            return False
        else:
            return s == s[::-1]

    # both even or odd sequences can be palindromes
    else:
        return s == s[::-1]