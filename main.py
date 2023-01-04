

def take_order():
  name = input("Hello welcome to order what should we call you")
  order = input("what would you like to order today " + name + " Choose from menue.")
  print("your order " + order + " has been sent to the kitchen")

def menue():
  print("our menue is being displayed now")
  print("""
  Menue
  ====================
  Lunch                |             Breakfast
 Pear salad
 Vegetable Playe                   Omlet
 French fries                      Tofu Scramble
 Applesuace                        Avacado toast
                                   French Fries
                                   Bluberry Pancakes
  Dinner
  Spinach Salad
  Baked Goat Cheese
  Mashed patatoes
  fennel coalsaw
  ______________________________________________________________
  
  """)
def specials():
  print("So you would like to know our menue specials for today")
  print("""
  Menue Specials
  _________________________
  Fish and chips
  Turkeypot pie
  Homemad Meatloaf
  grilled salmon
  Hawain Pizza
  Veggie Pizza
  Grilled Beef Tenderlain
  ________________________
  If you would like to order any of theese input them in the order section
  """)
def make_reservration():
  table = input("what table would you like to reserve a seat in")
  print("allright we will reserve your seat at table" + table)



def welcome():
    print("""
Welcome to out resturant chatbot I will offer you assistance with
any of your orders and any extra questions you would like to ask
 """)
    choices = input("""
    would you like to begin yes to yes or q to quit
    """)
    
    quit_character = "q"
    while choices.lower != quit_character:
      choice = input("""
    What do you want me to help you with
    1 Menue
    2 Todays Specails
    3 Make a reservration
    4 order
    """)
      
      if choice == quit_character:
        break
      elif choice == "1":
        menue()
      elif choice == "2":
        specials()
      elif choice == "3":
        make_reservration 
      elif choice == "4":
        take_order()
        break
      else:
        print("choose type in a number from the choices listed")

welcome()      
    