from typing import Tuple

codes = ["382A", "463A", "935A", "279A", "480A"]

num_keypad = {
    "0": (0, 1),
    "A": (0, 2),
    "1": (1, 0),
    "2": (1, 1),
    "3": (1, 2),
    "4": (2, 0),
    "5": (2, 1),
    "6": (2, 2),
    "7": (3, 0),
    "8": (3, 1),
    "9": (3, 2),
}

dir_keypad = {
    "<": ((0, 0), (-1, 0)),
    "v": ((1, 0), (0, -1)),
    ">": ((2, 0), (1, 0)),
    "^": ((1, 1), (0, 1)),
    "A": ((1, 2), (0, 0)),
}

inv_dir_keypad = {v[1]: k for k, v in dir_keypad.items()}


def find_shortest_sequence(code: str) -> str:
    """find shortest sequence of inputs that will produce the given code

    Args:
        code (str): the code to be produced

    Returns:
        str: the shortest sequence that produces the code
    """
    return ""


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
        a_coord = dir_keypad[a][0]
        b_coord = dir_keypad[b][0]
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
    # TODO: implement this
    horizontals = coord_diff[0]
    verticals = coord_diff[1]

    return None


if __name__ == "__main__":
    lengths = [len(find_shortest_sequence(code)) for code in codes]
    print(lengths)
    complexities = [length * int(code[:-1]) for length, code in zip(lengths, codes)]
    print(sum(complexities))
    print(key_coord_diff("0", "1", "num"))
