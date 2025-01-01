import datetime
from threading import Lock

class Restaurant:
    def __init__(self, name, city, area, cuisine, cost_for_two, is_veg):
        self.name=name
        self.city=city
        self.area=area
        self.cuisine=cuisine
        self.cost_for_two=cost_for_two
        self.is_veg=is_veg
        self.time_slots={}
        self.lock=Lock()

    def update_time_slots(self, date, slots):
        with self.lock:
            self.time_slots[date]=slots
    
    def is_slot_available(self, date, slot):
        return date in self.time_slots and slot in self.time_slots[date] and self.time_slots[date][slot]>0
    

    def book_slot(self, date, slot):
        with self.lock:
            if self.is_slot_available(date, slot):
                self.time_slots[date][slot] -= 1
                return True
            return False
        

class RestaurantBookingSystem:
    def __init__(self):
        self.restuarants = []
    
    def resigter_restuarant(self, name, city, area, cuisine, cost_for_two, is_veg):
        restuarant = Restaurant(name, city, area, cuisine, cost_for_two, is_veg)
        self.restuarants.append(restuarant)
        return restuarant
    
    def search_restuarant(self, city=None, area=None, cuisine=None, name=None):
        results=self.restuarants
        if city:
            results = [c for c in results if c.city == city]
        if area:
            results = [c for c in results if c.area == area]
        if cuisine:
            results = [c for c in results if c.cuisine == cuisine]
        if name:
            results = [c for c in results if c.name == name]
        return results

    def book_table(self, restaurant, date, slot, no_of_people):
        if restaurant.book_slot(date, slot):
            return f"Booking successful for {no_of_people} people on {date} at {slot}."
        return "Booking failed. Slot unavailable."

if __name__ == "__main__":
    system=RestaurantBookingSystem()
    r1=system.resigter_restuarant("Rachit's Kitchen", "Bangalore", "HSR", "Chinese", 1500, True)
    r2=system.resigter_restuarant("Anshika Ki Rasoi", "Navi Mumbai", "Panvel", "Chinese", 3000, False)

    date = (datetime.datetime.now() + datetime.timedelta(days=1)).strftime("%Y-%m-%d")
    r1.update_time_slots(date, {"12:00 PM": 5, "1:00 PM": 5})
    r2.update_time_slots(date, {"12:00 PM": 3, "1:00 PM": 4})

    search_results=system.search_restuarant(cuisine="Chinese")
    for restaurant in search_results:
        print(f"Found: {restaurant.name} in {restaurant.area}, cuisine: {restaurant.cuisine}")

    booking_result=system.book_table(r1, date, "12:00 PM", 2)
    print(booking_result)