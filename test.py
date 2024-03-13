from shopping_system import *


shop = Shop()

client = Client(shop, initial_money=200)
client.put_in_basket(Product('Milk', 100))

shop.buy_products(client.basket(), client.money_amount())
print(shop.product_list())