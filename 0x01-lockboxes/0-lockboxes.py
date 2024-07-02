#!/usr/bin/python3
"""
Module for the function
canUnlockAll
"""


def canUnlockAll(boxes):
    """
    Given a list of boxes, each containing a list of keys
    that can unlock it, this function determines whether
    it is possible to unlock all the boxes.

    :param boxes: a list of lists of integers, where each inner list represents
                    the keys that can unlock the corresponding box.
    :return: a boolean value indicating whether it is possible to unlock all
                the boxes.
    """
    n = len(boxes)  # Number of boxes
    unlocked = [False] * n  # Track which boxes are unlocked
    unlocked[0] = True  # Box 0 is initially unlocked
    keys = [0]  # Start with the key to box 0

    while keys:
        current_key = keys.pop()  # Take the next key to use
        for key in boxes[current_key]:  # Get all keys in the current box
            if key < n and not unlocked[key]:  # If the key opens a new box
                unlocked[key] = True  # Unlock the box
                keys.append(key)  # Add its keys to the list

    return all(unlocked)  # Check if all boxes are unlocked
