from typing import List, Optional, Tuple

from archive.y2021.puzzles.day_19.input_part_1 import get_input


class Beacon:
    def __init__(self, x: int, y: int, z: int):
        self.x = x
        self.y = y
        self.z = z

    def __repr__(self):
        return f"B({self.x},{self.y},{self.z})"

    def __hash__(self):
        return hash(str(self))

    def __add__(self, other: "Beacon") -> "Beacon":
        return Beacon(x=self.x + other.x, y=self.y + other.y, z=self.z + other.z)

    def __neg__(self) -> "Beacon":
        return Beacon(x=-self.x, y=-self.y, z=-self.z)

    def __sub__(self, other: "Beacon") -> "Beacon":
        return self + (-other)

    def __eq__(self, other: "Beacon") -> bool:
        return self.x == other.x and self.y == other.y and self.z == other.z

    def __iter__(self):
        yield self.x
        yield self.y
        yield self.z

    def reorient(self, orientation_matrix: List[List[int]]) -> "Beacon":
        return Beacon(
            x=self.x * orientation_matrix[0][0] + self.y * orientation_matrix[0][1] + self.z * orientation_matrix[0][2],
            y=self.x * orientation_matrix[1][0] + self.y * orientation_matrix[1][1] + self.z * orientation_matrix[1][2],
            z=self.x * orientation_matrix[2][0] + self.y * orientation_matrix[2][1] + self.z * orientation_matrix[2][2],
        )


class Scanner:
    def __init__(self, beacons: List[Tuple[int, int, int]], scanners: List[Beacon] = None):
        self.beacons = [Beacon(*coords) for coords in beacons]
        self.scanners: List[Beacon] = scanners or [Beacon(0, 0, 0)]
        self.overlap_minimum = 12

        self._beacon_inter_distances: List[Tuple[int, Beacon, Beacon]] = []

    def beacon_inter_distances(self) -> List[Tuple[int, Beacon, Beacon]]:
        # Don't recalculate. This is static.
        if not self._beacon_inter_distances:

            distances = []

            for i in range(len(self.beacons) - 1):
                for j in range(i + 1, len(self.beacons)):
                    distances.append(
                        (self.square_distance(self.beacons[i], self.beacons[j]), self.beacons[i], self.beacons[j])
                    )

            self._beacon_inter_distances = sorted(distances, key=lambda x: x[0])

        return self._beacon_inter_distances

    @staticmethod
    def square_distance(from_beacon: Beacon, to_beacon: Beacon) -> int:
        return (
            (from_beacon.x - to_beacon.x) ** 2 + (from_beacon.y - to_beacon.y) ** 2 + (from_beacon.z - to_beacon.z) ** 2
        )

    def find_overlap_candidates(self, other: "Scanner") -> List[Beacon]:
        own_inter_distances = self.beacon_inter_distances()
        other_inter_distances = other.beacon_inter_distances()
        other_distance_values = [dist for dist, _, _ in other_inter_distances]

        overlaps_include: List[Tuple[Beacon, Beacon]] = []
        overlaps_include_flat: List[Beacon] = []

        for dist, own_beac_1, own_beac_2 in own_inter_distances:
            if dist in other_distance_values:
                overlaps_include.append((own_beac_1, own_beac_2))
                overlaps_include_flat.append(own_beac_1)
                overlaps_include_flat.append(own_beac_2)

        all_checked = False

        while not all_checked:
            all_checked = True

            for beac_pair in tuple(overlaps_include):
                min_count = min(overlaps_include_flat.count(val) for val in beac_pair)

                if min_count < self.overlap_minimum - 1:
                    # Case that this pair is not part of a set of overlap minimum beacons, all "connected".
                    overlaps_include.remove(beac_pair)
                    overlaps_include_flat.remove(beac_pair[0])
                    overlaps_include_flat.remove(beac_pair[1])
                    all_checked = False

        return list(set(overlaps_include_flat))

    def validate_overlap_candidates(self, other_beacons: List[Beacon]) -> Optional[Tuple[List[List[int]], Beacon]]:
        other_distances_moving = [
            self.square_distance(other_beacons[i], other_beacons[i + 1]) for i in range(len(other_beacons) - 1)
        ]

        this_beacon_distances = self.beacon_inter_distances()

        def build_beacon_chain(beacon_array: List[Beacon], distances_to_cover: List[int]) -> Optional[List[Beacon]]:
            nonlocal self
            if not distances_to_cover:
                return beacon_array

            next_distance = distances_to_cover[0]
            last_beacon = beacon_array[-1]

            next_matches = [
                beac1 if beac2 is last_beacon else beac2
                for dist, beac1, beac2 in this_beacon_distances
                if dist == next_distance and (beac1 is last_beacon or beac2 is last_beacon)
            ]

            next_matches = [beac for beac in next_matches if beac not in beacon_array]

            for match in next_matches:
                sub_chain = build_beacon_chain(beacon_array + [match], distances_to_cover[1:])

                if sub_chain:
                    return sub_chain

        for starting_beacon in self.beacons:
            matching_chain = build_beacon_chain([starting_beacon], other_distances_moving)

            if matching_chain:
                first_other_vector = other_beacons[1] - other_beacons[0]
                first_matching_vector = matching_chain[1] - matching_chain[0]

                orientation_matrix = [
                    [(ov // mv if abs(ov) == abs(mv) else 0) for mv in first_matching_vector]
                    for ov in first_other_vector
                ]

                shift = other_beacons[0] - matching_chain[0].reorient(orientation_matrix)

                return orientation_matrix, shift

    def reorient(self, orientation_matrix: List[List[int]], shift: Beacon) -> None:
        self.beacons = [beacon.reorient(orientation_matrix) + shift for beacon in self.beacons]
        self.scanners = [scanner.reorient(orientation_matrix) + shift for scanner in self.scanners]

        # Force recalculation
        self._beacon_inter_distances = []

    def merge(self, other: "Scanner") -> "Scanner":
        this_tuples = [(beac.x, beac.y, beac.z) for beac in self.beacons]
        other_tuples = [(beac.x, beac.y, beac.z) for beac in other.beacons]

        merged_beacons = list(set(this_tuples + other_tuples))

        return Scanner(merged_beacons, scanners=self.scanners + other.scanners)


def merge_next(scanners: List[Scanner]) -> Optional[Tuple[Scanner, Scanner, Scanner]]:
    for i in range(len(scanners) - 1):
        for j in range(i + 1, len(scanners)):
            cands = scanners[i].find_overlap_candidates(scanners[j])

            if not cands:
                continue

            orientation_change = scanners[j].validate_overlap_candidates(cands)

            if not orientation_change:
                continue

            scanners[j].reorient(*orientation_change)

            new_scanner = scanners[i].merge(scanners[j])

            return scanners[i], scanners[j], new_scanner


def merge_until_done(input_values: List[List[Tuple[int, int, int]]]) -> Scanner:
    scanners = [Scanner(vals) for vals in input_values]

    while len(scanners) > 1:

        result = merge_next(scanners)

        if not result:
            raise RuntimeError("Could not find a next merge couple.")

        to_remove_1, to_remove_2, to_add = result

        scanners.remove(to_remove_1)
        scanners.remove(to_remove_2)
        scanners.insert(0, to_add)

    return scanners[0]


def calculate_solution(input_values: List[List[Tuple[int, int, int]]]) -> int:
    final = merge_until_done(input_values)

    return len(final.beacons)


if __name__ == "__main__":
    print(calculate_solution(get_input()))
