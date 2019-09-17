import csv
from Places import Places


class PlaceCollection():

    def __init__(self):
        self.collection = list()
        self.size = 0
        self.unvisited_counter = 0

    def save_places(self, filename):

    def load_places(self, filename):
        """ load_places(): FUNCTION DESIGNED TO READ CSV FILES
        AND SET THEM INTO DICTIONARY
        SORTING IS DONE BASED ON THE LIST INSIDE DICTIONARY
        PARAMS: FILENAME(STRING)
        RETURN VALUE: DICTIONARY(DICT), SIZE(INT)"""

        # START OF FUNCTION
        # OPEN FILE
        try:
            file_read = open(filename, 'r')
        except FileNotFoundError:
            print("File Not Found")
            exit()
        file_row = csv.reader(file_read, delimiter=',')
        
        for data in file_row:
            #print(data[0], data[1], data[2])
            self.collection.append(Places(data[0],data[1],data[2], data[3]))
            self.collection[self.size].priority = int(self.collection[self.size].priority)
            self.size+=1
        file_read.close()

    def print_list(self):
        for i in range(self.size):
            print(self.collection[i])

    def add_place(self):
        self.root.ids.name_text

    def get_unvisited_places(self):
        return self.unvisited_counter