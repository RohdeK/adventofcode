from typing import List, Tuple, Union, Optional
from itertools import combinations

from archive.y2021.puzzles.day_22.input_part_1 import get_input


class Cube:
    def __init__(self, x_range: Tuple[int, int], y_range: Tuple[int, int], z_range: Tuple[int, int], on: bool):
        self.x_0, self.x_1 = x_range
        self.y_0, self.y_1 = y_range
        self.z_0, self.z_1 = z_range

        self.on_status = on

    def __repr__(self):
        return (
            f"Cube ({'ON' if self.on_status else 'OFF'}): "
            f"({self.x_0}, {self.x_1})x({self.y_0},{self.y_1})x({self.z_0},{self.z_1})"
        )

    @classmethod
    def from_rep(cls, rep: str) -> "Cube":
        on_status, coords = rep.split(" ")

        x_coords, y_coords, z_coords = coords.split(",")

        x_range = x_coords.split("=")[1]
        y_range = y_coords.split("=")[1]
        z_range = z_coords.split("=")[1]

        x_0, x_1 = x_range.split("..")
        y_0, y_1 = y_range.split("..")
        z_0, z_1 = z_range.split("..")

        return cls(
            x_range=(int(x_0), int(x_1)),
            y_range=(int(y_0), int(y_1)),
            z_range=(int(z_0), int(z_1)),
            on=on_status == "on",
        )

    def volume(self) -> int:
        return (self.x_1 - self.x_0 + 1) * (self.y_1 - self.y_0 + 1) * (self.z_1 - self.z_0 + 1)

    def degenerate(self) -> bool:
        return self.x_0 > self.x_1 or self.y_0 > self.y_1 or self.z_0 > self.z_1

    def corners(self) -> List[Tuple[int, int, int]]:
        return [
            (self.x_0, self.y_0, self.z_0),
            (self.x_0, self.y_0, self.z_1),
            (self.x_0, self.y_1, self.z_0),
            (self.x_0, self.y_1, self.z_1),
            (self.x_1, self.y_0, self.z_0),
            (self.x_1, self.y_0, self.z_1),
            (self.x_1, self.y_1, self.z_0),
            (self.x_1, self.y_1, self.z_1),
        ]

    def edges(
        self,
    ) -> List[Tuple[Union[int, Tuple[int, int]], Union[int, Tuple[int, int]], Union[int, Tuple[int, int]]]]:
        return [
            (self.x_0, self.y_0, (self.z_0, self.z_1)),
            (self.x_0, self.y_1, (self.z_0, self.z_1)),
            (self.x_1, self.y_0, (self.z_0, self.z_1)),
            (self.x_1, self.y_1, (self.z_0, self.z_1)),
            (self.x_0, (self.y_0, self.y_1), self.z_0),
            (self.x_0, (self.y_0, self.y_1), self.z_1),
            (self.x_1, (self.y_0, self.y_1), self.z_0),
            (self.x_1, (self.y_0, self.y_1), self.z_1),
            ((self.x_0, self.x_1), self.y_0, self.z_0),
            ((self.x_0, self.x_1), self.y_0, self.z_1),
            ((self.x_0, self.x_1), self.y_1, self.z_0),
            ((self.x_0, self.x_1), self.y_1, self.z_1),
        ]

    def faces(
        self, out=0
    ) -> List[Tuple[Union[int, Tuple[int, int]], Union[int, Tuple[int, int]], Union[int, Tuple[int, int]]]]:
        return [
            (self.x_0 - out, (self.y_0, self.y_1), (self.z_0, self.z_1)),
            ((self.x_0, self.x_1), self.y_0 - out, (self.z_0, self.z_1)),
            ((self.x_0, self.x_1), (self.y_0, self.y_1), self.z_0 - out),
            (self.x_1 + out, (self.y_0, self.y_1), (self.z_0, self.z_1)),
            ((self.x_0, self.x_1), self.y_1 + out, (self.z_0, self.z_1)),
            ((self.x_0, self.x_1), (self.y_0, self.y_1), self.z_1 + out),
        ]

    def is_inside(self, point: Tuple[int, int, int]) -> bool:
        return (
            self.x_0 <= point[0] <= self.x_1 and self.y_0 <= point[1] <= self.y_1 and self.z_0 <= point[2] <= self.z_1
        )

    def split(self, based_on: "Cube") -> List["Cube"]:
        sub_cubes: List[Cube] = []

        if self.is_disjoint(based_on):
            return [self]

        # Split this cube into all subcubes that spread from the corners of the other cube.
        for i, corner in enumerate(based_on.corners()):
            if sub_cube := self.cut_from_corner(corner, i):
                sub_cubes.append(sub_cube)

        for i, edge in enumerate(based_on.edges()):
            if sub_cube := self.cut_from_edge(edge, i):
                sub_cubes.append(sub_cube)

        # Split this cube into all subcubes that are extended from the faces of the other cube.
        for i, face in enumerate(based_on.faces()):
            if sub_cube := self.cut_from_face(face, i):
                sub_cubes.append(sub_cube)

        return sub_cubes

    def is_disjoint(self, based_on: "Cube") -> bool:
        return (
            based_on.x_0 > self.x_1
            or based_on.x_1 < self.x_0
            or based_on.y_0 > self.y_1
            or based_on.y_1 < self.y_0
            or based_on.z_0 > self.z_1
            or based_on.z_1 < self.z_0
        )

    def cut_from_corner(self, corner_point: Tuple[int, int, int], corner_type: int) -> Optional["Cube"]:
        x, y, z = corner_point
        # Corner to the x-side
        if corner_type in (0, 1, 2, 3):
            x_range = (self.x_0, x - 1)
        else:
            x_range = (x + 1, self.x_1)

        if corner_type in (0, 1, 4, 5):
            y_range = (self.y_0, y - 1)
        else:
            y_range = (y + 1, self.y_1)

        if corner_type in (0, 2, 4, 6):
            z_range = (self.z_0, z - 1)
        else:
            z_range = (z + 1, self.z_1)

        return self.limited_cutout(x_range, y_range, z_range)

    def cut_from_edge(self, edge_dim_val, edge_type: int) -> Optional["Cube"]:
        if edge_type in (0, 1, 2, 3):
            x, y, z_range = edge_dim_val

            if edge_type in (0, 1):
                x_range = (self.x_0, x - 1)
            else:
                x_range = (x + 1, self.x_1)
            if edge_type in (0, 2):
                y_range = (self.y_0, y - 1)
            else:
                y_range = (y + 1, self.y_1)

        elif edge_type in (4, 5, 6, 7):
            x, y_range, z = edge_dim_val

            if edge_type in (4, 5):
                x_range = (self.x_0, x - 1)
            else:
                x_range = (x + 1, self.x_1)
            if edge_type in (4, 6):
                z_range = (self.z_0, z - 1)
            else:
                z_range = (z + 1, self.z_1)

        elif edge_type in (8, 9, 10, 11):
            x_range, y, z = edge_dim_val

            if edge_type in (8, 9):
                y_range = (self.y_0, y - 1)
            else:
                y_range = (y + 1, self.y_1)
            if edge_type in (8, 10):
                z_range = (self.z_0, z - 1)
            else:
                z_range = (z + 1, self.z_1)

        else:
            raise ValueError(f"Edge invalid: {edge_type}")

        return self.limited_cutout(x_range, y_range, z_range)

    def cut_from_face(self, face_dim_val, face_type: int) -> Optional["Cube"]:
        # Cutout area from other cube face
        if face_type == 0:
            x, y_range, z_range = face_dim_val
            x_range = (self.x_0, x - 1)
        elif face_type == 1:
            x_range, y, z_range = face_dim_val
            y_range = (self.y_0, y - 1)
        elif face_type == 2:
            x_range, y_range, z = face_dim_val
            z_range = (self.z_0, z - 1)
        elif face_type == 3:
            x, y_range, z_range = face_dim_val
            x_range = (x + 1, self.x_1)
        elif face_type == 4:
            x_range, y, z_range = face_dim_val
            y_range = (y + 1, self.y_1)
        elif face_type == 5:
            x_range, y_range, z = face_dim_val
            z_range = (z + 1, self.z_1)
        else:
            raise ValueError(f"Face invalid: {face_type}")

        return self.limited_cutout(x_range, y_range, z_range)

    def limited_cutout(
        self, x_range: Tuple[int, int], y_range: Tuple[int, int], z_range: Tuple[int, int]
    ) -> Optional["Cube"]:
        # Make sure cutout does not enlarge cube
        x_range = (max(self.x_0, x_range[0]), min(self.x_1, x_range[1]))
        y_range = (max(self.y_0, y_range[0]), min(self.y_1, y_range[1]))
        z_range = (max(self.z_0, z_range[0]), min(self.z_1, z_range[1]))

        sub_cube = Cube(x_range=x_range, y_range=y_range, z_range=z_range, on=self.on_status)

        if not sub_cube.degenerate():
            return sub_cube

    def can_be_joined(self, other: "Cube") -> bool:
        other_faces = other.faces()
        return any(face in other_faces for face in self.faces(out=1))

    def join(self, other: "Cube") -> "Cube":
        other_faces = other.faces()
        face_type = next(i for i, face in enumerate(self.faces(out=1)) if face in other_faces)

        x_range, y_range, z_range = (self.x_0, self.x_1), (self.y_0, self.y_1), (self.z_0, self.z_1)

        if face_type == 0:
            x_range = (other.x_0, self.x_1)
        elif face_type == 1:
            y_range = (other.y_0, self.y_1)
        elif face_type == 2:
            z_range = (other.z_0, self.z_1)
        elif face_type == 3:
            x_range = (self.x_0, other.x_1)
        elif face_type == 4:
            y_range = (self.y_0, other.y_1)
        elif face_type == 5:
            z_range = (self.z_0, other.z_1)
        else:
            raise ValueError(f"Face invalid: {face_type}")

        return Cube(x_range=x_range, y_range=y_range, z_range=z_range, on=self.on_status)


