from collections import defaultdict

from archive.y2024.puzzles.day_12.load_inputs import input_reader, InputType
from archive.y2024.puzzles.day_12.solution_part_1 import GardenMap
from utils.common_structures.planar_map import Location


def updated_calculate_fence_price(region: list[Location]) -> int:
    area = len(region)

    fence_locations = defaultdict(int)
    fence_orientations = {}

    for loc in region:
        fence_locations[(loc.row + 0.5, loc.col)] += 1
        fence_orientations[(loc.row + 0.5, loc.col)] = "L"
        fence_locations[(loc.row, loc.col + 0.5)] += 1
        fence_orientations[(loc.row, loc.col + 0.5)] = "U"
        fence_locations[(loc.row - 0.5, loc.col)] += 1
        fence_orientations[(loc.row - 0.5, loc.col)] = "R"
        fence_locations[(loc.row, loc.col - 0.5)] += 1
        fence_orientations[(loc.row, loc.col - 0.5)] = "D"

    sides = consolidate_sides([
        k for k, v in fence_locations.items() if v == 1
    ], fence_orientations)

    return area * sides


def consolidate_sides(
    fence_locations: list[tuple[float, float]],
    orientations: dict[tuple[float, float], str],
) -> int:
    consolidated_fences = []

    while fence_locations:
        iter_fence = fence_locations.pop(0)
        iter_orientation = orientations[iter_fence]
        fence_group = [iter_fence]

        if iter_fence[0] == int(iter_fence[0]):
            to_right = 0
            while True:
                to_right += 1
                fence_to_right = (iter_fence[0] + to_right, iter_fence[1])
                if fence_to_right not in fence_locations:
                    break

                if orientations[fence_to_right] != iter_orientation:
                    break

                fence_group.append(fence_locations.pop(fence_locations.index(fence_to_right)))

            to_left = 0
            while True:
                to_left += 1
                fence_to_left = (iter_fence[0] - to_left, iter_fence[1])
                if fence_to_left not in fence_locations:
                    break

                if orientations[fence_to_left] != iter_orientation:
                    break

                fence_group.append(fence_locations.pop(fence_locations.index(fence_to_left)))

        if iter_fence[1] == int(iter_fence[1]):
            to_bottom = 0
            while True:
                to_bottom += 1
                fence_to_bottom = (iter_fence[0], iter_fence[1] + to_bottom)
                if fence_to_bottom not in fence_locations:
                    break

                if orientations[fence_to_bottom] != iter_orientation:
                    break

                fence_group.append(fence_locations.pop(fence_locations.index(fence_to_bottom)))

            to_top = 0
            while True:
                to_top += 1
                fence_to_top = (iter_fence[0], iter_fence[1] - to_top)
                if fence_to_top not in fence_locations:
                    break

                if orientations[fence_to_top] != iter_orientation:
                    break

                fence_group.append(fence_locations.pop(fence_locations.index(fence_to_top)))

        consolidated_fences.append(fence_group)

    return len(consolidated_fences)


def calculate_solution(input_values: InputType) -> int:
    garden = GardenMap(input_values)

    areas = garden.detect_regions()

    checksum = 0

    for area in areas:
        checksum += updated_calculate_fence_price(area)

    return checksum


if __name__ == "__main__":
    puzzle_input = input_reader.from_file("./input.txt")
    print(calculate_solution(puzzle_input))
