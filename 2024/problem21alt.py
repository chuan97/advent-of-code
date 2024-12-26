"""Solve problem 21 of the 2024 Advent of Code"""

from functools import lru_cache
from itertools import permutations
from typing import Tuple

codes = ["382A", "463A", "935A", "279A", "480A"]
test_codes = ["029A", "980A", "179A", "456A", "379A"]
test_codes_sequences = [
    "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
    "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
    "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
    "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
]

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

inv_num_keypad = {v: k for k, v in num_keypad.items()}

dir_keypad = {
    "<": (0, 0),
    "v": (1, 0),
    ">": (2, 0),
    "^": (1, 1),
    "A": (2, 1),
}

dir_keypad_effects = {
    "<": (-1, 0),
    "v": (0, -1),
    ">": (1, 0),
    "^": (0, 1),
    "A": (0, 0),
}

inv_dir_keypad = {v: k for k, v in dir_keypad.items()}

N_NUM_KPADS = 3


@lru_cache
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


@lru_cache
def compose_paths(
    coord_diff: Tuple[int, int], start: Tuple[int, int], type_: str
) -> str:
    """compose all possible paths using the directional keypad that produces the coordinate difference

    Args:
        coord_diff (tuple[2]): difference in coordinates as 2-vector
        type (str): type of keypad

    Returns:
        str: path composed
    """
    if type_ == "num":
        inv_kpad = inv_num_keypad
    elif type_ == "dir":
        inv_kpad = inv_dir_keypad

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

    paths = []
    for p in set(permutations(path)):
        p = "".join(p)
        pos = start
        good = True
        for step in p:
            pos = (
                pos[0] + dir_keypad_effects[step][0],
                pos[1] + dir_keypad_effects[step][1],
            )
            if pos not in inv_kpad:
                good = False
                break
        if good:
            paths.append(p + "A")
    return paths


@lru_cache
def find_shortest_sequence(code, n_kpads, first_call=True):
    if first_call:
        type_ = "num"
        kpad = num_keypad
    else:
        type_ = "dir"
        kpad = dir_keypad

    prev_char = "A"
    sequence = ""
    for c in code:
        coord_diff = key_coord_diff(prev_char, c, type_)
        paths = compose_paths(coord_diff, kpad[prev_char], type_)
        if n_kpads == 1:
            sequence += paths[0]
        else:
            deeper_paths = []
            for p in paths:
                deeper_paths.append(find_shortest_sequence(p, n_kpads - 1, False))
            sequence += min(deeper_paths, key=len)
        prev_char = c

    return sequence


@lru_cache
def find_len_shortest_sequence(code, n_kpads, first_call=True):
    if first_call:
        type_ = "num"
        kpad = num_keypad
    else:
        type_ = "dir"
        kpad = dir_keypad

    prev_char = "A"
    length = 0
    for c in code:
        coord_diff = key_coord_diff(prev_char, c, type_)
        paths = compose_paths(coord_diff, kpad[prev_char], type_)
        if n_kpads == 1:
            length += len(paths[0])
        else:
            deeper_paths = []
            for p in paths:
                deeper_paths.append(find_len_shortest_sequence(p, n_kpads - 1, False))
            length += min(deeper_paths)
        prev_char = c

    return length


def num_complexity(code: str) -> int:
    """calculate the numerical complexity of a code

    Args:
        code (str): the code

    Returns:
        int: the complexity of the code
    """
    return int(code[:-1])


if __name__ == "__main__":
    code = test_codes[0]
    sequence = find_shortest_sequence(code, 3)
    print(code)
    print(sequence)
    print(test_codes_sequences[0])

    for i, c in enumerate(test_codes):
        sequence = find_shortest_sequence(c, 3)
        print(len(sequence), len(test_codes_sequences[i]))

    lengths = [find_len_shortest_sequence(code, N_NUM_KPADS) for code in codes]
    print(lengths)
    complexities = [
        length * num_complexity(code) for length, code in zip(lengths, codes)
    ]
    print(sum(complexities))
