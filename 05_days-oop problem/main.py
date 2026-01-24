class train:
    def __init__(self,name,fare,seat):
        self.name = name
        self.fare = fare
        self .seats =seat
    def get_status(self):
        print(f"{self.name} train {self.seats} no of seat")
    def get_fare_info(self):
        print(f"price is {self.fare}")
    def get_seat_status(self):
        if self.seats > 0:
            print("your seat is conform")
            print(f"seat no is {self.seats}")
            self.seats = self.seats-1
        else:
            print("there is no seats")
class passangewer(train):
     def showhunger(self):
         print("this passanger is not eatern")

a = train('rajdhani express',600,55) 
a.get_fare_info()
a.get_seat_status()
a.get_status()  
b =passangewer('rohan',688,33) 
b.showhunger()
b.get_fare_info()
b.get_seat_status()
b.get_status()  
