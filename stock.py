products_information = input().split()

products_data_dict = {}

for index in range(0,len(products_information),2):

    product = products_information[index]
    quantity = products_information[index+1]
    products_data_dict[product] = quantity

searched_products = input().split()

for products in searched_products:
    if products in products_data_dict:
        print(f"We have {products_data_dict[products]} of {products} left")
    else:
        print(f"Sorry, we don't have {products}")
