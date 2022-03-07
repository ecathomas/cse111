import csv
PRODUCT_NUMBER_INDEX = 0
PRODUCT_QUANTITY_INDEX = 1
PRODUCT_PRICE_INDEX = 2

def main():
    key_column_index = 0
    products = read_dict("products.csv", key_column_index)
    print (products)
    print()
    print ('Requested Items')
    with open ('request.csv', "rt") as csv_file:
        request = csv.reader(csv_file)
        next(request)
        for row_list in request:
            product_number = row_list[PRODUCT_NUMBER_INDEX]
            quantity = int(row_list[PRODUCT_QUANTITY_INDEX])
            if product_number in products :
                product = products[product_number]
                name = product[1]
                price = float(product[2])
                print(f'{name}: {quantity} @ ${price}')
    

def read_dict(filename, key_column_index):
    dictionary = {}
    with open (filename, "rt") as csv_file:
        reader = csv.reader(csv_file)
        next(reader)
        for row_list in reader:
            key = row_list[key_column_index]
            dictionary[key] = row_list
        return dictionary



if __name__ == "__main__":
    main()