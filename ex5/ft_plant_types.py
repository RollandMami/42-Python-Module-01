# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    ft_plant_types.py                                  :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: mamiandr <mamiandr@student.42antananari    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/03/24 11:39:15 by mamiandr          #+#    #+#              #
#    Updated: 2026/03/24 11:39:15 by mamiandr         ###   ########.fr        #
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
		self.height += daily_growth
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

class Flower(Plant):
	def __init__(self, name: str, height: float, age: int, color: str):
		super().__init__(name, height, age)
		self._color:str = color
		self._blooming:bool = False

	def show(self)-> None:
		super().show()
		print(f" Color: {self._color}")
		if self._blooming:
			print(f" {self.name} is blooming beautifully!")
		else:
			print(f" {self.name} has not blooming yet")

	def bloom(self)-> None:
		print("[asking the flower to bloom]")
		self._blooming = True
		if not self._blooming:
			print(f"{self.name} failed to bloom.")

class Tree(Plant):
	def __init__(self, name: str, height: float, age: int, trunk_diameter : float):
		super().__init__(name, height, age)
		self._trunk_diameter:float = trunk_diameter

	def show(self)-> None:
		super().show()
		print(f" Truck diameter: {self._trunk_diameter}cm")

	def produce_shade(self)-> None:
		print(f"[asking the {self.name.lower()} to produce shade]")
		print(f"Tree {self.name.capitalize()} now providing a shade of {self.get_height()}cm long and {self._trunk_diameter}cm wide.")

class Vegetables(Plant):
	def __init__(self, name: str, height: float, age: int, harvest_season: str):
		super().__init__(name, height, age)
		self._harvest_season:str = harvest_season
		self._nutritional_value:int = 0

	def show(self)-> None:
		super().show()
		print(f" Harvest season: {self._harvest_season}\n Nutritional value: {self._nutritional_value}")

	def harvest(self)-> None:
		print(f"{self.name} is ready to be harvested!")

	def age(self, days: int = 1)-> None:
		super().age(days)
		self._nutritional_value += days

	def grow(self, daily_growth: float = 0.8)->float:
		growth = super().grow(daily_growth)
		self._nutritional_value += 1
		return growth


if __name__ == "__main__":
	print("=== Garden Plant Types ===")
	my_flower = Flower(name="Rose", height=25.0, age=30, color="Red")
	my_tree = Tree(name="Oak", height=200.0, age=365, trunk_diameter=50.0)
	my_vegetable = Vegetables(name="Carrot", height=15.0, age=60, harvest_season="Spring")
	
	print("\n=== Flower")
	my_flower.show()
	my_flower.bloom()
	my_flower.show()

	print("\n=== Tree")
	my_tree.show()
	my_tree.produce_shade()

	print("\n=== Vegetable")
	my_vegetable.show()
	for day in range(1, 6):
		print(f"\nDay {day}:")
		my_vegetable.grow()
		my_vegetable.show()