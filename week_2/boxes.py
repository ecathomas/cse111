import math
items = int(input('Enter the number of items: '))
items_per_box = int(input('Enter the number of items per box: '))

def calculate_number_of_boxes() :
    return math.ceil(items / items_per_box)

def calculate_items_left_over() :
    return items % items_per_box

boxes = calculate_number_of_boxes()
last_box = calculate_items_left_over()

print(f'For {items} items, packing {items_per_box} in each box, you will need {boxes} boxes.')
if last_box != 0 :
    print(f'The last box will have {last_box} item(s).')

