#!/usr/bin/env python3

APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]

class Dog:
   def __init__(self, name):
     self.name =None
     def get_name(self):
       return self._name
   def set_name(self, name):
    if (type(name) in (str)) and (1 <= len(name) <= 25):
      self._name = name
    else:
      print("Name must be string between 1 and 25 characters.")
fido = Dog()
pass
