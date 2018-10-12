"""
URL of problem:
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""


def main(graph):
    # all_paths = traverse(graph, 0)
    all_paths = traverse2(graph, 0, [], len(graph)-1)
    for path in all_paths:
        print(path)


def traverse(graph, node):
    all_paths, path = [], []
    path.append(node)
    # stack.append(node)
    for child in graph[node]:
        # result = traverse(graph, child)
        path += traverse(graph, child)
        # stack = result[1]
        if node == 0 and path[-1] == len(graph) - 1:
            all_paths.append(path)
            path = [0]

    if node != 0:
        # stack.pop()
        return [path, stack]
    else:
        return all_paths


def traverse2(graph, node, path, last_node):
    all_paths = []
    path.append(node)
    if not graph[node]:
        if node == last_node:
            all_paths.append(path)
            return all_paths

    else:
        for child in graph[node]:
            path_to_send = [elem for elem in path]
            all_paths += traverse2(graph, child, path_to_send, last_node)

    return all_paths


if __name__ == '__main__':
    main([[4, 3, 1], [3, 2, 4], [3], [4], []])
