import csv
def main():
    key_column_index = 0
    students = read_dict("students.csv", key_column_index)
    i_number = input("Please enter an I-Number (xxxxxxxxx) : ")
    
    if i_number in students:
        print (students[i_number])
    else: 
        print ("No such student")


def read_dict(filename, key_column_index):
    """Read the contents of a CSV file into a
    dictionary and return the dictionary.

    Parameters
        filename: the name of the CSV file to read.
    Return: a dictionary that contains
        the contents of the CSV file.
    """
    dictionary = {}
    
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list[1]
        return dictionary


if __name__ == "__main__":
    main()