from collections import Counter

from commons import get_input, remove_empty

txt = set(remove_empty(get_input(2).split('\n')))
counts = [set(Counter(l).values()) for l in txt]
threes = sum(3 in count for count in counts)
twos = sum(2 in count for count in counts)


def find():
    for i in txt:
        for j in txt:
            if i == j:
                continue
            for k in range(len(j)):
                i_, j_ = list(i), list(j)
                i_[k] = j_[k]
                if i_ == j_:
                    return i[:k] + i[k + 1:]


if __name__ == '__main__':
    print("first: ", twos * threes)
    print("second:", find())
