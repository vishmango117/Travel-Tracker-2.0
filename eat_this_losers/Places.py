"""CP1404 Programming-II Assignment-2 Travel Tracker 2.0
Places.py: File containing the class Place which comprises of
name, country, priority, visited as the instance variables
and methods like mark_visited(), mark_unvisited(), important_place()
"""

from operator import attrgetter


class Place:
    def __init__(self, name, country, priority, visited='n'):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited
    
    def __str__(self):
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
        self.visited = 'v'
    
    def mark_unvisited(self):
        self.visited = 'n'
    
    def important_place(self):
        return self.priority <= 2
    
    