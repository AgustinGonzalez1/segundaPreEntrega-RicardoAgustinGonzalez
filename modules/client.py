from modules.persona import Persona
from products import Products

class Client(Persona):
  def __init__(self, name, last_name, age, cart):
    super().__init__(name, last_name, age)
    self.cart = cart
  
  def add_to_cart(self, product_number):
    try:
      product = Products[product_number - 1]
    
      if product in self.cart:
        product["quantity"] += 1
        product["product_price"] = product["product_price"] * product["quantity"]
      else:
        product["quantity"] = 1
        self.cart.append(product)
    except:
      print("No se encontró el producto: ", product_number)
  
  def remove_from_cart(self, product_number):
    try:
      product = Products[product_number - 1]
    
      if product in self.cart:
        self.cart.remove(product)
      else:
        print("El producto no está en el carrito")
    except:
      print("No se encontró el producto: ", product_number)
    

  
  def view_cart(self):
    if len(self.cart) == 0:
      print("El carrito esta vacío")
    else:
      print("Carrito:")
      for product in self.cart:
        print(f"Product: {product['product_name']}, price: {product['product_price']}, quantity: {product['quantity']}")
      
      total = 0
      for product in self.cart:
        total += int(product["product_price"])
      print(f"Total: {total}")
  
  def view_products(self):
    for product in Products:
      i = Products.index(product) + 1
      print(f"{i} - Product: {product['product_name']}, price: {product['product_price']}")
    
