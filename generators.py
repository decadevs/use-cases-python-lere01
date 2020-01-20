# Document at least 3 use cases of generators

"""
Generators are functions (expression/comprehension) that return lazy iterators which although are like lists do not 
store their content in memory. This makes generators useful when dealing extremely large files or infinite sequence. 
They are also commonly used to create data pipelines. One big advantage that they bring to the table is that they can 
be used in situations where we want to avoid memory error.
"""

# A generator to infinitly generate fibonacci numbers
def fibonacci(n):
    term_one, term_two = 0,1

    while True:
        yield term_one
        term_one, term_two = term_two, term_one + term_two


# A generator to read files from really large files
def read_file(csv_file):
    for row in open(csv_file, 'r'):
        yield row


# A data pipeline for creating column data dictionary from a csv file
def file_to_dictionary(csv_file):
    lines = (line for line in open(csv_file))
    line_items = (item.rstrip().split(",") for item in lines)
    list_of_columns = next(line_items)
    dictionaries = (dict(zip(list_of_columns, data)) for data in line_items)

    return dictionaries