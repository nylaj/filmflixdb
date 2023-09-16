from database import Database
import time

exit = False
db = Database("filmflix.db", "tblFilms")

def resultPrettifier(fields, results):
    print("RESULTS")
    header = ""
    for each_field in fields:
        if each_field != fields[len(fields) - 1]:
            header += f"{each_field}, "
        else:
            header += each_field
    print(header)
    for each_entry in results:
        record = ""
        for each_cell in each_entry:
            if each_cell != each_entry[len(each_entry) - 1]:
                record += f"{each_cell}, "
            else:
                record += f"{each_cell}"
        print(record)
    print("----END----")
    time.sleep(2)

def reportMenu(db = None):
    exit = False
    while exit != True:
        print("""1. Print details of all films
2. Print all films of a particular genre
3. Print all films of a particular year
4. Print all films of a particular rating
5. Exit
""")
        try:
            report_choice = int(input("Type your desired action's number >> "))
            match report_choice:
                case 1:
                    resultPrettifier(db.getTableFields(), db.printAllRecords())
                    exit = True
                case 2:
                    chosen_genre = input("Type your desired genre >> ")
                    resultPrettifier(db.getTableFields(), db.selectRecords(f"WHERE genre = '{chosen_genre}'"))
                    exit = True
                    pass
                case 3:
                    chosen_year = input("Type your desired year >> ")
                    resultPrettifier(db.getTableFields(), db.selectRecords(f"WHERE year = {chosen_year}"))
                    exit = True
                    pass
                case 4:
                    chosen_rating = input("Type your desired rating >> ")
                    resultPrettifier(db.getTableFields(), db.selectRecords(f"WHERE rating = '{chosen_rating}'"))
                    exit = True
                case 5:
                    exit = True
                case _:
                    print("Invalid option.")
        except ValueError:
            print("Input must be a number.")


while exit != True:
    print("""Filmflix Command Line Interface
    1. Add a Record
    2. Delete a Record
    3. Amend a Record
    4. Reports
    5. Print Table
    6. Quit""")
    try:
        choice = int(input("Type your desired action's number >> "))
        match choice:
            case 1:
                try:
                    values = input("Insert your data in the following order and form: (filmID, \"title\", yearReleased, \"rating\", duration, \"genre\")\n>> ")
                    db.addRecord(values)
                except:
                    print("Syntax is incorrect!")
            case 2:
                try:
                    recordID = int(input("Type the ID of the record you want to delete >> "))
                    db.deleteRecords(f"WHERE filmID = {recordID}")
                except ValueError:
                    print("Not a number!")
            case 3:
                print(f"Relevant fields: {db.getTableFields()}")
                fields = input("Type the fields and values you wanted to change, like this: column1 = \"value1\", column2 = value2, ...\n>> ")
                condition = input("Type your condition, like ID\n>> ")
                command = f"{fields} WHERE {condition}"
                db.updateRecords(command)
            case 4:
                reportMenu(db)
            case 5:
                resultPrettifier(db.getTableFields(), db.printAllRecords())
            case 6:
                print("Exiting...")
                exit = True
            case _:
                print("Not a valid option!")
    except ValueError:
        print("Input must be a single number!")
