#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque


def bfs(n, m, edges, s):
    neighbors = [set() for _ in range(n)]
    for u, v in edges:
        neighbors[u - 1].add(v - 1)
        neighbors[v - 1].add(u - 1)
    visited = [False for _ in range(n)]
    dists = [-1 for _ in range(n)]

    dists[s - 1] = 0
    node_q = deque([s - 1])
    while len(node_q) > 0:
        node = node_q.popleft()
        if visited[node]:
            continue
        visited[node] = True

        for neighbor_node in neighbors[node]:
            if visited[neighbor_node]:
                continue
            if dists[neighbor_node] == -1:
                dists[neighbor_node] = dists[node] + 6
            node_q.append(neighbor_node)
    return dists[: s - 1] + dists[s:]


if __name__ == "__main__":
    with open(os.environ["INPUT_PATH"], "r") as f, open(os.environ["OUTPUT_PATH"], "w") as fptr:

        q = int(f.readline().strip())

        for q_itr in range(q):
            first_multiple_input = f.readline().rstrip().split()

            n = int(first_multiple_input[0])

            m = int(first_multiple_input[1])

            edges = []

            for _ in range(m):
                edges.append(list(map(int, f.readline().rstrip().split())))

            s = int(f.readline().strip())

            result = bfs(n, m, edges, s)

            fptr.write(" ".join(map(str, result)))
            fptr.write("\n")
