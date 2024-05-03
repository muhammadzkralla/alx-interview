#!/usr/bin/python3
'''Lockboxes DFS Solution'''
visited = set()

def canUnlockAll(boxes) :
    visited.clear()
    dfs(boxes, 0)

    if len(visited) == len(boxes):
        return True

    return False

def dfs(boxes, currIdx) :
    visited.add(currIdx)
    box = boxes[currIdx]

    for key in box:
        if key not in visited:
            dfs(boxes, key)