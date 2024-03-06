class Persona:
  def __init__(self, name, last_name, age):
    self.name = name
    self.last_name = last_name
    self.age = age
  
  def __str__(self):
    return f"Cliente {self.name} {self.last_name}, edad: {self.age}"