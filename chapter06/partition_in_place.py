from random import randint, shuffle


def partition_in_place(seq, p=0, r=None):
    """ A function that partitions an array in place.

    :param seq: A sequence of numbers (perhaps other comparable)
    :param p: The lowest index included in the partitioning
    :param r: The highest index included in the partitioning
    :return: Index of pivot element
    """

    if r is None:
        r = len(seq) - 1

    rand_idx = randint(p, r)

    if rand_idx != r:
        seq[rand_idx], seq[r] = seq[r], seq[rand_idx]

    pi = seq[r]

    i = p

    for j in range(p, r):
        if seq[j] <= pi:
            seq[i], seq[j] = seq[j], seq[i]
            i += 1

    seq[i], seq[-1] = seq[-1], seq[i]

    return i


def test():
    a = [i for i in range(10)]

    for j in range(5):
        b = a[:]
        shuffle(b)
        i = partition_in_place(b)
        print(b[:i], b[i], b[i + 1:])


if __name__ == "__main__":
    test()