from typing import List

raw_input = """
6617113584
6544218638
5457331488
1135675587
1221353216
1811124378
1387864368
4427637262
6778645486
3682146745
"""


def get_input() -> List[List[int]]:
    return [[int(val) for val in list(line)] for line in raw_input.split("\n")[1:-1]]
