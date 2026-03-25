# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_garden_security.py                              :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 10:14:49 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 10:14:49 by mamiandr         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#!usr/bin/env python3

class Plant:
	""" A class representing a plant with a name, height, and age."""
	def __init__(self, name: str, height: float, age: int):
		if not Plant.attribute_validation(name, height, age):
			raise ValueError("Invalid plant attributes.")
		self.name:str = name
		self._height:float = height
		self._age:int = age

	def show(self)-> None:
		print(f"{self.name}: {round(self._height, 1)}cm, {self._age} days old")

	def age(self, days: int=1)-> None:
		self._age += days

	def grow(self, daily_growth: float = 0.8)->float:
		self._height += daily_growth
		self.age()
		return daily_growth

	@classmethod
	def from_dict(cls, dico: dict):
		if not cls.attribute_validation(dico["name"], dico["height"], dico["age"]):
			raise ValueError("Invalid plant attributes.")
		return cls(**dico)

	@staticmethod
	def attribute_validation(name: str, height: float, age: int)-> bool:
		if not name:
			print("Error: Name must be a non-empty string.")
			return False
		if height < 0:
			print("Error: Height must be a non-negative number.")
			return False
		if age < 0:
			print("Error: Age must be a non-negative integer.")
			return False
		return True

	def get_height(self)-> float:
		return self._height

	def get_age(self)-> int:
		return self._age

	def set_height(self, height: float)-> None:
		if height < 0:
			print(f"{self.name}: Error, height can't be negative")
			print("Height update rejected")
			return
		self._height = height
		print(f"Height updated: {int(self._height)}cm")
  
	def set_age(self, age: int)-> None:
		if age < 0:
			print(f"{self.name}: Error, Age can't be negative")
			print("Age update rejected")
			return
		self._age = age
		print(f"Age updated: {self._age} days")

if __name__ == "__main__":
    factory_plants = {"name": "Rose", "height": 15.0, "age": 10}
    print("=== Garden Security System ===")
    Rose = Plant.from_dict(factory_plants)
    print("Plant created: ", end="")
    Rose.show()
    print()
    Rose.set_height(25.0)
    Rose.set_age(30)
    print()
    Rose.set_height(-5.0)
    Rose.set_age(-10)
    print()
    print("Current state: ", end="")
    Rose.show()