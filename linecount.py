def line_count(filename: str, lookup_value: str) -> int:
    """
    Counts the number of lines in a file. 
    If a lookup value is present, only counts lines that contain that value.
    If the file does not exist, returns -1.
    :param filename: name of the file to count lines from
    :param lookup_value: string value to lookup for within the file
    :return: number of lines matching the lookup value, or -1 if the file doesn't exist
    """
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
            count = 0
            for line in lines:
                if lookup_value in line:
                    count += 1
            return count
    except FileNotFoundError:
        return -1
