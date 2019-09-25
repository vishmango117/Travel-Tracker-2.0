"""CP1404 Programming-II Assignment-2 Travel Tracker 2.0
PlaceCollection.py: file containing the class Placecollection
which consists of collection(list), size(int), unvisited_counter(int)
and methods like load_places(), add_place(), save_places(), get_unvisited()"""

import csv
from Places import Place
from operator import attrgetter


class PlaceCollection():

    def __init__(self):
        """ __init__():Function to build the placecollection object """

        # START OF FUNCTION
        self.collection = list()
        self.size = 0
        self.unvisited_counter = 0

    def load_places(self, filename):
        """ load_places(): method of placecollection designed to read csv files
        and send them into the list inside placeCollection"""

        # START OF FUNCTION
        try:
            file_read = open(filename, 'r')
        except FileNotFoundError:
            print("File Not Found")
            exit()
        file_row = csv.reader(file_read, delimiter=',')

        for data in file_row:
            self.collection.append(Place(data[0], data[1], data[2], data[3]))
            self.collection[self.size].priority = (int(
                self.collection[self.size].priority))
            if(self.collection[self.size].visited == 'n'):
                self.unvisited_counter += 1
            self.size += 1
        file_read.close()

    def add_place(self, name, country, priority):
        """add_place(): Method to add Place object to a list"""

        # START OF FUNCTION
        place_obj = Place(name, country, priority)
        self.collection.append(place_obj)
        self.size += 1
        self.unvisited_counter += 1

    def save_places(self, filename):
        """ write_file(): FUNCTION TO WRITE TO CSV FILE
        WRITING IS DONE WHEN PROGRAM IS QUITTED OR ERR(KEYBOARD INTERRUPT)
        PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
        RETURN VALUE: NO VALUES ARE RETURNED"""

        # START OF FUNCTION
        fp = open(filename, 'w+')
        for i in range(self.size):
            fp.write("{},{},{},{}\n".format(self.collection[i].name,
                                            self.collection[i].country,
                                            self.collection[i].priority,
                                            self.collection[i].visited))
        fp.close()

    def get_unvisited(self):
        return self.unvisited_counter
