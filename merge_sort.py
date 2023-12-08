#!/usr/bin/env bash
"""The merge function"""

def mergeSort(array):
    """
    Merge Sort: Merges two sorted arrays into a single sorted array.

    Args:
        array (list): The input list to be sorted.

    Returns:
        list: A sorted list.

    """
    # Base case: if the array has only one element, it is already sorted
    if len(array) == 1:
        return array
    else:
        # Divide the array into two halves and recursively sort each half
        value1 = sortLeftArray(array)
        value2 = sortRightArray(array)

        # Merge the sorted halves
        value3 = mergeFunction(value1, value2)
        return value3


def sortLeftArray(array):
    """
    Sort Left Array: Recursively sorts the left half of the input array.

    Args:
        array (list): The input list to be sorted.

    Returns:
        list: A sorted list.

    """
    # Find the index to divide the array into two halves
    findIndex = len(array) // 2

    # Divide the array into the left half
    divideLeft = array[0:findIndex]
    _ = array[findIndex:]  # Discard the right half

    # Base case: if the left half has only one element, it is already sorted
    if len(divideLeft) == 1:
        return divideLeft
    else:
        # Recursively sort the left half
        value = mergeFunction(divideLeft)
        return value


def sortRightArray(array):
    """
    Sort Right Array: Recursively sorts the right half of the input array.

    Args:
        array (list): The input list to be sorted.

    Returns:
        list: A sorted list.

    """
    # Find the index to divide the array into two halves
    findIndex = len(array) // 2

    _ = array[0:findIndex]  # Discard the left half
    divideRight = array[findIndex:]  # Take the right half

    # Base case: if the right half has only one element, it is already sorted
    if len(divideRight) == 1:
        return divideRight
    else:
        # Recursively sort the right half
        value = mergeFunction(divideRight)
        return value


def mergeFunction(value1, value2):
    """
    Merge Function: Merges two sorted arrays into a single sorted array.

    Args:
        value1 (list): The first sorted list.
        value2 (list): The second sorted list.

    Returns:
        list: A merged and sorted list.

    """
    maxLength = len(value1) + len(value2)
    merge = []

    # Iterate through the combined length of the two lists
    for _ in range(maxLength):
        length1 = len(value1)
        length2 = len(value2)

        # Cases:
        if length1 == 0:
            merge.append(value2[0])
            value2.pop(0)
        elif length2 == 0:
            merge.append(value1[0])
            value1.pop(0)
        elif value1[0] < value2[0]:
            merge.append(value1[0])
            value1.pop(0)
        else:
            merge.append(value2[0])
            value2.pop(0)

    return merge
