from classes import booking 

def menu():
    choice = input("Welcome to MK Motorsports!" + "\n" "Would you like to book a service?" + "\n" "Type Y or N: ")
    if choice == "Y" or choice == "y":
        print("Thanks for choosing us")
        return booking_service == True
    elif choice == "N" or choice == "n":
        print("Thank you for visiting us!")
    else: 
        print("Invalid Input")
        
# def booking_system():
#     if booking_service == True:
#         input("")






booking_service = True
menu()
booking_input()














# from classes import Gun

# Galil = Gun("Galil", "Rifle", "Automatic", 30)
# AK47 = Gun("AK47", "Rifle", "Automatic", 30)
# AWP = Gun("AWP", "Sniper", "Bolt Action", 6)
# print(AWP.select_fire)
# print(AWP.is_a_sniper())

# from classes import COD




# from classes import COD
# import datetime 

# class COD(object):
#     def __init__(self, title, map, gun, skin, lethal):
#         self.title = title 
#         self.map = map
#         self.gun = gun
#         self.skin = skin
#         self.lethal = lethal 

#     def enter_data(self):
#         self.title = input("Please enter favourite COD Game: ")
#         self.map = input("COD Map: ")
#         self.gun = input("COD Gun: ")
#         self.skin = input("COD Skin: ")
#         self.lethal = input("COD Lethal: ")

#     def print_data(self):
#         print("Your favourite COD Game is: " + self.title)
#         print("Your favourite COD Map is : " + self.map)
#         print("Your favourite COD Gun is : " + self.gun)
#         print("Your favourite COD Skin is : " + self.skin)
#         print("Your favourite COD Lethal is: " + self.lethal)


# a = COD()
# L = []


# a.enter_data() 
# L.append(a)












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

