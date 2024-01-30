from src.utils.constants import characters
from src.utils.invalid_input_error import InvalidInputError


def is_valid_character(char):
    return char in characters


def is_valid_flow(flow):
    return all(is_valid_character(char) for char in flow)


""" This method calculates the sum of measurements in an inflow """
def get_inflow_value(flow, character_encoding, start, end):
    sum = 0
    while start <= end:
        sum = sum + character_encoding[flow[start]]
        start = start + 1
    return sum


""" This method finds the longest inflow string from a given index
and return the end index of the inflow """
def get_inflow_end_index(flow, multiple_sequence_char, inflow_start_index):
    inflow_end_index = inflow_start_index
    while (
        inflow_end_index < len(flow)
        and flow[inflow_end_index] == multiple_sequence_char
    ):
        inflow_end_index = inflow_end_index + 1
    if inflow_end_index == len(flow):
        raise InvalidInputError(
            flow,
            "contains a package with fewer characters than specified by package-size"
        )
    else:
        return inflow_end_index
