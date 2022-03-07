#You work for a retail store that wants to increase sales on Tuesday and Wednesday, 
# which are the store's slowest sales days. On Tuesday and Wednesday, if a customer's subtotal is $50 or greater, 
# the store will discount the customer's subtotal by 10%.

#Your program asks the user for the subtotal but does not ask the user for the day of the week. 
#Your program gets the day of the week from your computer's operating system.
#Your program correctly computes and prints the discount amount if applicable.
#Your program correctly computes and prints the sales tax amount and the total amount due.
'''
Add code to your program that the computer will execute if today is Tuesday or Wednesday and the customer is not purchasing 
enough to receive the discount. This added code should compute and print the difference between $50 and the subtotal which 
is the additional amount the customer would need to purchase in order to receive the discount.

Near the beginning of your program replace the code that asks the user for the subtotal with a loop that repeatedly asks the 
user for a price and a quantity and computes the subtotal. This loop should repeat until the user enters "0" for the price.
'''

from datetime import datetime
current_date = datetime.now()
weekday = current_date.weekday()  #0-6 Mon-Sun

discount = 0.10
sales_tax = 0.06
price = 1
customer_subtotal = 0

while price != 0:
    price = float(input('What is the price of your item? (Enter 0 when finished): '))
    if price != 0:
        quantity = float(input('What is the quantity of item? '))
        customer_subtotal += (price * quantity)

#customer_subtotal = float(input('Please enter your subtotal: '))
if weekday == 1 or weekday == 2 and customer_subtotal >= 50:
    customer_subtotal = customer_subtotal * (1-discount)
elif weekday == 1 or weekday == 2 and customer_subtotal <= 50:
    difference = 50 - customer_subtotal
    print(f'You are eligable for a 10% discount if you spend ${difference:.2f} more.    ')

final_sales_tax = customer_subtotal * sales_tax
total = customer_subtotal + final_sales_tax

print (f'Sales tax amount: ${final_sales_tax:.2f} ')
print (f'Your total is ${total:.2f}')