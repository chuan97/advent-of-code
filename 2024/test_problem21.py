"""tests for problem 21"""

from problem21 import (
    N_NUM_KPADS,
    compose_path,
    find_shortest_sequence,
    key_coord_diff,
    num_complexity,
)

test_codes = ["029A", "980A", "179A", "456A", "379A"]
test_codes_sequences = [
    "<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A",
    "<v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A",
    "<v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
    "<v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A",
    "<v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A",
]


def test_key_coord_diff():
    assert key_coord_diff("A", "9", "num") == (0, 3)
    assert key_coord_diff("A", "8", "num") == (-1, 3)
    assert key_coord_diff("A", "A", "num") == (0, 0)
    assert key_coord_diff("A", "A", "dir") == (0, 0)
    assert key_coord_diff("A", ">", "dir") == (0, -1)
    assert key_coord_diff("A", "v", "dir") == (-1, -1)


def test_compose_path():
    assert compose_path((0, 3)) == "^^^A"
    assert compose_path((-1, 1)) == "<^A"
    assert compose_path((0, 0)) == "A"
    assert compose_path((0, -1)) == "vA"
    assert compose_path((-1, -1)) == "<vA"


def test_num_complexity():
    assert num_complexity(test_codes[0]) == 29
    assert num_complexity(test_codes[1]) == 980
    assert num_complexity(test_codes[2]) == 179
    assert num_complexity(test_codes[3]) == 456
    assert num_complexity(test_codes[4]) == 379


def test_find_shortest_sequence():
    for code, sequence in zip(test_codes, test_codes_sequences):
        assert len(find_shortest_sequence(code, N_NUM_KPADS)) == len(sequence)
