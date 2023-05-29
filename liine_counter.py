class LineCounter:

    def __init__(self, filename: str):
        self.filename = filename

    def count_lines(self, lookup_value: str) -> int:
        """
        Counts the number of lines in the file.
        If a lookup value is present, only counts lines that contain that value.
        If the file does not exist, returns -1.
        :param: lookup_value: string value to lookup for within the file
        :return: int number of lines matching lookup value, or -1
        """
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                if lookup_value:
                    lines = [line for line in lines if lookup_value in line]
                return len(lines)
        except FileNotFoundError: 
            return -1


# Usage example
filename = "TopTechCompaniesInUsa.txt"
counter = LineCounter(filename)
lookup_value = "Software Engineering Internship"
line_count = counter.count_lines(lookup_value)
if line_count == -1:
    print("File not found.")
else:
    print(f"Number of lines that contains '{lookup_value}' are {line_count}")
