from PlaceCollection import PlaceCollection
from Places import Places
from app_gui import MVCDemo


    

if __name__ == "__main__":
    myapp = MVCDemo()
    myapp.run()
    travel_tracker = PlaceCollection()
    travel_tracker.load_places("src/places_base.csv")
    myapp = MVCDemo()
    for i in range(travel_tracker.size):
        myapp.create_widgets(travel_tracker.collection[i].name, travel_tracker.collection[i].country, travel_tracker.collection[i].priority)