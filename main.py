from modules.client import Client

client = Client("Agustin", "Carrillo", 24, [])

print(client)

client.view_products()

client.add_to_cart(1)
client.add_to_cart(1)
client.add_to_cart(3)
client.add_to_cart(3)
client.add_to_cart(5)
client.add_to_cart(7)
client.add_to_cart(9)

client.view_cart()
print()

client.remove_from_cart(1)
print()
client.view_cart()

client.remove_from_cart(3)
print()
client.view_cart()