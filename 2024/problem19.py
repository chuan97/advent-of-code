"""Solve problem 19 of the 2024 Advent of Code"""

from functools import lru_cache
from typing import Tuple

test_patterns = ("r", "wr", "b", "g", "bwu", "rb", "gb", "br")
test_designs = ("brwrr", "bggr", "gbbr", "rrbgbr", "ubwu", "bwurrg", "brgr", "bbrgwb")


# @lru_cache
# def can_design_be_made(design: str, patterns: Tuple[str]) -> bool:
#     """Check if a design can be made from the available patterns

#     Args:
#         design (str): the design to be made
#         pattern (str): the patterns to be used

#     Returns:
#         bool: True if the design can be made from the pattern, False otherwise
#     """
#     for pattern in patterns:
#         l = len(pattern)
#         if design[:l] == pattern:
#             if l == len(design):
#                 return True

#             if can_design_be_made(design[l:], patterns):
#                 return True

#     return False


@lru_cache
def can_design_be_made(design: str, patterns: Tuple[str]) -> bool:
    """Check if a design can be made from the available patterns

    Args:
        design (str): the design to be made
        pattern (str): the patterns to be used

    Returns:
        bool: True if the design can be made from the pattern, False otherwise
    """
    if design == "":
        return True

    for pattern in patterns:
        l = len(pattern)
        if design[:l] == pattern and can_design_be_made(design[l:], patterns):
            return True

    return False


# @lru_cache
# def number_of_ways_to_make_desing(design: str, patterns: Tuple[str]) -> int:
#     """Compute the number of ways a design can be made from the available patterns

#     Args:
#         design (str): the design to be made
#         pattern (str): the patterns to be used

#     Returns:
#         int: the number of ways
#     """
#     n_ways = 0
#     for pattern in patterns:
#         l = len(pattern)
#         if design[:l] == pattern:
#             if l == len(design):
#                 n_ways += 1
#             else:
#                 n_ways += number_of_ways_to_make_desing(design[l:], patterns)

#     return n_ways


@lru_cache
def number_of_ways_to_make_desing(design: str, patterns: Tuple[str]) -> int:
    """Compute the number of ways a design can be made from the available patterns

    Args:
        design (str): the design to be made
        pattern (str): the patterns to be used

    Returns:
        int: the number of ways
    """
    if design == "":
        return 1

    n_ways = 0
    for pattern in patterns:
        l = len(pattern)
        if design[:l] == pattern:
            n_ways += number_of_ways_to_make_desing(design[l:], patterns)

    return n_ways


def read_patterns(file_path: str) -> Tuple[str]:
    """Read the input file and return the patterns and designs

    Args:
        file_path (str): the path to the input file

    Returns:
        tuple: the patterns and designs
    """
    with open(file_path, "r", encoding="utf-8") as file:
        return tuple(file.readline().split(", "))  # patterns


if __name__ == "__main__":
    print([can_design_be_made(design, test_patterns) for design in test_designs])
    print(
        sum(
            number_of_ways_to_make_desing(design, test_patterns)
            for design in test_designs
        )
    )

    print("-----------------")

    f_input = "2024/input_19_1.txt"
    patterns = read_patterns(f_input)
    n_possible_designs = 0
    total_n_ways = 0
    with open(f_input, "r", encoding="utf-8") as file:
        next(file)
        next(file)

        for line in file:
            n_possible_designs += can_design_be_made(line.strip(), patterns)
            total_n_ways += number_of_ways_to_make_desing(line.strip(), patterns)

    print(n_possible_designs)
    print(total_n_ways)
