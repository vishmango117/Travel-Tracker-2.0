class Place:
    def __init__(self, name, country, priority, visited='n'):
        self.name = name
        self.country = country
        self.priority = priority
        self.visited = visited
    
    def __str__(self):
        if(self.visited == 'n'):
            return "Name: {} Country: {} Priority: {}".format(self.name, self.country, self.priority)
        elif(self.visited == 'v'):
            return "Name: {} Country: {} Priority: {} (visited)".format(self.name, self.country, self.priority)
    
    def mark_visited(self):
        self.visited = 'v'
    
    def mark_unvisited(self):
        self.visited = 'n'
    
    def important_place(self):
        return self.priority <= 2
    
    