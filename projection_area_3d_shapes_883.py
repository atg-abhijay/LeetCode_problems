"""
URL of problem: https://leetcode.com/problems/projection-area-of-3d-shapes/description/
"""

def main(grid):
    dimension = len(grid)

    # yz_dict = {}
    # for i in range(dimension):
    #     column = grid[i]
    #     for j in range(dimension):
    #         z_val = column[j]

    xyz_dict = {}
    for i in range(dimension):
        for j in range(dimension):
            xyz_dict[(i,j)] = grid[i][j]

    # yz_dict = {}
    # for key, z_val in xyz_dict.items():
    #     y_val = key[1]
    #     if y_val in yz_dict:
    #         yz_dict[y_val].append(z_val)
    #     else:
    #         yz_dict[y_val] = [z_val]

    # yz_area = 0
    # for list_val in yz_dict.values():
    #     yz_area += max(list_val)

    # xz_dict = {}
    # for key, z_val in xyz_dict.items():
    #     x_val = key[0]
    #     if x_val in xz_dict:
    #         xz_dict[x_val].append(z_val)
    #     else:
    #         xz_dict[x_val] = x_val

    # print(yz_dict)

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


def make_dict(xyz_dict, key_index):
    az_dict = {}
    for key, z_val in xyz_dict.items():
        a_val = key[key_index]
        if a_val in az_dict:
            az_dict[a_val].append(z_val)
        else:
            az_dict[a_val] = [z_val]

    return az_dict


def calc_area(az_dict):
    az_area = 0
    for list_val in az_dict.values():
        az_area += max(list_val)

    return az_area


if __name__ == '__main__':
    main([[1,2],[3,4]])
