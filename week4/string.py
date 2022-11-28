"""
CP404 Strings - Do this now
"""


def main():
    string = "name=Bob&age=99&day=Wed"

    pairs = extract_pairs(string)
    result = [('name', 'Bob'), ('age', 99), ('day', 'Wed')]
    assert pairs == result
    print(pairs)


def extract_pairs(string):
    if not string.startswith('?'):
        return[]
    pairs = []
    parts = string[1:].split('&')
    for part in parts:
        pair = part.split('=')
        try:
            pair[1] = int(pair[1])
        except ValueError:
            pass
        pairs.append(tuple(pair))
    return pairs


main()