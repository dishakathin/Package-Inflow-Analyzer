from src.utils.encoding import character_encoding
from src.utils.helper import get_inflow_end_index
from src.utils.helper import get_inflow_value
from src.utils.helper import is_valid_flow
from src.utils.invalid_input_error import InvalidInputError


"""Terminology
A Flow consists of a sequence of packages
Each Package consists of a sequence of inflows
Each inflow is a sequence of characters
First inflow of each package represents the package-size
All subsequent inflows represent measurements to be summed up
"""


class PackageInflowProcessor:
    def __init__(self):
        """ Requirements
        - self.character_encoding: encoding provided by encoding.py
        - self.multiple_sequence_char: 'z' is the character
          after which multiple sequence starts
        """
        self.character_encoding = character_encoding
        self.multiple_sequence_char = max(
            character_encoding, key=character_encoding.get
        )

    # This method processes the 'flow' obtained from the ACME BMS
    def process_input(self, flow):
        """
        This method takes a string 'flow' as input and
        return the list of total package inflows as output
        'inflow_start_index' and 'inflow_end_index' represent the inflow substring
        each inflow value is measured using 'get_inflow_value' method  
        maintain a 'counter' to count the number of inflows summedup so far
        when 'counter' reaches 'package_size',
        append the sum of inflows to the result list and start measuring the next package
        'find_package_size' is a boolean flag which identifies if the inflow value represents
        a package size or measurements to be summed up
        """

        total_package_inflows = []
        package_size, counter, package_inflow_sum = 0, 0, 0
        inflow_start_index = 0
        find_package_size = True

        if not is_valid_flow(flow):
            raise InvalidInputError(
                flow,
                "contains an invalid character"
            )

        # Assuming only lowercase
        flow = flow.lower()

        while inflow_start_index < len(flow):
            inflow_end_index = get_inflow_end_index(flow, self.multiple_sequence_char, inflow_start_index)
            inflow_sum = get_inflow_value(flow, character_encoding,
                                              inflow_start_index,
                                              inflow_end_index)
            if find_package_size:
                # Assumption: if package substring is '_' then we append null value to result
                if inflow_sum == 0:
                    total_package_inflows.append(None)
                else:
                    package_size = inflow_sum
                    counter = 0
                    find_package_size = False
            else:
                package_inflow_sum = package_inflow_sum + inflow_sum
                counter = counter + 1
                if counter == package_size:
                    total_package_inflows.append(package_inflow_sum)
                    package_inflow_sum = 0
                    find_package_size = True
            inflow_start_index = inflow_end_index + 1

        if counter < package_size:
            raise InvalidInputError(
                flow,
                "contains a package with fewer characters than specified by package-size"
            )
        
        return total_package_inflows
