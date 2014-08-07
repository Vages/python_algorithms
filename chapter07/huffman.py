# The files for huffman-coding from the book

from heapq import heapify, heappush, heappop
from itertools import count

def huffman(seq, frq):
    num = count()
    trees = list(zip(frq, num, seq))
    heapify(trees)
    while len(trees) > 1:
        fa, _, a = heappop(trees)
        fb, _, b = heappop(trees)
        n = next(num)
        heappush(trees, (fa+fb, n, [a, b]))
    return trees[0][-1]


def codes(tree, prefix=""):
    if len(tree) == 1:
        yield (tree, prefix)                    # A leaf with its code
        return
    for bit, child in zip("01", tree):          # Left (0) and right (1)
        for pair in codes(child, prefix + bit): # Get codes recursively
            yield pair

def huffman_test():
    seq = "abcdefghi"
    frq = [4, 5, 6, 9, 11, 12, 15, 16, 20]
    my_tree = huffman(seq, frq)
    print(my_tree)

    code_list = list(codes(my_tree))

    print(code_list)

if __name__ == "__main__":
    huffman_test()