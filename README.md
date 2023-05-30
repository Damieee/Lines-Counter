# Lines-Counter

This is a Python program that counts the number of lines in a file, with the option to only count lines that contain a specific lookup value. If the file does not exist, `it returns -1`.

## Usage
To use this program, follow these steps:

- Ensure you have Python installed on your system.
- Provide the filename parameter with the path to the file you want to analyze.
- Optionally, provide the lookup_value parameter if you want to count lines that contain a specific value.
- Run the program.
- The program will display the number of lines that match the lookup value or show a `File not found` message if the file does not exist.

## Code Explanation
The main function in this program is count_lines, which takes the `filename` and `lookup_value` as parameters and returns the count of lines matching the lookup value or `-1` if the file is not found.

### Inside the function:

- A try block is used to handle exceptions. It attempts to open the file and read its contents.
- If the file is found, the lines are read, and optionally, the lines that contain the lookup value are filtered.
- The function returns the count of lines that match the lookup value.
- If a `FileNotFoundError` occurs, the except block is executed, and the function returns -1.
- The code includes a usage example where you can modify the filename and `lookup_value` variables to analyze different files and lookup values. The program prints the result based on the count of lines returned by the count_lines function.