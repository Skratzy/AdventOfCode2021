import itertools
import math
import time
from collections import defaultdict
from functools import cache

validation = False


@cache
def get_rotated_pos(v, p, sign):
    return tuple([v[p[0]] * sign[0], v[p[1]] * sign[1], v[p[2]] * sign[2]])


@cache
def rotate_scanner(s, p, sign):
    return [get_rotated_pos(v, p, sign) for v in s]


def subtract_v(v1, v2):
    return tuple([v1[0] - v2[0], v1[1] - v2[1], v1[2] - v2[2]])


def add_v(v1, v2):
    return tuple([v1[0] + v2[0], v1[1] + v2[1], v1[2] + v2[2]])


def check(absolute_positions, relative_positions):
    for p in itertools.permutations([0, 1, 2]):
        for sign in [[1, 1, 1], [1, 1, -1], [1, -1, 1], [1, -1, -1],
                     [-1, 1, 1], [-1, 1, -1], [-1, -1, 1], [-1, -1, -1]]:
            diffs = defaultdict(int)
            rotated_positions = rotate_scanner(relative_positions, tuple(p), tuple(sign))

            for abs_pos in absolute_positions:
                for rotated_position in rotated_positions:
                    # We want to find 12 diffs that are the same
                    # rotated_pos = get_rotated_pos(rel_pos, p, sign)
                    diffs[add_v(abs_pos, rotated_position)] += 1

            for k, v in diffs.items():
                if v >= 12:
                    #print(k)
                    return True, [subtract_v(k, rotated_position) for rotated_position in rotated_positions], k

    return False, None, None


def both_parts():
    part_1_input_file = "input.txt"
    if validation:
        part_1_input_file = "validation_part_1.txt"
    with open(part_1_input_file, "r") as file:
        # Solution here
        input = file.read().split('\n\n')
        scanners = []
        for scanner in input:
            _, positions_s = scanner.split('---\n')
            positions_s = positions_s.split('\n')
            vertices = []
            for position_s in positions_s:
                vertex = [int(coordinate) for coordinate in position_s.split(',')]
                vertices.append(tuple(vertex))
            scanners.append(tuple(vertices))

        abs_beacon_positions = {0: scanners[0]}
        all_beacons = set()
        for beacon in scanners[0]:
            all_beacons.add(beacon)

        not_done_scanners = [i for i in range(1, len(scanners))]

        aligned_checked = {k: [] for k in range(len(scanners))}

        scanner_positions = {0: [0, 0, 0]}
        while not_done_scanners:
            found_scanner = False
            for scanner_to_check in not_done_scanners:
                if found_scanner:
                    break

                for aligned_scanner in abs_beacon_positions:
                    if aligned_scanner not in aligned_checked[scanner_to_check]:
                        #print(f"Checking {scanner_to_check} against aligned scanner {aligned_scanner}")
                        is_aligned, aligned_beacons, scanner_pos = check(abs_beacon_positions[aligned_scanner], scanners[scanner_to_check])

                        aligned_checked[scanner_to_check].append(aligned_scanner)

                        if is_aligned:
                            scanner_positions[scanner_to_check] = scanner_pos

                            abs_beacon_positions[scanner_to_check] = aligned_beacons
                            not_done_scanners.remove(scanner_to_check)
                            for beacon in aligned_beacons:
                                all_beacons.add(beacon)
                            found_scanner = True
                            break

        #print(scanner_positions)
        largest_manhattan_distance = 0
        manhattan_distances = []

        for k, v in scanner_positions.items():
            for k2, v2 in scanner_positions.items():
                largest_manhattan_distance = max(largest_manhattan_distance, sum(abs(val) for val in subtract_v(v, v2)))

        return len(all_beacons), largest_manhattan_distance


start = time.perf_counter()
answer_part_1, answer_part_2 = both_parts()
print(f'{answer_part_1=} {answer_part_2=}')
assert(answer_part_1 == 342 and answer_part_2 == 9668)
print(f'Took {time.perf_counter() - start} seconds.')
