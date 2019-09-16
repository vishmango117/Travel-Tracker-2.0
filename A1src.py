""" CP1404 Assignment 1 Travel Tracker 1.0
 Prepared By: Vishal Manghnani 13759845
 Github Repository(Primary) : https://github.com/vishmango117/CP1404-A1
 GithubRepo(Auxillary):https://github.com/JCUS-CP1404/jcus-cp1404-assg1-vishmango117
 """

# IMPORTING SYSTEM LIBRARIES
import csv
from operator import itemgetter
from os import system, name
from time import sleep


# ================ FILE OPERATIONS & SORTING ========================


def write_file(dictionary, size, filename):
    """ write_file(): FUNCTION TO WRITE TO CSV FILE
    WRITING IS DONE WHEN PROGRAM IS QUITTED OR ERR(KEYBOARD INTERRUPT)
    PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
    RETURN VALUE: NO VALUES ARE RETURNED"""

    # START OF FUNCTION
    fp = open(filename, 'w')
    for i in range(size):
        print("{},{},{},{}"
              .format(dictionary[i][0],
                      dictionary[i][1], dictionary[i][2],
                      dictionary[i][3]), file=fp)
    print("{} places saved to {}".format(size, filename))
    fp.close()


def read_file(filename):
    """ read_file(): FUNCTION DESIGNED TO READ CSV FILES
    AND SET THEM INTO DICTIONARY
    SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
    PARAMS: FILENAME(STRING)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    destination = dict()
    size = 0
    unvisited_counter = 0
    # OPEN FILE
    try:
        file_read = open(filename, 'r')
    except FileNotFoundError:
        print("File Not Found")
        exit()
    file_row = csv.reader(file_read, delimiter=',')
    for data in file_row:
        destination[size] = data
        size += 1
        if data[3] == "n":
            unvisited_counter += 1
    print("{} places loaded from {}".format(size, filename))
    file_read.close()

    # typecasting priority to int
    for i in range(size):
        destination[i][2] = int(destination[i][2])

    return (destination, size, unvisited_counter)


def sorting_engine(dictionary, size):
    """sorting_engine(): PROGRAM TO SORT ELEMENTS
    SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
    PARAMS: DICTIONARY(DICT), SIZE(INT)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    unsorted_list = []
    for index in range(size):
        unsorted_list.append(dictionary[index])
    # sort based on unvisited then priority using itemgetter
    unsorted_list.sort(key=itemgetter(3, 2))
    for index in range(size):
        dictionary[index] = unsorted_list[index]
    return (dictionary, size)


# ========================= PROGRAM'S PRIMARY FUNCTIONS =======================


def list_places(dictionary, size):
    """list_places(): FUNCTION IS USED TO THE LIST ALL THE PLACES
    LISTING OF ALL THE PLACES IS DONE AND CHECKING WHICH OF THOSE PLACES ARE
    PARAMS: DICTIONARY(DICT), SIZE(INT)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    max_length_city = 0
    max_length_country = 0
    unvisited_counter = 0
    for i in range(size):
        max_length_city = max(max_length_city, len(dictionary[i][0]))
        max_length_country = max(max_length_country, len(dictionary[i][1]))
        if(dictionary[i][3] == 'n'):
            unvisited_counter += 1
    for i in range(size):
        if(dictionary[i][3] == 'v'):
            print(" {0}. {1}{2} in {3}{4} priority {5}".format(i+1,
                  dictionary[i][0],
                 ' '*(max_length_city-len(dictionary[i][0])),
                  dictionary[i][1],
                  ' '*(max_length_country-len(dictionary[i][1])),
                  dictionary[i][2]))
        elif(dictionary[i][3] == 'n'):
            print("*{0}. {1}{2} in {3}{4} priority {5}".format(i+1,
                  dictionary[i][0],
                 ' '*(max_length_city-len(dictionary[i][0])),
                  dictionary[i][1],
                  ' '*(max_length_country-len(dictionary[i][1])),
                  dictionary[i][2]))
    if(unvisited_counter == 0):
        print("{} places. No places left to visit. Why not add a new place?"
              .format(size))
    else:
        print("{} places. You still want to visit {} places."
              .format(size, unvisited_counter))


def add_place(dictionary, size, unvisited_counter):
    """add_place(): FUNCTION TO ADD PLACES TO THE DICTIONARY
    WE ERROR CHECK AND VALIDATE THEN ADD PLACE TO THE DICTIONARY
    PARAMS: DICTIONARY(DICT), SIZE(INT)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    # ADDING PLACE NAME
    flag = True
    while flag:
        name = input("Name: ")
        if(name == ''):
            print("Input cannot be blank")
        elif(not(name.isalpha())):
            print("Invalid Name Try Again")
        else:
            flag = False

    # ADDING PLACE'S COUNTRY
    flag = True
    while flag:
        country = input("Country: ")
        if(country == ''):
            print("Input cannot be blank")
        elif(not(country.isalpha())):
            print("Invalid Country Try Again")
        else:
            flag = False

    # ADDING PLACE'S PRIORITY TO TRAVEL
    flag = True
    while flag:
        try:
            priority = int(input("Priority: "))
            if(priority <= 0):
                print("Number must be > 0")
            else:
                flag = False
        except ValueError:
            print("Invalid input; enter a valid number")

    # GENERATING LIST CONTAINING NAME, COUNTRY, PRIORITY AND VISIT
    newplace = [name, country, priority, 'n']
    print("{} in {} (priority {}) added to Travel Tracker"
          .format(name, country, priority))

    # ADDING TO DICTIONARY
    dictionary[size] = newplace
    size += 1
    unvisited_counter += 1

    # SORTING THE DICTIONARY
    (dictionary, size) = sorting_engine(dictionary, size)
    return (dictionary, size, unvisited_counter)


