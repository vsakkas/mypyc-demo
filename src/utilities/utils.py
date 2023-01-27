import random


def sort_string(string: str) -> str:
    """
    Sorts the input string in alphabetical order.

    Parameters:
    string (str): The input string to be sorted.

    Returns:
    str: The sorted string.
    """
    return "".join(sorted(string))


def randomize_string(string: str) -> str:
    """
    Randomizes the input string.

    Parameters:
    string (str): The input string to be randomized.

    Returns:
    str: The randomized string.
    """
    return "".join(random.sample(string, len(string)))


def reverse_string(string: str) -> str:
    """
    Reverses the input string.

    Parameters:
    string (str): The input string to be reversed.

    Returns:
    str: The reversed string.
    """
    return string[::-1]


def fibonacci(n: int) -> int:
    """
    Calculate the n-th number in the Fibonacci sequence using recursion.

    Parameters:
    n (int): The n-th number to calculate.

    Returns:
    int: The n-th number in the Fibonacci sequence.
    """
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
