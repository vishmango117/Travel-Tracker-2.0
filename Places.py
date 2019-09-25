"""CP1404 Programming-II Assignment-2 Travel Tracker 2.0
Places.py: File containing the class Place which comprises of
name, country, priority, visited as the instance variables
and methods like mark_visited(), mark_unvisited(), important_place()
"""

from operator import attrgetter


class Place:
    def __init__(self, name, country, priority, visited='n'):
        """__init__(): Method that loads the Places on load
        calls the super classes __init__  function and sets the object."""

        # START OF FUNCTION
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited

    def __str__(self):
        """__str__(): Method that prints str on print object """

        # START OF FUNCTION
        if(self.visited == 'n'):
            return (
                "{} in {}, priority {}".format(self.name,
                                               self.country,
                                               self.priority))
        elif(self.visited == 'v'):
            return (
                "{} in {}, priority {} (visited)".format(self.name,
                                                         self.country,
                                                         self.priority))

    def mark_visited(self):
        """mark_visited(): function to set visited to v"""
        self.visited = 'v'

    def mark_unvisited(self):
        """mark_unvisited(): function to set visited to n"""
        self.visited = 'n'

    def important_place(self):
        """important_place(): function to return a boolean
        based on priority being less than equal to 2"""
        return self.priority <= 2

# DEVELOPMENT AND TESTING PURPOSES
# It allows individual testing of the files independently
if __name__ == "__main__":
    placeobj = Place("Lima", "Peru", 12)
    print(placeobj)
    placeobj.mark_visited()
    print(placeobj)
