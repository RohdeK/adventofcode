from typing import Tuple

from puzzles.day_17.input_part_1 import get_input


def calculate_solution(hor: Tuple[int, int], vert: Tuple[int, int]) -> int:
    velocity_vectors = set()

    for i in range(hor[0], hor[1] + 1):
        for j in range(vert[0], vert[1] + 1):
            may_be_reached = True
            in_horizontal_fadeout_range = None
            fadeout_velocity = None
            n_steps = 0

            while may_be_reached:
                n_steps += 1

                if in_horizontal_fadeout_range is False:
                    # Overshooting horizontally
                    may_be_reached = False
                    continue

                if n_steps > 2 * abs(j):
                    # Overshooting on downfall
                    may_be_reached = False
                    continue

                if in_horizontal_fadeout_range is True:
                    # On fadeout - horizontal velocity is fixed
                    can_be_reached_in_n_steps_horizontally = True
                else:
                    # Check if is overshot when targetted with fadeout velocity.
                    steps_fadeout = (n_steps * (n_steps + 1)) // 2

                    if i == steps_fadeout:
                        # Hits the horizontal position on fadeout
                        in_horizontal_fadeout_range = True
                        fadeout_velocity = n_steps
                    elif steps_fadeout > i:
                        # Overshoots on fadeout - won't reach ever.
                        in_horizontal_fadeout_range = False

                    # Direct calculation of capability to be reached
                    if n_steps % 2 == 1:
                        can_be_reached_in_n_steps_horizontally = i % n_steps == 0
                    else:
                        can_be_reached_in_n_steps_horizontally = i % n_steps == n_steps // 2

                if not can_be_reached_in_n_steps_horizontally:
                    continue

                # Direct calculation of capability to be reached
                if n_steps % 2 == 1:
                    can_be_reached_in_n_steps_vertically = j % n_steps == 0
                else:
                    can_be_reached_in_n_steps_vertically = j % n_steps == n_steps // 2

                if not can_be_reached_in_n_steps_vertically:
                    continue

                if in_horizontal_fadeout_range:
                    # In case horizontal velocity is fixed - no calculation
                    init_velo_x = fadeout_velocity
                else:
                    # Calculation based on step count
                    init_velo_x = (i + (n_steps * n_steps - 1) // 2) // n_steps

                # Calculation based on step count
                init_velo_y = (j + (n_steps * n_steps - 1) // 2) // n_steps

                # Add velocity vector to set - note that one velocity vector can hit the target in multiple step counts.
                velocity_vectors.add((init_velo_x, init_velo_y))

    return len(velocity_vectors)


if __name__ == "__main__":
    print(calculate_solution(*get_input()))
