"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}

    # Your code goes here
    for a in items:
        new_a = str(a)

        if new_a in frequencies:
            frequencies[new_a] += 1
        else:
            frequencies[new_a] = 1

    return frequencies
