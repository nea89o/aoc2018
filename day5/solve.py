from string import ascii_lowercase, ascii_uppercase

from commons import get_input

removals = [''.join(x) for x in
            list(zip(ascii_uppercase, ascii_lowercase)) + list(zip(ascii_lowercase, ascii_uppercase))]

inp = get_input(5)


def find_reduced_length(txt):
    last = ""

    while last != txt:
        last = txt
        for removal in removals:
            txt = txt.replace(removal, '')
            if txt != last:
                break
    return len(txt)


def find_best_removal(txt):
    min_length = 1000000000
    for ch in ascii_lowercase:
        length = find_reduced_length(txt.replace(ch, '').replace(ch.upper(), ''))
        if length < min_length:
            min_length = length
    return min_length


if __name__ == '__main__':
    print("first:", find_reduced_length(inp))
    print("second:", find_best_removal(inp))
