from PlaceCollection import PlaceCollection
from app_gui import TravelTrackerApp

# Main function: Function to call the Kivy GUI app
# and send the PlaceCollection Object
def main():
    """main(): The main function for the entire program
    which build run the GUI and builds the Place collection object"""
    myplaceobj = PlaceCollection()
    myapp = TravelTrackerApp(myplaceobj)
    myapp.run()

if __name__ == "__main__":
    main()