def mark_visited(dictionary, size, unvisited_counter):
    """mark_visited(): FUNCTION TO MARK THE PLACES AS VISITED
    UPDATES THE PLACES UNVISITED TO VISITED OF SELECTED LOCATION
    PARAMS: DICTIONARY(DICT), SIZE(INT)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    flag = True
    # CHECK IF ALL PLACES ARE VISITED
    if(unvisited_counter == 0):
        print("No unvisited places")
        return (dictionary, size, unvisited_counter)
    else:
        # PRINTING LISTS
        list_places(dictionary, size)
        print("Enter the number of place to mark as visited")
    # ASSUMING ALL PLACES ARE NOT VISITED
        while flag:
            try:
                submenuoption = int(input(">>>"))
                if (submenuoption <= 0):
                    print("Number must be > 0")
                elif(not(submenuoption <= size)):
                    print("Invalid place number")
                elif(dictionary[submenuoption-1][3] == 'v'):
                    print("That place has already been visited")
                else:
                    dictionary[submenuoption-1][3] = 'v'
                    print("{} in {} visited!"
                          .format(dictionary[submenuoption-1][0],
                                  dictionary[submenuoption-1][1]))
                    unvisited_counter -= 1
                    flag = False
            except ValueError:
                print("Invalid input; enter a valid number")
        # SORTING TO MAKE UPDATES BASED ON NEW VALUES
        (dictionary, size) = sorting_engine(dictionary, size)
    return (dictionary, size, unvisited_counter)


# ======================= MAIN & MENU ======================================


def main():
    """main(): MAIN FUNCTION TO CALL ALL OTHER FUNCTIONS
    PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    system("clear")
    try:
        print("Travel Tracker V1.0 - by Vishal Manghnani")
        dictionary = dict()
        size = 0
        counter = 0
        (dictionary, size, unvisited_counter) = read_file("csv/places.csv")
        (dictionary, size, unvisited_counter) = menu(dictionary,
                                                     size, unvisited_counter)
        print(size)
        write_file(dictionary, size, 'csv/places.csv')
        print("Have a nice day :)")
        sleep(2.0)

    except KeyboardInterrupt:
        size = len(dictionary)
        print("Program Halted writing changes to file")
        write_file(dictionary, size, 'csv/places.csv')
        print("Have a nice day :)")
        sleep(2.0)

    system("clear")


def menu(dictionary, size, counter):
    """menu(): FUNCTION TO SHOW THE PROGRAM MENU
    PARAMS: DICTIONARY(DICT), SIZE(INT)
    RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

    # START OF FUNCTION
    flag = True
    while flag:
        print("Menu:")
        print("L - List places")
        print("A - Add new place")
        print("M - Mark place as visited")
        print("Q - Quit")
        menuoption = input(">>>")
        if(menuoption == "L" or menuoption == "l"):
            list_places(dictionary, size)
        elif(menuoption == "A" or menuoption == "a"):
            (dictionary, size, counter) = add_place(dictionary, size, counter)
        elif(menuoption == "M" or menuoption == "m"):
            (dictionary, size, counter) = mark_visited(dictionary, size,
                                                       counter)
        elif(menuoption == "q" or menuoption == "Q"):
            flag = False
        else:
            print("Invalid Menu Choice")
    return (dictionary, size, counter)


# CALLING MAIN FUNCTION
if __name__ == "__main__":
    main()
