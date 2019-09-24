from PlaceCollection import PlaceCollection
from app_layout import TravelTrackerApp


# Main function: Function to call the Kivy GUI app
# and send the PlaceCollection Object
def main():
    try:
        my_dict = PlaceCollection()
        myapp = TravelTrackerApp(my_dict)
        myapp.run()
    except KeyboardInterrupt:
        myapp.on_stop()

if __name__ == "__main__":
    main()
