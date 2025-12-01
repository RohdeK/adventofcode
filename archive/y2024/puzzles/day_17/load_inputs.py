from utils.input_deformatter import InputDeformatter

InputType = tuple[tuple[int, int, int], list[int]]


def parse_registers(regs: str) -> tuple[int, int, int]:
    reg_a, reg_b, reg_c = regs.split("\n")
    val_a, val_b, val_c = reg_a.split(": ")[1], reg_b.split(": ")[1],  reg_c.split(": ")[1]
    return int(val_a), int(val_b), int(val_c)


def parse_program(prog: str) -> list[int]:
    prog = prog.split("Program: ")[1]
    return [int(v) for v in prog.split(",")]


input_reader = InputDeformatter[InputType](
    input_primary_split="\n\n",
    cast_inner_type=[parse_registers, parse_program],
)
