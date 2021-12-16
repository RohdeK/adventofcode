from typing import List, Optional, Tuple

from puzzles.day_16.input_part_1 import get_input


class BITS:
    version_bit_start = 0
    version_bit_size = 3
    type_bit_start = 3
    type_bit_size = 3
    literal_content_start = 6
    literal_chunk_length = 5
    operator_length_type_start = 6
    operator_length_start = 7
    operator_length_type_0_size = 15
    operator_length_type_1_size = 11
    operator_content_type_0_start = 22
    operator_content_type_1_start = 18

    def __init__(self, hex_rep: Optional[str] = None, binary_rep: Optional[str] = None):
        assert (hex_rep and not binary_rep) or (binary_rep and not hex_rep)

        if hex_rep:
            self._bin_rep = self._convert(hex_rep)
        else:
            self._bin_rep = binary_rep

        self.literal_content: Optional[int] = None
        if self.is_literal:
            self.literal_content, self.content_end_index = self._literal_content()

        self.operator_packages: List["BITS"] = []
        if self.is_operator:
            self.operator_packages, self.content_end_index = self._find_sub_packages()

    def __repr__(self):
        desc = "Literal" if self.is_literal else "Operator"
        return f"{desc}: {self._bin_rep}"

    @staticmethod
    def _convert(hex_rep: str) -> str:
        return "".join(f"{int(digit, base=16):04b}" for digit in list(hex_rep))

    def _int_from_positions(self, start: int, length: int) -> int:
        return int(self._bin_rep[start : (start + length)], base=2)

    @property
    def version(self) -> int:
        return self._int_from_positions(self.version_bit_start, self.version_bit_size)

    @property
    def is_operator(self) -> bool:
        return not self.is_literal

    @property
    def is_literal(self) -> bool:
        return self.type == 4

    @property
    def type(self) -> int:
        return self._int_from_positions(self.type_bit_start, self.type_bit_size)

    @property
    def exceeds_content(self) -> bool:
        return self.content_end_index < len(self._bin_rep)

    def _literal_content(self) -> Tuple[List[int], int]:
        literal_number_content = []
        out_of_content = False
        starting_pos = self.literal_content_start

        int_break = int("1" + "0" * (self.literal_chunk_length - 1), base=2)

        # Part 1: Reading content
        while not out_of_content:
            next_chunk = self._int_from_positions(starting_pos, self.literal_chunk_length)

            if next_chunk >= int_break:
                literal_number_content.append(next_chunk - int_break)
            else:
                out_of_content = True
                literal_number_content.append(next_chunk)

            starting_pos += self.literal_chunk_length

        # Part 2: Finding content end index
        total_content_bit_length = len(literal_number_content) * self.literal_chunk_length
        # Including header
        total_content_bit_length += self.type_bit_size + self.version_bit_size

        # expected_hex_rep_leftover_bits = total_content_bit_length % 4
        #
        # if expected_hex_rep_leftover_bits > 0:
        #     expected_hex_rep_leftover_bits = 4 - expected_hex_rep_leftover_bits
        #
        # content_end_position = starting_pos + expected_hex_rep_leftover_bits

        return literal_number_content, total_content_bit_length

    def _find_sub_packages(self) -> Tuple[List["BITS"], int]:
        length_type = self._int_from_positions(self.operator_length_type_start, 1)

        if length_type == 0:
            return self._find_sub_packages_content_type_0()
        else:
            return self._find_sub_packages_content_type_1()

    def _find_sub_packages_content_type_0(self) -> Tuple[List["BITS"], int]:
        sub_packages_bit_length = self._int_from_positions(self.operator_length_start, self.operator_length_type_0_size)
        operator_content_type_0_end = self.operator_content_type_0_start + sub_packages_bit_length

        sub_content_bit_string = self._bin_rep[self.operator_content_type_0_start : operator_content_type_0_end]

        packages, _ = self._find_sub_packages_from_binary(sub_content_bit_string)

        return packages, operator_content_type_0_end

    def _find_sub_packages_content_type_1(self) -> Tuple[List["BITS"], int]:
        sub_package_count = self._int_from_positions(self.operator_length_start, self.operator_length_type_1_size)

        sub_content_bit_string = self._bin_rep[self.operator_content_type_1_start :]

        packages, end_pos = self._find_sub_packages_from_binary(sub_content_bit_string, stop_after=sub_package_count)

        assert end_pos > 0

        return packages, self.operator_content_type_1_start + end_pos

    @staticmethod
    def _find_sub_packages_from_binary(binary_encoding: str, stop_after=0) -> Tuple[List["BITS"], int]:
        keep_searching = True
        out_bits: List[BITS] = []
        stop_after_position = 0
        dissected_binary_encoding = binary_encoding

        while keep_searching:
            if not dissected_binary_encoding:
                break

            next_bit = BITS(binary_rep=dissected_binary_encoding)

            if stop_after > 0:
                if len(out_bits) == stop_after - 1:
                    # Just let the rest be added to the out bits
                    keep_searching = False
                else:
                    # There should be more bits, continue with leftover binary rep.
                    dissected_binary_encoding = next_bit.cut_excess()

                stop_after_position += next_bit.content_end_index
            else:
                if next_bit.has_excess():
                    # There may be more bits
                    dissected_binary_encoding = next_bit.cut_excess()
                else:
                    keep_searching = False

            out_bits.append(next_bit)

        return out_bits, stop_after_position

    def has_excess(self) -> bool:
        return self.exceeds_content

    def cut_excess(self) -> str:
        if not self.has_excess():
            raise RuntimeError("Excess expected but not present.")

        excess = self._bin_rep[self.content_end_index :]

        self._bin_rep = self._bin_rep[: self.content_end_index]

        return excess


def calculate_solution(input_values: str) -> int:
    bitrep = BITS(hex_rep=input_values)

    version_numbers = bitrep.version

    version_numbers += sum_sub_versions(bitrep)

    return version_numbers


def sum_sub_versions(bits: BITS) -> int:
    sub_version_sum = 0

    for sub_bit in bits.operator_packages:
        sub_version_sum += sub_bit.version
        sub_version_sum += sum_sub_versions(sub_bit)

    return sub_version_sum


if __name__ == "__main__":
    print(calculate_solution(get_input()))
