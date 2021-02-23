# this program simulates the software at a restaurant for calculating the total price of items ordered, including tip 
# and tax

import pandas as pd
from IPython.display import display

#creating and displaying the menu to the user before their order is taken
menu = ['hamburger', 'cheeseburger', 'hotdog', 'fries', 'soda', 'chicken sandwich', 'corndog', 'milkshake', 'nachos']
prices = [3.00, 3.50, 2.50, 3.00, 1.50, 4.00, 2.00, 3.00, 5.00]
m = {'Items': menu, 'Prices': prices}
df = pd.DataFrame(m)
display(df)


def Order():
    items = []
    start = input('Hello! Would you like to order something to eat? ').lower() #answer either yes or no
    while True:
        if start == 'no':
            break
        order = input('What would you like to order? ') #answer with name of item previously displayed on menu, or quit to exit
        if order == 'quit':
            break
        else:
            items.append(order)
            order_again = input('Would you like anything else? ') #answer either yes or no
            if order_again == 'no':
                break
            else:
                continue
    return items


def Total_Price(items, tax):
    
    sub_total = 0
    for i in items:
        if i in menu:
            sub_total = sub_total + prices[menu.index(i)]
            
    ask_tip = input('Would you like to add a tip? ') #answer either yes or no
    
    while True:
        if ask_tip == 'yes':
            tip = float(input('How much would you like to tip? ')) #answer with a number
            while True:
                if tip < 0:
                    print('You cannot tip a negative amount. Please enter a different tip. ') #answer with a number
                    tip = float(input('How much would you like to tip? ')) #answer with a number
                else: break
            
            sub_total = sub_total + tip
            break
        else: break
    #combining sub total and tax, and then rounding it to the nearest hundredth of a cent
    total = sub_total * (1 + .01 * tax)
    total = round(total, 2)
    print('Your total is $'+str(total))
    

Total_Price(Order(), 7.75)