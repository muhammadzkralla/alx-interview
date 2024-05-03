#!/usr/bin/python3
'''Lockboxes DFS Solution'''
visited = set()


def canUnlockAll(boxes):
    '''Setup Function'''
    visited.clear()
    dfs(boxes, 0)

    if len(visited) == len(boxes):
        return True

    return False


def dfs(boxes, currIdx):
    '''Dfs Function'''
    visited.add(currIdx)
    box = boxes[currIdx]

    for key in box:
        if key not in visited:
            dfs(boxes, key)
