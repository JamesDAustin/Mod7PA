# instructor-provided function
# copy and paste into your solution
def read_penguin_row(row_number):
    penguin_row = ""

    # open the CSV file and skip the header row
    with open("PalmerPenguins.csv", "r") as penguin_file:
        penguin_file.readline()

        current_row = 1

        # search for the requested data row
        for row in penguin_file:
            if current_row == row_number:
                penguin_row = row.strip()
                break

            current_row += 1

    # return the requested row as a string
    return penguin_row