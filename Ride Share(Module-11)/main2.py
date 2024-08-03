from user import Rider, Driver
from vehicles import Car, Bike, CNG
from ride_1 import Ride, RideRequest, RideMatching, RideSharing

niye_jao = RideSharing("Niye Jao")
rahim = Rider("Rahim Uddin", "rahim@gmail.com", 123654, "Mohakhali", 1000)
niye_jao.add_rider(rahim)
karim = Driver("Karim Uddin", "karim", 4567, "Gulshan")
niye_jao.add_driver(karim)
rahim.request_ride(niye_jao, "Uttara", 'bike')
karim.reach_destination(rahim.current_ride)
rahim.show_current_ride()
# print(niye_jao)