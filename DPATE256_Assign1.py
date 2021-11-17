##
#Dhyey Patel
#250960470
#October 4th 2017
#Assignment 1: Coffee or Tea, I see
##

#define the needed constants 
SMALL =1.5
MEDIUM = 2.5
LARGE = 3.25
VANILLA = .25
CHOCOLATE = .75
MAPLE = .5
LEMON = .25
MINT = .5
TAXES = 1.11

#ask for name and then validate if to make sure the input will work
name = input("Enter your name please: ")
if not(name.isalpha()):
    exit("Error: Invalid Input!!!!! Sorry :(")
#ask for type of beverage and then validate if to make sure the input will work
type = input("What beverage would you like coffee or tea? ")
if not(type.lower()=="tea" or type.lower()=="coffee" or type.lower()=="t" or type.lower()=="c"):
    exit("Error: Invalid Input!!!!! Sorry :(")
#ask for size and then validate if to make sure the input will work
size = input("What size would you like; Small, Medium or Large? ")
if not(size.lower()=="small" or size.lower()=="medium" or size.lower()=="large" or size.lower()=="s" or size.lower()=="m" or size.lower()=="l"):
    exit("Error: Invalid Input!!!!! Sorry :(")

#Depending on the type of beverage ask for the flavours, and then validate them to make sure the input will work
if type[0].lower()=="c":
    printtype = "Coffee"
    flavour = input("What flavor would you like; none, chocolate, vanilla or maple? ")
    if not(flavour.lower()=="none" or flavour == "" or flavour.lower()=="c" or flavour.lower()=="v" or flavour.lower()=="m" or flavour.lower()=="chocolate" or flavour.lower()=="vanilla" or flavour.lower()=="maple" ):
        exit("Error: Invalid Input!!!!! Sorry :(")
elif type[0].lower()=="t":
    printtype = "Tea"
    flavour = input("What flavor would you like; none, lemon or mint? ")
    if not(flavour.lower()=="none" or flavour == "" or flavour.lower()=="l" or flavour.lower()=="m" or flavour.lower()=="mint" or flavour.lower()=="lemon"):
        exit("Error: Invalid Input!!!!! Sorry :(")

#Depending on the size of the beverage set cost to that value
if (size[0].lower()=="s"):
    cost = SMALL
    printsize = "Small"
elif (size[0].lower()=="m"):
    cost = MEDIUM
    printsize = "Medium"
elif (size[0].lower()=="l"):
    cost = LARGE
    printsize = "Large"

#Depedning on what flavour was ordered add the amount to the cost
printflavour = "None"
if flavour[0].lower()=="v":
    cost = cost+VANILLA
    printflavour = "Vanilla"
elif flavour[0].lower()=="c":
    cost = cost+CHOCOLATE
    printflavour = "Chocolate"
elif type[0].lower()=="c" and flavour[0].lower()=="m":
    cost = cost+MAPLE
    printflavour = "Maple"
elif flavour[0].lower()=="l":
    cost = cost+LEMON
    printflavour = "Lemon"
elif type[0].lower()=="t" and flavour[0].lower()=="m":
    cost = cost+MINT
    printflavour = "Mint"

# Add the takes to the final cost, and then round the number to two decimal places
cost = cost*TAXES
cost = round(cost,2)

# Print the statement, with all of the options, and the final cost after tax
print("For",name,"a",printsize,printtype+", Flavouring:",printflavour+", Cost: $"+ str(cost) )

