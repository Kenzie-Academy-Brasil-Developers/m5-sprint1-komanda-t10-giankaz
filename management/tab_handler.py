from datetime import datetime

from utils import menu_reading


def product_finder (id):
    menu = menu_reading()
    for menu_item in menu:
        if (menu_item['id'] == id):
            return menu_item
    
    return 404



def total_calculator(consumed_products):
    subtotal = 0

    for n in consumed_products:
       id = n['id']
       amount = n['amount']
       product = product_finder(id)
       
       if (product == 404):
         return f'The id {id} was not found in our menu database'
    
       subtotal += (product['price'] * amount)

    bill = {'subtotal': subtotal, 'created_at': datetime.now().strftime("%d/%m/%Y, %H:%M:%S")}
    return bill

