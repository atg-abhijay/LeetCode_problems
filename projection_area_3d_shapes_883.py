"""
URL of problem:
https://leetcode.com/problems/projection-area-of-3d-shapes/description/
"""


def main(grid):
    """
    main method for running the program.
    Argument:
        grid - a 2D grid with grid[i][j] = height of tower
    Prints:
        Total projection area
    """
    dimension = len(grid)

    # dict where:
    # Key - tuple (x, y)
    # Value - height of tower
    xyz_dict = {}
    for i in range(dimension):
        for j in range(dimension):
            xyz_dict[(i, j)] = grid[i][j]

    # for xy_area we simply look at the
    # presence/absence of a tower. we don't
    # care about the height itself. if a tower
    # is present, then add 1 to the xy_area
    xy_area = 0
    for val in xyz_dict.values():
        if val != 0:
            xy_area += 1

    yz_dict = make_dict(xyz_dict, 1)
    yz_area = calc_area(yz_dict)

    xz_dict = make_dict(xyz_dict, 0)
    xz_area = calc_area(xz_dict)

    total_projection = xy_area + yz_area + xz_area
    print("Total projection:", total_projection)
    # return total_projection


def make_dict(xyz_dict, key_index):
    """
    Makes a dictionary where:
        Key - 'a'-value ('a' can be x or y)
        Value - list of all the z-values associated
                with that specific a-value
    Arguments:
        xyz_dict - dict with:
                    Key - tuple (x, y)
                    Value - the z-value for the tuple
        key_index - takes on a value of 0 or 1
                    for x or y in the tuple (x, y)
    Returns:
        a dictionary az ('a' can be x or y) where:
            Key - 'a'-value ('a' can be x or y)
            Value - list of all the z-values associated
                    with that specific a-value
    """
    az_dict = {}
    for key, z_val in xyz_dict.items():
        a_val = key[key_index]
        # if a_val already exists in dict,
        # then add the z_val to its list of
        # values else initialize the list
        # for it with this z_val
        if a_val in az_dict:
            az_dict[a_val].append(z_val)
        else:
            az_dict[a_val] = [z_val]

    return az_dict


def calc_area(az_dict):
    """
    For each of the coordinate values
    'a' (can be x or y), find the maximum
    value in its list of values and add
    that to the projection area on the
    az-plane.

    The projection area along each 'a'
    coordinate is the highest tower, therefore
    we take the maximum value for each coordinate.

    Argument:
        az_dict - dict with
                    Key - 'a'-value
                    Value - list of z-values
    Returns:
        Area of projection on the az-plane
    """
    az_area = 0
    for list_val in az_dict.values():
        az_area += max(list_val)

    return az_area


if __name__ == '__main__':
    main([[1, 2], [3, 4]])
