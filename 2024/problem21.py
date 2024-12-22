"""Solve problem 21 of the 2024 Advent of Code"""

from typing import Tuple

codes = ["382A", "463A", "935A", "279A", "480A"]

num_keypad = {
    "0": (1, 0),
    "A": (2, 0),
    "1": (0, 1),
    "2": (1, 1),
    "3": (2, 1),
    "4": (0, 2),
    "5": (1, 2),
    "6": (2, 2),
    "7": (0, 3),
    "8": (1, 3),
    "9": (2, 3),
}

dir_keypad = {
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
    "^": (1, 1),
    "A": (2, 1),
}

N_NUM_KPADS = 3


def find_shortest_sequence(code: str, n_num_keypads: int) -> str:
    """find shortest sequence of inputs that will produce the given code

    Args:
        code (str): the code to be produced
        N_num_keypads (int): number of numberic keypads in the chain of commands

    Returns:
        str: the shortest sequence that produces the code
    """
    start = "A"
    sequence = ""
    for char in code:
        coord_diff = key_coord_diff(start, char, "num")
        path = compose_path(coord_diff)
        sequence += path
        start = char

    for _ in range(n_num_keypads - 1):
        goal = sequence
        start = "A"
        sequence = ""
        for char in goal:
            coord_diff = key_coord_diff(start, char, "dir")
            path = compose_path(coord_diff)
            sequence += path
            start = char

    return sequence


def key_coord_diff(a: str, b: str, type_: str) -> Tuple[int, int]:
    """find the difference in coordinates between two keys on the keypad

    Args:
        a (str): first key
        b (str): second key
        type (str): type of keypad

    Returns:
        tuple[2]: difference in coordinates as 2-vector
    """
    if type_ == "num":
        a_coord = num_keypad[a]
        b_coord = num_keypad[b]
    elif type_ == "dir":
        a_coord = dir_keypad[a]
        b_coord = dir_keypad[b]
    else:
        raise ValueError(f"Invalid type: '{type_}', must be 'num' or 'dir'")

    return (b_coord[0] - a_coord[0], b_coord[1] - a_coord[1])


def compose_path(coord_diff: Tuple[int, int]) -> str:
    """compose a path using the directional keypad that produces the coordinate difference

    Args:
        coord_diff (tuple[2]): difference in coordinates as 2-vector

    Returns:
        str: path composed
    """
    n_hsteps_signed = coord_diff[0]
    n_vsteps_signed = coord_diff[1]

    path = ""
    if n_hsteps_signed > 0:
        path += ">" * n_hsteps_signed
    elif n_hsteps_signed < 0:
        path += "<" * abs(n_hsteps_signed)

    if n_vsteps_signed > 0:
        path += "^" * n_vsteps_signed
    elif n_vsteps_signed < 0:
        path += "v" * abs(n_vsteps_signed)

    return path + "A"


def num_complexity(code: str) -> int:
    """calculate the numerical complexity of a code

    Args:
        code (str): the code

    Returns:
        int: the complexity of the code
    """
    return int(code[:-1])


if __name__ == "__main__":
    lengths = [len(find_shortest_sequence(code, N_NUM_KPADS)) for code in codes]
    print(lengths)
    complexities = [
        length * num_complexity(code) for length, code in zip(lengths, codes)
    ]
    print(sum(complexities))
