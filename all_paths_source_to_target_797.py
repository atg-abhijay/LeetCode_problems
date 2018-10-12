"""
URL of problem:
https://leetcode.com/problems/all-paths-from-source-to-target/description/
"""


def main(graph):
    all_paths = traverse(graph, 0, [], len(graph)-1)
    for path in all_paths:
        print(path)


def traverse(graph, node, path, last_node):
    all_paths = []
    path.append(node)
    # if node doesn't have any
    # children, then we have
    # reached the end of the path.
    # check whether path ends in last_node.
    # if it does, append path to all_paths
    # return updated all_paths
    if not graph[node]:
        if node == last_node:
            all_paths.append(path)
            return all_paths

    else:
        for child in graph[node]:
            # we copy the path found as of now
            # into a new path which is the one
            # used in the recursive call. this
            # ensures that when we return from
            # the recursive call, we don't end
            # up changing the path that was found
            # at this level in the stack of calls.
            path_to_send = [elem for elem in path]
            all_paths += traverse(graph, child, path_to_send, last_node)

    return all_paths


if __name__ == '__main__':
    main([[4, 3, 1], [3, 2, 4], [3], [4], []])
