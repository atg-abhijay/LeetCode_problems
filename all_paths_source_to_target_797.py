"""
URL of problem:
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""


def main(graph):
    all_paths = traverse(graph, 0)
    for path in all_paths:
        print(path)


def traverse(graph, node):
    all_paths = []
    path = []
    path.append(node)
    for child in graph[node]:
        path += traverse(graph, child)
        if node == 0 and path[-1] == len(graph) - 1:
            all_paths.append(path)
            path = [0]

    if node != 0:
        return path
    else:
        return all_paths


if __name__ == '__main__':
    main([[4, 3, 1], [3, 2, 4], [3], [4], []])
