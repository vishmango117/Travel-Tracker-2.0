from PlaceCollection import PlaceCollection
from app_gui import TravelTrackerApp

# Main function: Function to call the Kivy GUI app
# and send the PlaceCollection Object
def main():
    myapp = TravelTrackerApp(PlaceCollection())
    myapp.run()

if __name__ == "__main__":
    main()
