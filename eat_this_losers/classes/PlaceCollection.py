import csv
from Places import Place


class PlaceCollection():
    def __init__(self):
        self.collection = list()
        self.size = 0
        self.unvisited_counter = 0
    
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
            self.collection.append(Place(data[0],data[1],data[2], data[3]))
            self.collection[self.size].priority = int(self.collection[self.size].priority)
            self.size+=1
        file_read.close()

    def add_place(self, filename):
        (name, country, priority)=("Testing","Test123",12)
        place_obj = Place(name, country, priority)
        self.collection.append(place_obj)

    def save_places(self, filename):
        """ write_file(): FUNCTION TO WRITE TO CSV FILE
        WRITING IS DONE WHEN PROGRAM IS QUITTED OR ERR(KEYBOARD INTERRUPT)
        PARAMS: DICTIONARY(DICT), SIZE(INT), FILENAME(STRING)
        RETURN VALUE: NO VALUES ARE RETURNED"""

        # START OF FUNCTION
        fp = open(filename, 'w+')
        for i in range(0, self.size):
            print("{},{},{}".format(self.collection[i].name, self.collection[i].year, self.collection[i].cost, file=fp))
        print("{} places saved to {}".format(self.size, filename))
        fp.close()

    def get_unvisited(self):
        return self.unvisited_counter
    
    #def sort_function(self):