class CubeSet:
    def __init__(self):
        self.cubes: List[Cube] = []

    def merge(self, target_cube: Cube) -> None:
        if not self.cubes and target_cube.on_status:
            self.cubes = [target_cube]
            return

        for cube in tuple(self.cubes):
            self.cubes.remove(cube)

            sub_cubes = cube.split(target_cube)
            sub_cubes = self.combine(sub_cubes)

            self.cubes.extend(sub_cubes)

        # If the based on cube was off, all the subcubes cut are the remainders of the current cube set. The remainders
        # here are all disjoint to the based on cube. If it was on, adding it completes the picture.
        if target_cube.on_status:
            self.cubes.append(target_cube)

    @staticmethod
    def combine(cubes: List[Cube]) -> List[Cube]:
        checked_all = False

        while not checked_all:
            checked_all = True

            for cube_1, cube_2 in combinations(cubes, 2):
                if cube_1.can_be_joined(cube_2):
                    joined = cube_1.join(cube_2)
                    cubes.remove(cube_1)
                    cubes.remove(cube_2)
                    cubes.append(joined)
                    checked_all = False
                    break

        return cubes

    def volume(self) -> int:
        return sum(cub.volume() for cub in self.cubes)


def calculate_solution(input_values: List[str]) -> int:
    cube_set = CubeSet()

    for rep in input_values:
        cube = Cube.from_rep(rep)
        cube = cube.limited_cutout((-50, 50), (-50, 50), (-50, 50))

        if cube:
            cube_set.merge(cube)

    return cube_set.volume()


if __name__ == "__main__":
    print(calculate_solution(get_input()))
