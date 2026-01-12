class Rider:
    def __init__(self,name):
        self.name=name
        self.destination = None
        self.current_location = None
        self.vehicle_type = None

    def request_ride(self,driver):
        self.destination=input("Enter your destination(A,B,C): ").upper()
        self.vehicle_type=input("select vehicle type (car,motercycle): ").lower()
        driver.accept_ride(self)

class Driver:
    def __init__(self,name):
        self.name = name
        self.current_locatio = None

    def accept_ride(self,rider):
        print(f"Rider accepted: {rider.name} destination: {rider.destination}")
        print(f"vehicle type : {rider.vehicle_type}")
        print("Ride in progress.............")

        # fare calculation
        fare = self.calculate_fare(rider.destination,rider.vehicle_type)
        print(f"your fare for this ride is: ${fare}")

    def calculate_fare(self,destination,vehicle_type):
        fare_map = {
            'A': {'car':10 ,'motercycle':8},
            'B': {'car':15 ,'motercycle':13},
            'C': {'car':20 ,'motercycle':18}
        }    
        return fare_map.get(destination,{}).get(vehicle_type,0)
    
location = {'A':"location A",'B':"location B",'C':"location C"}
rider_name =input("Entyer your name: ")
rider=Rider(rider_name)

driver_name=input("Enter driver name: ")
driver = Driver(driver_name)

print("Available location: ")
for loc_key,loc_value in location.items():
    print(f"{loc_key}.:{loc_value}")

print("Available vehicle type: car,motercycle")
rider.current_location =input("Enter your current location (A,B,C): ").upper()
driver.current_location =input("Enter drivers current location (A,B,C): ").upper()

rider.request_ride(driver)