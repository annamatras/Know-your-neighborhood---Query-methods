from locationList import LocationList
import sys
import csv


def read_from_csv(file):
    """reading data from csv file
        returns:
            data from file
    """
    with open(file) as f:
        next(f)
        data = []
        for line in csv.reader(f, delimiter='\t'):
            data.append(list(line))
    return data


def file_from_user():
    """Takes file name from user and checks if exists"""
    try:
        file = get_input("Please enter name of the file to get data from. For exit press 0: ")
        if file == "0":
            sys.exit()
        LocationList.add_location(read_from_csv(file))
    except FileNotFoundError:
        print("\nThis file wasn't found. Try again or press 0 to exit.\n")
        file_from_user()


def print_table(table, title_list):
    """Displays data in a formatted table
    Return:
        table
    """
    table.insert(0, title_list)
    for row_index, row in enumerate(table):
        for col_index, col in enumerate(row):
            if (type(col) == float) or (type(col) == int):
                table[row_index][col_index] = str("{0:,.2f}".format(col))
    widths = [max(map(len, col)) for col in zip(*table)]
    sum_of_widths = sum(widths) + len(table[0]) * 3 - 1
    for row in table:
        print("-" * sum_of_widths)
        print("|" + "  ".join((val.ljust(width) + "|" for val, width in zip(row, widths))))
    print("-" * sum_of_widths)


def printing(content):
    """Prints output"""
    print(content)


def get_input(user_input):
    """Takes input from user"""
    return input(user_input)


def display_menu():
    """Method display menu for users
        return:
                display string
    """
    print("""\nChoose option:
       (1) List statistics
       (2) Display 3 cities with longest names
       (3) Display county's name with the largest number of communities
       (4) Display locations, that belong to more than one category
       (5) Advanced search
       (0) Exit program""")
