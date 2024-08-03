from ride import Ride, RideMatching, RideRequest, RideSharing
from users import Rider, Driver
from vehicle import Car, Bike

niye_jao = RideSharing("Niye Jao")
rahim = Rider("Rahim", "rahim@gmail.com", 1234, "Mohakhali", 500)
niye_jao.add_rider(rahim)
karim = Driver("Karim", "karim@gmail.com", 1234, "Gulshan")
niye_jao.add_driver(karim)
rahim.request_ride(niye_jao, "Uttara", "car")
karim.reach_destination(rahim.current_ride) # current_ride holo ride class er object
rahim.show_current_ride()
# print(niye_jao)