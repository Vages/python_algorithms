from random import randint, shuffle


def quicksort(seq, p=0, r=None):
    """Sorts an array in place using quicksort

    :param seq: The array
    :param p: Index of first element included in sort.
    :param r: Index of last element included in sort.
    :return: None
    """
    if r is None:
        r = len(seq)-1

    if p < r:
        q = partition_in_place(seq, p, r)
        quicksort(seq, p, q-1)
        quicksort(seq, q+1, r)



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

    seq[i], seq[r] = seq[r], seq[i]

    return i


def partition_test():
    print("Partition test")

    a = [i for i in range(10)]

    for j in range(5):
        b = a[:]
        shuffle(b)
        print(b)
        i = partition_in_place(b)
        print(b[:i], b[i], b[i + 1:], "\n")

def quicksort_test():
    print("Quicksort test")

    a = [i for i in range(10)]

    for j in range(5):
        b = a[:]
        shuffle(b)
        print(b)
        quicksort(b)
        print(b, "\n")

if __name__ == "__main__":
    partition_test()
    quicksort_test()