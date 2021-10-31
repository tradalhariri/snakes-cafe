def printWelcome():
    print("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
""")
def printMenu():
    for i in menu:
        print(i)
        print("-"*len(i))
        for j in menu[i]:
            print(j)
        print()
    print("""
***********************************
** What would you like to order? **
***********************************
    """)

menu = {"Appetizers":["Wings","Cookies","Spring Rolls",],
"Entrees":["Salmon","Steak","Meat Tornado","A Literal Garden",],
"Desserts":["Ice Cream","Cake","Pie"],
"Drinks":["Coffee","Tea","Unicorn Tears"]
}
menuContent = {}
def fillMenuContent():
    for i in menu:
        for j in menu[i]:
            menuContent[j]=0


            
def makeOrder():
    orderInput = input("> ")
    while orderInput!="quit":
        if orderInput in menuContent:
            menuContent[orderInput]+=1
            print(f"** {menuContent[orderInput]} order of {orderInput} have been added to your meal **")

        else:
            print("** Your choice not found ,please choose from the menu above. **")
        orderInput = input("> ")
    
    if orderInput == "quit":
        print("** You choosed the following : **")
        for i in menuContent:
            if menuContent[i] > 0:
                print(f"** {menuContent[i]} order of {i}  **")


            
  
       
printWelcome()
printMenu()
fillMenuContent()
makeOrder()