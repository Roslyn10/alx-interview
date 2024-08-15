#!/usr/bin/env python3
""" A function that determines whether boxes can be opened using a key"""

def canUnlockAll(boxes):
    """
    Returns the length of the unlocked boxes if it equals the length of the boxes
    """

    keys = set()
    unlocked = set()
    queue = [0]
    unlocked.add(0)

    while queue:
        current_box = queue.pop(0)
        for key in boxes[current_box]:
            if key < len(boxes) and key not in unlocked:
                unlocked.add(key)
                queue.append(key)

    return len(unlocked) == len(boxes)
