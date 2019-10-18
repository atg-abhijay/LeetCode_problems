"""
URL of problem:
https://leetcode.com/problems/keys-and-rooms/
"""


class Room:
    def __init__(self, room_number, neighbours):
        self.room_number = room_number
        self.neighbour_indexes = neighbours
        self.visited = False


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        room_nodes = []
        for index, neighbours in enumerate(rooms):
            room_nodes.append(Room(index, neighbours))

        # Use DFS to explore the rooms. At the end,
        # check if all rooms have been visited.
        queue = [room_nodes[0]]
        while queue:
            room = queue.pop(0)
            if room.visited:
                continue

            room.visited = True
            for nb_index in room.neighbour_indexes:
                nb = room_nodes[nb_index]
                if not nb.visited:
                    queue.append(nb)

        return all(room.visited for room in room_nodes)


def main():
    print(Solution().canVisitAllRooms([[1, 3], [3, 0, 1], [2], [0]]))


if __name__ == '__main__':
    main()
