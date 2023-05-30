
def count_lines(filename, lookup_value: str) -> int:
    """
    Counts the number of lines in the file.
    If a lookup value is present, only counts lines that contain that value.
    If the file does not exist, returns -1.
    :param: lookup_value: string value to lookup for within the file
    :return: int number of lines matching lookup value, or -1
    """
    # This try block run the code normally, and if no error occurs, it skips the code in the except block
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            if lookup_value:
                lines = [line for line in lines if lookup_value in line]
            return len(lines)

    # This except block handles the error when the file is not found
    except FileNotFoundError: 
        return -1


# Usage example
filename = "TopTechCompaniesInUsa.txt"
lookup_value = "Software Engineering Internship"
counter = count_lines(filename, lookup_value)

if counter == -1:
    print("File not found.")
else:
    print(f"Number of lines that contains '{lookup_value}' is {counter}")
