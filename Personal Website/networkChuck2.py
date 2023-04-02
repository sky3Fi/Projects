print("Hello, welcome to NetworkChuck Coffee!!!!!!!!!\n")

name = input("What is your name?\n")

if name == "Ben" :
    print(
    "You're not welcome here.  Get out Evil Ben!")
    exit()
else :
    print("Hello " + name + " ,thank you so much for coming in today. \n\n\n")

    order = input("Below are our current offerings:\n \n Sizes: Small, Medium or Large \n"
              " Flavors: French Vanilla, Chocolate, Carmel or Irish Cream \n Hot or Iced Coffee \n Hot or Iced Latte "
              "\n \n"
              "What would you like? \n")

çuantity = input("\nHow many " + order + "'s would you like? (Do not spell out the number please) \n")

price = 3

total = int(çuantity) * price

print("Excellent choice " + name + ". Your " + çuantity + " " + order + " will be ready in just a few minutes. \n")

print("Your total for " + çuantity + " " + order + " comes to $",total ,".")