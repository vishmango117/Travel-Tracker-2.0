from PlaceCollection import PlaceCollection
from Places import Places
from A2src import MVCDemo

def main():
    travel_tracker = PlaceCollection()
    travel_tracker.load_places("src/places_base.csv")
    travel_tracker.print_list()

    

if __name__ == "__main__":
    #main()
    myapp = MVCDemo()
    myapp.run()