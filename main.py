from classes import COD
import datetime 

class COD(object):
    def __init__(self, title, map, gun, skin, lethal):
        self.title = title 
        self.map = map
        self.gun = gun
        self.skin = skin
        self.lethal = lethal 

    def enter_data(self):
        self.title = input("Please enter favourite COD Game: ")
        self.map = input("COD Map: ")
        self.gun = input("COD Gun: ")
        self.skin = input("COD Skin: ")
        self.lethal = input("COD Lethal: ")

    def print_data(self):
        print("Your favourite COD Game is: " + self.title)
        print("Your favourite COD Map is : " + self.map)
        print("Your favourite COD Gun is : " + self.gun)
        print("Your favourite COD Skin is : " + self.skin)
        print("Your favourite COD Lethal is: " + self.lethal)


a = COD()
L = []


a.enter_data() 
L.append(a)












# class booking_system: 
#     def __init__(self):
#         self.bookings



# # def mainprompt():
# #     print("Welcome MK Motorsports")
# #     booking_choice = input("Would you like to book a service with us?\nPlease type Y or N")
# #     if booking_choice == "Y" or "y":
# #         return 

# # def booking_sys(booking_choice,):
# #     if booking_choice == "Y" or "y":
# #         return 


# # mainprompt()
# # booking_sys()

