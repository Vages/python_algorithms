def coord_sort(tuple_list, sort_coord="x"):
    """Sorts a list of (x, y) coordinates by their x or y coordinates using merge sort."""

    if sort_coord == "x": idx = 0
    else: idx = 1

    mid = len(tuple_list)//2

    lft, rgt = tuple_list[:mid], tuple_list[mid:]

    if len(lft) > 1: lft = coord_sort(lft, sort_coord)
    if len(rgt) > 1: rgt = coord_sort(rgt, sort_coord)

    res = []

    while lft and rgt:
        if lft[-1][idx] >= rgt[-1][idx]:
            res.append(lft.pop())
        else:
            res.append(rgt.pop())

    res.reverse()

    return (lft or rgt) + res


def sort_test():
    """Test for the coord_sort method"""
    raw_data = [(2,3),(1,4),(0,5),(3,2),(4,1),(5,0)]
    print(coord_sort(raw_data[:], "x"))
    print(coord_sort(raw_data[:], "y"))

    # passed


if __name__ == "__main__":
    sort_test()