from itertools import cycle

from commons import get_input, remove_empty

seq = list(map(int, remove_empty(get_input(1).split('\n'))))

found = set()

freq = 0
dup = 0
for el in cycle(seq):
    freq += el
    if freq in found:
        dup = freq
        break
    found.add(freq)

if __name__ == '__main__':
    print("first:", sum(seq))
    print("second:", dup)
