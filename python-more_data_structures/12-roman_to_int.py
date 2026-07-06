def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0
    d = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    t = [d[c] for c in roman_string if c in d]
    return sum(-x if x < y else x for x, y in zip(t, t[1:] + [0]))
